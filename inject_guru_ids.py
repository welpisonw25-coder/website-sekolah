import re

with open('guru.html', 'r', encoding='utf-8') as f:
    guru = f.read()

# Add id to guruTataTertibList
if 'id="guruTataTertibList"' not in guru:
    pattern_tatib = r'(<h3 style="font-size: 18px; color: var\(--primary-dark\); font-weight: 800; margin: 0;">\s*👨‍🏫 11 Poin Tata Tertib Guru & Tenaga Kependidikan\s*</h3>[\s\S]*?<ol style="margin: 0; padding-left: 20px; font-size: 14px; color: #334155; line-height: 1\.7; display: flex; flex-direction: column; gap: 8px;")'
    guru = re.sub(pattern_tatib, r'\1 id="guruTataTertibList"', guru, count=1)

# Add id to guruJadwalPiketGrid
if 'id="guruJadwalPiketGrid"' not in guru:
    pattern_piket = r'(Jadwal Piket Harian Guru \(Senin – Jumat\)[\s\S]*?<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(200px, 1fr\)\); gap: 14px;")'
    guru = re.sub(pattern_piket, r'\1 id="guruJadwalPiketGrid"', guru, count=1)

# Add id to guruSeragamTableBody
if 'id="guruSeragamTableBody"' not in guru:
    pattern_seragam = r'(Jadwal Pemakaian Seragam Guru[\s\S]*?<thead>[\s\S]*?</thead>\s*<tbody)'
    guru = re.sub(pattern_seragam, r'\1 id="guruSeragamTableBody"', guru, count=1)

# Add id to guruPramukaSiagaList
if 'id="guruPramukaSiagaList"' not in guru:
    pattern_siaga = r'(Pembina Pramuka Siaga \(Kls 1, 2, 3\)[\s\S]*?<ul style="margin: 0; padding-left: 18px; font-size: 13\.5px; color: #334155; display: flex; flex-direction: column; gap: 4px;")'
    guru = re.sub(pattern_siaga, r'\1 id="guruPramukaSiagaList"', guru, count=1)

# Add id to guruPramukaPenggalangList
if 'id="guruPramukaPenggalangList"' not in guru:
    pattern_penggalang = r'(Pembina Pramuka Penggalang \(Kls 4, 5, 6\)[\s\S]*?<ul style="margin: 0; padding-left: 18px; font-size: 13\.5px; color: #334155; display: flex; flex-direction: column; gap: 4px;")'
    guru = re.sub(pattern_penggalang, r'\1 id="guruPramukaPenggalangList"', guru, count=1)

with open('guru.html', 'w', encoding='utf-8') as f:
    f.write(guru)

print("guru.html updated with dynamic IDs!")
