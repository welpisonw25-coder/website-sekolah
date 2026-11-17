import os
import re
import urllib.parse

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f"=== AUDIT OF ALL {len(html_files)} HTML FILES ===")

broken_links = []
missing_assets = []

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check local href links
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in hrefs:
        href_clean = href.split('?')[0].split('#')[0]
        if not href_clean or href.startswith('http') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('javascript:'):
            continue
        if not os.path.exists(href_clean):
            broken_links.append((hf, href))

    # Check local src assets (images, scripts, etc.)
    srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
    for src in srcs:
        src_clean = src.split('?')[0].split('#')[0]
        if not src_clean or src.startswith('http') or src.startswith('data:'):
            continue
        if not os.path.exists(src_clean):
            missing_assets.append((hf, src))

print(f"Broken href links: {len(broken_links)}")
for b in broken_links:
    print(f"  In {b[0]}: {b[1]}")

print(f"Missing src assets: {len(missing_assets)}")
for m in missing_assets:
    print(f"  In {m[0]}: {m[1]}")

# Check data_sekolah.json integrity
import json
try:
    with open('data_sekolah.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("data_sekolah.json is valid JSON with keys:", list(data.keys()))
except Exception as e:
    print("data_sekolah.json error:", e)

# Check js/main.js and js/admin.js syntax
try:
    with open('js/main.js', 'r', encoding='utf-8') as f:
        js_main = f.read()
    print("js/main.js size:", len(js_main), "bytes")
    with open('js/admin.js', 'r', encoding='utf-8') as f:
        js_admin = f.read()
    print("js/admin.js size:", len(js_admin), "bytes")
except Exception as e:
    print("JS read error:", e)
