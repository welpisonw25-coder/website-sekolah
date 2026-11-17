with open('js/admin.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(5640, min(len(lines), 5804)):
    print(f'{j+1}: {lines[j]}', end='')
