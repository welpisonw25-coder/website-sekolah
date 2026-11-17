with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(190, 220):
    print(f"{i+1}: {lines[i]}", end="")
