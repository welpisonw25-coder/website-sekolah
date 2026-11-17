with open('sop.html', 'r', encoding='utf-8') as f:
    sop = f.read()

with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    pg = f.read()

# Let's inspect sop sections
print("--- SOP.HTML SECTIONS ---")
lines_sop = sop.splitlines()
for i, l in enumerate(lines_sop):
    if 'POIN 1:' in l or 'POIN 2:' in l or 'POIN 3:' in l or 'POIN 5:' in l or 'POIN 6:' in l or 'POIN 7:' in l:
        print(f"Line {i+1}: {l}")

print("\n--- PENGEMBANGAN-GURU.HTML SECTIONS ---")
lines_pg = pg.splitlines()
for i, l in enumerate(lines_pg):
    if 'IDENTITAS GUGUS' in l or 'BAGIAN 1: K3S' in l or 'KELOMPOK A' in l or 'KELOMPOK B' in l or 'BAGIAN 3:' in l:
        print(f"Line {i+1}: {l}")
