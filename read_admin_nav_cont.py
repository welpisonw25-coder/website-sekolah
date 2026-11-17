with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(160, 185):
    print(f"{i+1}: {lines[i]}", end="")
