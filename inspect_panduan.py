with open('panduan-serah-terima.html', 'r', encoding='utf-8') as f:
    panduan_html = f.read()

lines = panduan_html.splitlines()
print(f"Total lines in panduan-serah-terima.html: {len(lines)}")
for i, l in enumerate(lines):
    if any(k in l.lower() for k in ['sop', 'tata tertib', 'kkg', 'k3s', 'seragam', 'piket']):
        print(f"{i+1}: {l.strip()[:100]}")
