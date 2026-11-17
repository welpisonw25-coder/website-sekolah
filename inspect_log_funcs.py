with open('js/admin.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'function logAdminActivity' in l:
        for j in range(max(0, i-5), min(len(lines), i+80)):
            print(f'{j+1}: {lines[j]}', end='')
        break
