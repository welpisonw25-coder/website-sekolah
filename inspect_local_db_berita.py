# -*- coding: utf-8 -*-
import json
with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

berita = db.get('berita', [])
print('Total berita in local data_sekolah.json:', len(berita))
for b in berita:
    foto = b.get('foto', '')
    print(b.get('id'), b.get('judul'), 'foto_len:', len(foto), foto[:40])
