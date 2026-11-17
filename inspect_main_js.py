with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

lines_main = main_js.splitlines()
print(f"Total lines in js/main.js: {len(lines_main)}")

for i, l in enumerate(lines_main):
    if 'kkg' in l.lower() or 'sop' in l.lower() or 'piket' in l.lower() or 'seragam' in l.lower():
        print(f"Line {i+1}: {l.strip()[:100]}")
