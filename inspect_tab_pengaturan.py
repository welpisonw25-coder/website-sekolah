with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="tab-pengaturan"' in l:
        for j in range(max(0, i-5), min(len(lines), i+150)):
            print(f'{j+1}: {lines[j]}', end='')
        break
