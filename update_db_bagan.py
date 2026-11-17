import json

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

if 'bagan_struktur' not in db:
    db['bagan_struktur'] = ''
    with open('data_sekolah.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
    print("Added bagan_struktur to data_sekolah.json successfully!")
else:
    print("bagan_struktur already in data_sekolah.json")
