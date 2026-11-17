with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    pg_html = f.read()

lines_pg = pg_html.splitlines()
for i, l in enumerate(lines_pg):
    if 'getkkgdata' in l.lower() or 'sdn_kkg_data' in l.lower() or 'sdn_database' in l.lower() or '<script>' in l.lower() or '<script ' in l.lower():
        print(f"Line {i+1}: {l.strip()[:100]}")
