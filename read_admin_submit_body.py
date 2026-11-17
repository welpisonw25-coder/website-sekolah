with open('js/admin.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(930, 985):
    print(f"{i+1}: {lines[i]}", end="")
