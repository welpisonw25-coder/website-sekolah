with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

lines = main_js.splitlines()
for i, l in enumerate(lines):
    if 'function initfeaturedshowcaseslider' in l.lower():
        for j in range(i, min(i+40, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
