with open('berita.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(150, 230):
    print(f"{i+1}: {lines[i]}", end="")
