with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== TAB KKG (lines 1320 to 1420) ===")
for i in range(1320, min(1420, len(lines))):
    print(f"{i+1}: {lines[i]}", end="")

print("\n=== TAB SOP (lines 1555 to 1620) ===")
for i in range(1555, min(1630, len(lines))):
    print(f"{i+1}: {lines[i]}", end="")
