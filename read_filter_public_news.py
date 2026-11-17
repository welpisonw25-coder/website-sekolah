with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

lines = main_js.splitlines()
for i, l in enumerate(lines):
    if 'filterpublicnews' in l.lower():
        for j in range(max(0, i-5), min(i+60, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
