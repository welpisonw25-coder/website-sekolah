with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'CATATAN RIWAYAT AKTIVITAS' in l:
        for j in range(max(0, i-10), min(len(lines), i+65)):
            print(f'{j+1}: {lines[j]}', end='')
        break
