with open('js/admin.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'function getUserData()' in l:
        for j in range(max(0, i-10), min(len(lines), i+15)):
            print(f'{j+1}: {lines[j]}', end='')
        break
