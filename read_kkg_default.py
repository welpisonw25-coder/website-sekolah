with open('js/admin.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(3810, 3870):
    print(f"{i+1}: {lines[i]}", end="")
