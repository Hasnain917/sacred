import json

with open('scraped_data/structured_pages.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('scraped_data/inspection_summary.txt', 'w', encoding='utf-8') as out:
    for k, v in d.items():
        out.write(f"\n============================ PAGE: {k} ============================\n")
        out.write(f"TITLE: {v['title']}\n")
        out.write(f"DESC: {v['description']}\n")
        out.write(f"TOTAL ITEMS: {len(v['items'])}\n")
        for it in v['items']:
            if it['type'] == 'img':
                out.write(f"  [IMG] src={it['src']} alt={it.get('alt')}\n")
            elif it['type'] in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                out.write(f"  [{it['type'].upper()}] {it['text']}\n")
            elif it['type'] == 'p':
                out.write(f"  [P] {it['text']}\n")
            elif it['type'] == 'li':
                out.write(f"  [LI] {it['text']}\n")
            elif it['type'] in ('button', 'a'):
                out.write(f"  [{it['type'].upper()}] {it['text']}\n")

print("Wrote inspection summary in UTF-8.")
