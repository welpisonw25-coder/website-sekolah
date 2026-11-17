with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

lines = main_js.splitlines()
for i, l in enumerate(lines):
    if 'function loaddynamic' in l.lower():
        print(f"Line {i+1}: {l}")
        for j in range(i+1, min(i+25, len(lines))):
            if 'function ' in lines[j]:
                break
            print(f"  {lines[j].strip()}")
