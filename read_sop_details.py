with open('sop.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

def print_range(start, end, title):
    print(f"=== {title} (lines {start} to {end}) ===")
    for i in range(start-1, min(end, len(lines))):
        print(f"{i+1}: {lines[i]}", end="")

print_range(400, 470, "POIN 1 & 2 (Tata Tertib Guru & Siswa)")
print_range(473, 575, "POIN 3 & 4 (Seragam Guru & Siswa)")
print_range(576, 632, "POIN 5 (Jadwal Piket Guru)")
print_range(648, 715, "POIN 7 (Pramuka Siaga & Penggalang)")
