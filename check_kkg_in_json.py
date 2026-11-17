import json

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

kkg = d.get('kkg', {})
print("Type of kkg:", type(kkg))
if isinstance(kkg, dict):
    print("Keys in kkg:", list(kkg.keys()))
    if 'gusek_info' in kkg:
        print("gusek_info:", kkg['gusek_info'])
    if 'jadwal_pertemuan' in kkg:
        print("jadwal_pertemuan count:", len(kkg['jadwal_pertemuan']))
