import os
import re
import json
import requests
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser

PAGES = [
    ('/', 'https://www.sacredorigins.org/'),
    ('/about-us', 'https://www.sacredorigins.org/about-us'),
    ('/offerings', 'https://www.sacredorigins.org/offerings'),
    ('/scheduling', 'https://www.sacredorigins.org/scheduling'),
    ('/upcoming-retreat', 'https://www.sacredorigins.org/upcoming-retreat'),
    ('/contact', 'https://www.sacredorigins.org/contact'),
    ('/blog', 'https://www.sacredorigins.org/blog'),
    ('/blog/the-pharmacology-of-kambo-how-its-compounds-affect-the-human-body', 'https://www.sacredorigins.org/blog/the-pharmacology-of-kambo-how-its-compounds-affect-the-human-body'),
    ('/blog/the-sacred-origins-of-sananga-history-benefits-and-usage', 'https://www.sacredorigins.org/blog/the-sacred-origins-of-sananga-history-benefits-and-usage'),
    ('/blog/81aapg1ja12yc9wjolnnpckod4loeh', 'https://www.sacredorigins.org/blog/81aapg1ja12yc9wjolnnpckod4loeh'),
    ('/blog/getting-ready-for-your-kambo-ceremony-a-friendly-guide', 'https://www.sacredorigins.org/blog/getting-ready-for-your-kambo-ceremony-a-friendly-guide'),
    ('/blog/discovering-kambo-a-sacred-healing-tradition-for-modern-times', 'https://www.sacredorigins.org/blog/discovering-kambo-a-sacred-healing-tradition-for-modern-times')
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

RAW_DIR = 'scraped_data'
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(os.path.join(RAW_DIR, 'images'), exist_ok=True)

class ContentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.in_title = False
        self.headings = []
        self.current_tag = None
        self.paragraphs = []
        self.links = []
        self.images = []
        self.text_chunks = []
        self.current_heading_text = ''
        self.current_p_text = ''

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attrs_dict = dict(attrs)
        if tag == 'title':
            self.in_title = True
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.current_heading_text = ''
        elif tag == 'p':
            self.current_p_text = ''
        elif tag == 'a' and 'href' in attrs_dict:
            self.links.append({'href': attrs_dict['href']})
        elif tag == 'img':
            src = attrs_dict.get('src') or attrs_dict.get('data-src') or attrs_dict.get('data-image')
            alt = attrs_dict.get('alt', '')
            if src:
                self.images.append({'src': src, 'alt': alt})

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            if self.current_heading_text.strip():
                self.headings.append({'level': tag, 'text': self.current_heading_text.strip()})
            self.current_heading_text = ''
        elif tag == 'p':
            if self.current_p_text.strip():
                self.paragraphs.append(self.current_p_text.strip())
            self.current_p_text = ''
        self.current_tag = None

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.current_tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.current_heading_text += data
        elif self.current_tag == 'p':
            self.current_p_text += data
        text = data.strip()
        if text:
            self.text_chunks.append(text)

results = {}
all_image_urls = set()

for route, url in PAGES:
    print(f"Fetching {route} -> {url} ...", flush=True)
    try:
        res = requests.get(url, headers=HEADERS, timeout=20)
        res.raise_for_status()
        html = res.text
        
        # Save raw HTML
        clean_name = route.replace('/', '_').strip('_') or 'home'
        with open(os.path.join(RAW_DIR, f"{clean_name}.html"), 'w', encoding='utf-8') as f:
            f.write(html)
            
        parser = ContentParser()
        parser.feed(html)
        
        # Also find all image urls via regex in squarespace markup
        # Squarespace often uses data-src or data-image
        sq_images = re.findall(r'(https?://images\.squarespace-cdn\.com/content/[^\s"\'\?<>]+)', html)
        sq_static = re.findall(r'(https?://static1\.squarespace\.com/static/[^\s"\'\?<>]+)', html)
        
        found_imgs = []
        for img in parser.images:
            found_imgs.append(img)
            all_image_urls.add(img['src'])
        for sq in sq_images + sq_static:
            all_image_urls.add(sq)
            found_imgs.append({'src': sq, 'alt': ''})
            
        results[route] = {
            'url': url,
            'title': parser.title.strip(),
            'headings': parser.headings,
            'paragraphs': parser.paragraphs,
            'images': found_imgs
        }
    except Exception as e:
        print(f"Failed {route}: {e}", flush=True)

with open(os.path.join(RAW_DIR, 'site_content.json'), 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

with open(os.path.join(RAW_DIR, 'all_images.json'), 'w', encoding='utf-8') as f:
    json.dump(list(all_image_urls), f, indent=2)

print(f"Done! Scraped {len(results)} pages and found {len(all_image_urls)} unique image URLs.", flush=True)
