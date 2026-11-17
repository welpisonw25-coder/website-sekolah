with open('js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1430, 1520):
    print(f"{i+1}: {lines[i]}", end="")
