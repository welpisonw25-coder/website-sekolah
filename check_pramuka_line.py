with open('sop.html', 'r', encoding='utf-8') as f:
    sop = f.read()

lines = sop.splitlines()
for i, l in enumerate(lines):
    if 'POIN 7: EKSTRAKURIKULER PRAMUKA' in l:
        for j in range(i, min(i+20, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
