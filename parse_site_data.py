import os
import glob
import json
import re
from html.parser import HTMLParser

class SectionParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.current_section = []
        self.current_tag = None
        self.text_buf = ''
        self.in_script = False
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript'):
            self.in_script = True
            return
        self.current_tag = tag
        attrs_dict = dict(attrs)
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'button', 'a'):
            self.text_buf = ''
        elif tag == 'img':
            src = attrs_dict.get('src') or attrs_dict.get('data-src') or attrs_dict.get('data-image')
            alt = attrs_dict.get('alt', '')
            if src:
                self.current_section.append({'type': 'img', 'src': src, 'alt': alt})

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript'):
            self.in_script = False
            return
        if self.in_script:
            return
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'button', 'a'):
            t = self.text_buf.strip()
            if t:
                self.current_section.append({'type': tag, 'text': t})
            self.text_buf = ''
        elif tag in ('section', 'article', 'div') and len(self.current_section) > 5:
            # chunking
            pass

    def handle_data(self, data):
        if self.in_script:
            return
        self.text_buf += data

pages_data = {}
for html_file in glob.glob('scraped_data/*.html'):
    page_name = os.path.splitext(os.path.basename(html_file))[0]
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract title
    m_title = re.search(r'<title>(.*?)</title>', html, re.I)
    title = m_title.group(1) if m_title else page_name
    title = re.sub(r'&quot;|&#124;|&amp;', lambda m: {'&quot;':'"', '&#124;':'|', '&amp;':'&'}[m.group(0)], title)
    
    # Extract description
    m_desc = re.search(r'<meta\s+(?:name|property)="[^"]*description"[^>]*content="([^"]*)"', html, re.I)
    desc = m_desc.group(1) if m_desc else ""
    
    # Extract main content text
    # Squarespace puts content inside #page or main or .page-section
    parser = SectionParser()
    parser.feed(html)
    
    # Filter items
    cleaned_items = []
    seen = set()
    skip_phrases = ['Skip to Content', 'Cart', '0', 'Open Menu', 'Close Menu', 'Back to Top']
    for item in parser.current_section:
        if item['type'] == 'img':
            cleaned_items.append(item)
        else:
            txt = item['text'].strip()
            if txt in skip_phrases or len(txt) == 0:
                continue
            # avoid exact duplicate consecutive
            if cleaned_items and cleaned_items[-1].get('text') == txt:
                continue
            cleaned_items.append(item)
            
    pages_data[page_name] = {
        'title': title,
        'description': desc,
        'items': cleaned_items
    }

with open('scraped_data/structured_pages.json', 'w', encoding='utf-8') as f:
    json.dump(pages_data, f, indent=2)

print(f"Extracted structured content for {len(pages_data)} pages.")
