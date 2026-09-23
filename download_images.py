import os
import re
import json
import requests
from urllib.parse import urlparse, unquote

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

IMG_DIR = os.path.join('dist', 'assets', 'images')
os.makedirs(IMG_DIR, exist_ok=True)

with open('scraped_data/all_images.json', 'r', encoding='utf-8') as f:
    image_urls = json.load(f)

url_to_local = {}

for u in image_urls:
    u = u.strip().rstrip('",;')
    if not u.startswith('http'):
        if u.startswith('//'):
            u = 'https:' + u
        else:
            continue
    if '.css' in u or '.js' in u or 'favicon.ico' in u or u.endswith('/'):
        continue
    
    # Generate clean filename
    parsed = urlparse(u)
    path = unquote(parsed.path)
    base = os.path.basename(path)
    if not base or '.' not in base:
        continue
    
    # Normalize filename
    clean_base = re.sub(r'[^a-zA-Z0-9_\.-]', '_', base).lower()
    local_path = os.path.join(IMG_DIR, clean_base)
    
    # Download with query param format=1500w or format=original if possible
    download_url = u.split('?')[0] + '?format=1500w'
    
    if not os.path.exists(local_path) or os.path.getsize(local_path) == 0:
        print(f"Downloading {clean_base} from {download_url} ...", flush=True)
        try:
            r = requests.get(download_url, headers=HEADERS, timeout=15)
            if r.status_code == 200 and len(r.content) > 500:
                with open(local_path, 'wb') as img_f:
                    img_f.write(r.content)
                url_to_local[u] = f"/assets/images/{clean_base}"
            else:
                # try without query
                r2 = requests.get(u, headers=HEADERS, timeout=15)
                if r2.status_code == 200 and len(r2.content) > 500:
                    with open(local_path, 'wb') as img_f:
                        img_f.write(r2.content)
                    url_to_local[u] = f"/assets/images/{clean_base}"
        except Exception as e:
            print(f"Error downloading {u}: {e}", flush=True)
    else:
        url_to_local[u] = f"/assets/images/{clean_base}"

with open('scraped_data/url_to_local_images.json', 'w', encoding='utf-8') as f:
    json.dump(url_to_local, f, indent=2)

print(f"Downloaded {len(url_to_local)} images successfully into {IMG_DIR}!")
