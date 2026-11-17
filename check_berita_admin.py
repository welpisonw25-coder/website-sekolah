with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

lines = admin_js.splitlines()
for i, l in enumerate(lines):
    if 'function initberitamanager' in l.lower():
        for j in range(i, min(i+60, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
