with open('admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- HEADER TOP BAR (lines 85-118) ---")
for j in range(84, 118):
    print(f"{j+1}: {lines[j]}", end="")

print("\n--- MARQUEE BOX IN TAB-PROFIL (lines 490-510) ---")
for j in range(490, 510):
    print(f"{j+1}: {lines[j]}", end="")

print("\n--- MULTI-USER TABLE IN TAB-PENGATURAN (lines 2370-2410) ---")
for j in range(2370, 2410):
    print(f"{j+1}: {lines[j]}", end="")
