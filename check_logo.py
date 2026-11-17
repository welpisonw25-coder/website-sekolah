import os
import glob
import requests

print("=== Check local images folder ===")
files = os.listdir('images')
for f in files:
    if any(k in f.lower() for k in ['logo', 'tutwuri', 'keerom', 'papua']):
        size = os.path.getsize(os.path.join('images', f))
        print(f"Local file: images/{f} ({size} bytes)")

print("\n=== Check references in index.html ===")
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
img_tags = re.findall(r'<img[^>]*src=[\'"]([^\'"]+)[\'"][^>]*>', html)
for src in img_tags:
    if any(k in src.lower() for k in ['logo', 'tutwuri', 'keerom', 'papua', 'icon']):
        print(f"Referenced in index.html: {src}")

print("\n=== Check live HTTP requests ===")
check_urls = [
    'https://sdninpresarso8.sch.id/images/logo-keerom.png',
    'https://sdninpresarso8.sch.id/images/tutwuri.png',
    'https://sdninpresarso8.sch.id/images/logo.png',
    'https://sdninpresarso8.sch.id/images/logo-sd.png',
    'https://sdninpresarso8.sch.id/favicon.ico'
]

for u in check_urls:
    try:
        r = requests.get(u, timeout=10)
        print(f"{u} -> Status: {r.status_code}, Length: {len(r.content)}, Content-Type: {r.headers.get('content-type')}")
    except Exception as e:
        print(f"{u} -> Error: {e}")
