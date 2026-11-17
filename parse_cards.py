import re

with open('kolaborasi.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_tag = 'id="kolaborasiListContainer"'
pos1 = text.find(start_tag)
pos2 = text.find('</section>', pos1)
cards_block = text[pos1:pos2]

cards = cards_block.split('<div class="card"')
for idx, c in enumerate(cards[1:], 1):
    c = '<div class="card"' + c
    title_m = re.search(r'<h3[^>]*>(.*?)</h3>', c, re.DOTALL)
    badge_m = re.search(r'class="badge-tag"[^>]*>(.*?)</span>', c, re.DOTALL)
    img_m = re.search(r'<img[^>]+src="([^">]+)"', c)
    pic_m = re.search(r'Penanggung Jawab:\s*<strong[^>]*>(.*?)</strong>', c, re.DOTALL)
    per_m = re.search(r'Periode:\s*<strong[^>]*>(.*?)</strong>', c, re.DOTALL)
    
    print(f"--- CARD {idx} ---")
    print("Title:", title_m.group(1).strip() if title_m else "N/A")
    print("Badge:", badge_m.group(1).strip() if badge_m else "N/A")
    print("Image:", img_m.group(1) if img_m else "N/A")
    print("PIC:", pic_m.group(1).strip() if pic_m else "N/A")
    print("Periode:", per_m.group(1).strip() if per_m else "N/A")
