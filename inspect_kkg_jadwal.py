import json

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

kkg = data.get('kkg', {})
print("KKG keys:", list(kkg.keys()))

jadwal = kkg.get('jadwal_pertemuan', [])
print("Jadwal count:", len(jadwal))
for i, j in enumerate(jadwal, 1):
    print(f"\nItem {i}:")
    print("  Tanggal:", j.get('tanggal'))
    print("  Agenda:", j.get('agenda'))
    print("  Tuan Rumah:", j.get('tuan_rumah'))
    print("  Kelompok:", j.get('kelompok'))
    print("  Foto:", j.get('foto'))
    print("  Status:", j.get('status'))
