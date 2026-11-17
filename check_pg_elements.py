with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    pg = f.read()

lines = pg.splitlines()
for i in range(155, 285):
    print(f"{i+1}: {lines[i]}")
