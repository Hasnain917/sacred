import re
from html.parser import HTMLParser

class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.labels = []
        self.in_label = False
        self.cur_label = ''
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == 'input':
            self.inputs.append(d)
        elif tag == 'textarea':
            self.inputs.append(d)
        elif tag == 'select':
            self.inputs.append(d)
        elif tag == 'label':
            self.in_label = True
            self.cur_label = ''
    def handle_endtag(self, tag):
        if tag == 'label':
            self.in_label = False
            if self.cur_label.strip():
                self.labels.append(self.cur_label.strip())
    def handle_data(self, data):
        if self.in_label:
            self.cur_label += data

for p in ['contact.html', 'home.html']:
    with open(f'scraped_data/{p}', 'r', encoding='utf-8') as f:
        html = f.read()
    fp = FormParser()
    fp.feed(html)
    print(f"\n=== Forms in {p} ===")
    print("Labels found:", fp.labels)
    print("Inputs found:", [(i.get('name'), i.get('type'), i.get('placeholder')) for i in fp.inputs])
