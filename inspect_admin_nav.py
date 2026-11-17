with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

lines = admin_html.splitlines()
for i, l in enumerate(lines[:170]):
    if 'data-tab=' in l:
        print(f"Line {i+1}: {l.strip()}")
