path = r'C:\Users\acer\.gemini\antigravity\brain\dd0dfa00-a14b-4840-8d1f-b223e643fa0a\PANDUAN_SERAH_TERIMA_SEKOLAH.md'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

lines = c.splitlines()
print(f"Total lines in md artifact: {len(lines)}")
for i, l in enumerate(lines):
    if 'fitur di panel admin' in l.lower() or '| sambutan' in l.lower():
        for j in range(max(0, i-5), min(i+40, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
