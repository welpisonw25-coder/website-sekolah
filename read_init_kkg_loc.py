with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

lines = admin_js.splitlines()
for i, l in enumerate(lines):
    if 'function initkkgmanager' in l.lower():
        print(f"Line {i+1}: {l}")
        for j in range(i, min(i+30, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
