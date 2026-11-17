with open('guru.html', 'r', encoding='utf-8') as f:
    guru = f.read()

lines = guru.splitlines()
for i, l in enumerate(lines):
    if 'Tata Tertib, Piket & Seragam Dewan Guru' in l:
        for j in range(i, min(i+40, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
