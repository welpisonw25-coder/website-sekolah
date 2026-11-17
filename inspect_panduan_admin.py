with open('panduan-serah-terima.html', 'r', encoding='utf-8') as f:
    panduan_html = f.read()

lines = panduan_html.splitlines()
for i, l in enumerate(lines):
    if 'admin.html' in l or 'dashboard' in l.lower() or 'kelola' in l.lower():
        print(f"{i+1}: {l.strip()[:100]}")
