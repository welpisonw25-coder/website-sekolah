with open('guru.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(688, 850):
    print(f"{i+1}: {lines[i]}", end="")
