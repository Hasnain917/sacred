import re

for page in ['scheduling', 'contact', 'home']:
    with open(f'scraped_data/{page}.html', 'r', encoding='utf-8') as f:
        html = f.read()
    print(f"\n--- {page}.html ---")
    iframes = re.findall(r'<iframe[^>]*src="([^"]*)"', html, re.I)
    forms = re.findall(r'<form[^>]*action="([^"]*)"', html, re.I)
    sq_scheduling = re.findall(r'https?://[^\s"\'<>]+(?:acuity|calendly|scheduling|squarespace)[^\s"\'<>]*', html, re.I)
    print("Iframes:", iframes)
    print("Forms:", forms)
    print("Scheduling links:", [l for l in sq_scheduling if 'scheduling' in l or 'acuity' in l or 'calendly' in l])
