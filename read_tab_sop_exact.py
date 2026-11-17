with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1555, 1608):
    print(f"{i+1}: {lines[i]}", end="")
