with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

lines = admin_html.splitlines()
for i, l in enumerate(lines):
    if 'id="addBeritaForm"' in l or 'id="beritaFileInput"' in l:
        for j in range(max(0, i-5), min(i+40, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
