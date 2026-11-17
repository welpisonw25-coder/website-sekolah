with open('profil.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(135, 205):
    print(f'{j+1}: {lines[j]}', end='')
