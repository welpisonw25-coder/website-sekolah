import json

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

kkg = d.get('kkg', {})
print("k3s:", json.dumps(kkg.get('k3s', {}), indent=2))
print("kkg_kelompok_a:", json.dumps(kkg.get('kkg_kelompok_a', {}), indent=2))
print("kkg_kelompok_b:", json.dumps(kkg.get('kkg_kelompok_b', {}), indent=2))
