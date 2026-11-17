with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(max(0, len(lines)-60), len(lines)):
    print(f'{j+1}: {lines[j]}', end='')
