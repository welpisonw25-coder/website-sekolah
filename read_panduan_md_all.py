path = r'C:\Users\acer\.gemini\antigravity\brain\dd0dfa00-a14b-4840-8d1f-b223e643fa0a\PANDUAN_SERAH_TERIMA_SEKOLAH.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(min(50, len(lines))):
    print(f"{i+1}: {lines[i]}", end="")
