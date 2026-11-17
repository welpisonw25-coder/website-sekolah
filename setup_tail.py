path = r'C:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\scratch\read_panduan_md_tail.py'
with open(path, 'w', encoding='utf-8') as f:
    f.write("""path_md = r'C:\\Users\\acer\\.gemini\\antigravity\\brain\\dd0dfa00-a14b-4840-8d1f-b223e643fa0a\\PANDUAN_SERAH_TERIMA_SEKOLAH.md'
with open(path_md, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(95, len(lines)):
    print(f"{i+1}: {lines[i]}", end="")
""")
