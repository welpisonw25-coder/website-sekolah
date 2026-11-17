import re, json

with open('kolaborasi.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_tag = 'id="kolaborasiListContainer"'
pos1 = text.find(start_tag)
pos2 = text.find('</section>', pos1)
cards_block = text[pos1:pos2]

raw_cards = cards_block.split('<div class="card"')
extracted = []

for idx, c in enumerate(raw_cards[1:], 1):
    c = '<div class="card"' + c
    
    # Icon
    icon_m = re.search(r'font-size:\s*34px[^>]*>\s*([^<]+)\s*</span>', c)
    icon = icon_m.group(1).strip() if icon_m else '🤝'
    
    # Badge
    badge_m = re.search(r'class="badge-tag"[^>]*>\s*([^<]+)\s*</span>', c)
    badge = badge_m.group(1).strip() if badge_m else 'KEMITRAAN'
    
    # Title
    title_m = re.search(r'<h3[^>]*>\s*([^<]+)\s*</h3>', c)
    title = title_m.group(1).strip() if title_m else f'Pilar {idx}'
    
    # Status
    status_m = re.search(r'<span style="background:\s*#dcfce7[^>]*>\s*([^<]+)\s*</span>', c)
    status = status_m.group(1).strip() if status_m else '🟢 Aktif Berjalan Rutin'
    
    # Summary (first p after title)
    p_m = re.search(r'<p style="font-size:\s*14px[^>]*>(.*?)</p>', c, re.DOTALL)
    desc = re.sub(r'\s+', ' ', p_m.group(1).strip()) if p_m else ''
    
    # Image
    img_m = re.search(r'<img[^>]+src="([^">]+)"[^>]*alt="([^">]*)"', c)
    img_src = img_m.group(1) if img_m else ''
    img_alt = img_m.group(2) if img_m else ''
    
    # Image caption
    cap_m = re.search(r'<span>📌</span>\s*<span>(.*?)</span>', c, re.DOTALL)
    caption = re.sub(r'\s+', ' ', cap_m.group(1).strip()) if cap_m else ''
    
    # Uraian kerja list
    ul_m = re.search(r'<ul[^>]*>(.*?)</ul>', c, re.DOTALL)
    lis = []
    if ul_m:
        lis = [re.sub(r'\s+', ' ', item.strip()) for item in re.findall(r'<li[^>]*>(.*?)</li>', ul_m.group(1), re.DOTALL)]
    
    # PIC and Periode
    pic_m = re.search(r'Penanggung Jawab:\s*<strong[^>]*>(.*?)</strong>', c, re.DOTALL)
    per_m = re.search(r'Periode:\s*<strong[^>]*>(.*?)</strong>', c, re.DOTALL)
    pic = pic_m.group(1).strip() if pic_m else ''
    periode = per_m.group(1).strip() if per_m else ''
    
    extracted.append({
        'idx': idx,
        'icon': icon,
        'badge': badge,
        'title': title,
        'status': status,
        'desc': desc,
        'foto': img_src,
        'foto_alt': img_alt,
        'keterangan_foto': caption,
        'uraian_kerja': lis,
        'pic': pic,
        'periode': periode
    })

print(f"Extracted {len(extracted)} items.")
for item in extracted:
    print(f"Pilar {item['idx']}: {item['title']} - {len(item['uraian_kerja'])} poin kerja - Foto: {item['foto']}")

with open('scratch/extracted_kolaborasi.json', 'w', encoding='utf-8') as out:
    json.dump(extracted, out, ensure_ascii=False, indent=2)
print("Saved to scratch/extracted_kolaborasi.json")
