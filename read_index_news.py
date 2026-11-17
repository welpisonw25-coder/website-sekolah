with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

lines = index_html.splitlines()
for i, l in enumerate(lines):
    if 'homeNewsGrid' in l or 'homenewsgrid' in l.lower():
        for j in range(i, min(i+40, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
