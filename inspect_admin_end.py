with open('js/admin.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Total lines in js/admin.js:', len(lines))
for j in range(5415, min(len(lines), 5460)):
    print(f'{j+1}: {lines[j]}', end='')
