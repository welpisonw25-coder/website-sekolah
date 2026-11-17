with open('guru.html', 'r', encoding='utf-8') as f:
    guru = f.read()

lines = guru.splitlines()
for i in range(744, 840):
    print(f"{i+1}: {lines[i]}")
