with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    pg_html = f.read()

# Let's inspect lines around sekretariat, ketua, waktu, dasar penetapan
lines = pg_html.splitlines()
for i, l in enumerate(lines):
    if 'Sekretariat:' in l or 'Ketua Pengelola:' in l or 'Waktu Pertemuan:' in l or 'Dasar Penetapan:' in l or 'Uraian Kerja & Program Strategis K3S' in l:
        print(f"Line {i+1}: {l.strip()}")
