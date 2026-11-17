import json

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("Local data_sekolah.json berita count:", len(d.get('berita', [])))
for b in d.get('berita', []):
    print(f"ID {b.get('id')}: {b.get('judul')} ({b.get('tanggal')})")
