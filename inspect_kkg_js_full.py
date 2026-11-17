with open('js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'kkgDokumentasiGrid' in l:
        for j in range(max(0, i-30), min(len(lines), i+60)):
            print(f'{j+1}: {lines[j]}', end='')
        break
