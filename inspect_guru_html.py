with open('guru.html', 'r', encoding='utf-8') as f:
    guru_html = f.read()

lines_guru = guru_html.splitlines()
for i, l in enumerate(lines_guru):
    if any(k in l.lower() for k in ['piket', 'seragam', 'pramuka', 'sop', 'tata tertib', 'kkg', 'k3s']):
        print(f"Line {i+1}: {l.strip()[:100]}")
