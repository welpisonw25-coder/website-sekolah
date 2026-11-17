with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(120, 260):
    print(f'{j+1}: {lines[j]}', end='')
