with open('js/admin.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(100, 180):
    print(f'{j+1}: {lines[j]}', end='')
