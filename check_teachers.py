import json

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

guru = d.get('guru', [])
print(f"Total guru: {len(guru)}")
for g in guru:
    print(f"- {g.get('nama')} ({g.get('jabatan')})")
