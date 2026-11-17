with open('berita.html', 'r', encoding='utf-8') as f:
    berita_html = f.read()

lines = berita_html.splitlines()
print(f"Total lines in berita.html: {len(lines)}")
for i, l in enumerate(lines):
    if 'news-grid' in l or 'beritaListGrid' in l or 'loadDynamicNews' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")
