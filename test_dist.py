import os
import re
from pathlib import Path
from html.parser import HTMLParser

dist = Path('dist')
html_files = list(dist.rglob('*.html'))
print(f"Testing {len(html_files)} HTML files in dist/...")

class LinkChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.img_srcs = []
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == 'img' and 'src' in d:
            self.img_srcs.append(d['src'])
        if tag == 'a' and 'href' in d:
            self.hrefs.append(d['href'])

missing_images = set()
missing_links = set()

for h in html_files:
    content = h.read_text(encoding='utf-8')
    parser = LinkChecker()
    parser.feed(content)
    
    # Check images
    for src in parser.img_srcs:
        if src.startswith('/'):
            local_path = dist / src.lstrip('/')
            if not local_path.exists():
                missing_images.add((str(h.relative_to(dist)), src))
                
    # Also check inline styles with background-image:url(...)
    for bg in re.findall(r'url\([\'"]?(/[^\'")]+)[\'"]?\)', content):
        local_bg = dist / bg.lstrip('/')
        if not local_bg.exists():
            missing_images.add((str(h.relative_to(dist)), bg))
            
    # Check internal links
    for href in parser.hrefs:
        if href.startswith('/') and not href.startswith('//'):
            clean_href = href.split('?')[0].split('#')[0]
            if clean_href in ('/', ''):
                continue
            target = dist / clean_href.strip('/') / 'index.html'
            if not target.exists() and not (dist / clean_href.lstrip('/')).exists():
                missing_links.add((str(h.relative_to(dist)), href))

if missing_images:
    print(f"WARNING: Missing images found ({len(missing_images)}):")
    for src in missing_images:
        print(" ", src)
else:
    print("SUCCESS: All local images and background images exist on disk!")

if missing_links:
    print(f"WARNING: Missing link targets ({len(missing_links)}):")
    for lnk in missing_links:
        print(" ", lnk)
else:
    print("SUCCESS: All internal links resolve to valid generated pages!")
