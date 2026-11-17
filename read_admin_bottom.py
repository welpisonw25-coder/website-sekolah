with open('js/admin.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for i in range(max(0, len(lines)-60), len(lines)):
    print(f"{i+1}: {lines[i]}", end="")
