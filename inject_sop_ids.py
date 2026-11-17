import re

# 1. Update sop.html
with open('sop.html', 'r', encoding='utf-8') as f:
    sop = f.read()

# Add id to sopTataTertibGuruList if not present
if 'id="sopTataTertibGuruList"' not in sop:
    sop = sop.replace('<ol class="sop-list" type="a">', '<ol class="sop-list" type="a" id="sopTataTertibGuruList">', 1)

# Add id to sopTataTertibSiswaList if not present
if 'id="sopTataTertibSiswaList"' not in sop:
    # Notice second ol class="sop-list" type="a"
    pattern = r'(<h4 style="font-size: 15px; font-weight: 700; color: var\(--primary\); margin: 0 0 10px;">A\. Ketentuan Tata Tertib Masuk & Aktivitas Harian:</h4>\s*<ol class="sop-list" type="a")'
    sop = re.sub(pattern, r'\1 id="sopTataTertibSiswaList"', sop)

# Add id to sopTabelSeragamGuruBody
if 'id="sopTabelSeragamGuruBody"' not in sop:
    pattern_seragam = r'(<table class="table-sop">[\s\S]*?<thead>[\s\S]*?</thead>\s*<tbody)'
    sop = re.sub(pattern_seragam, r'\1 id="sopTabelSeragamGuruBody"', sop, count=1)

# Add id to sopJadwalPiketGuruGrid
if 'id="sopJadwalPiketGuruGrid"' not in sop:
    pattern_piket = r'(POIN 5: JADWAL PIKET GURU[\s\S]*?<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(260px, 1fr\)\); gap: 14px;")'
    sop = re.sub(pattern_piket, r'\1 id="sopJadwalPiketGuruGrid"', sop, count=1)

# Add id to sopPramukaJadwalText
if 'id="sopPramukaJadwalText"' not in sop:
    pattern_pramuka_text = r'(<div style="background: #f8fafc; border: 1px solid var\(--border-color\); border-radius: var\(--radius-sm\); padding: 12px 16px; margin-bottom: 16px; font-size: 13\.5px; color: #334155;")'
    sop = re.sub(pattern_pramuka_text, r'\1 id="sopPramukaJadwalText"', sop, count=1)

# Add id to sopPramukaSiagaList
if 'id="sopPramukaSiagaList"' not in sop:
    pattern_siaga = r'(PRAMUKA SIAGA \(Kelas 1, 2, dan 3\)</h4>[\s\S]*?<ul style="margin: 0; padding-left: 18px; font-size: 13\.5px; color: #1e293b; display: flex; flex-direction: column; gap: 4px;")'
    sop = re.sub(pattern_siaga, r'\1 id="sopPramukaSiagaList"', sop, count=1)

# Add id to sopPramukaPenggalangList
if 'id="sopPramukaPenggalangList"' not in sop:
    pattern_penggalang = r'(PRAMUKA PENGGALANG \(Kelas 4, 5, dan 6\)</h4>[\s\S]*?<ul style="margin: 0; padding-left: 18px; font-size: 13\.5px; color: #1e293b; display: flex; flex-direction: column; gap: 4px;")'
    sop = re.sub(pattern_penggalang, r'\1 id="sopPramukaPenggalangList"', sop, count=1)

with open('sop.html', 'w', encoding='utf-8') as f:
    f.write(sop)

print("sop.html updated with dynamic IDs!")
