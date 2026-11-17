with open('js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1353, 1420):
    print(f"{i+1}: {lines[i]}", end="")
