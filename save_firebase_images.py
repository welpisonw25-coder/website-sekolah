# -*- coding: utf-8 -*-
import urllib.request
import json
import base64
import os

url = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/berita.json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    berita_list = json.loads(resp.read().decode('utf-8'))

file_map = {
    2: 'images/kegiatan-anbk-komputer.jpg',
    3: 'images/kegiatan-senam-bersama.jpg',
    4: 'images/kegiatan-keagamaan-rohani.jpg',
    5: 'images/kegiatan-rapat-dewan-guru.jpg',
    6: 'images/kegiatan-pramuka-budaya.jpg'
}

for item in berita_list:
    item_id = item.get('id')
    foto = item.get('foto', '')
    if foto.startswith('data:image'):
        # extract base64
        header, encoded = foto.split(',', 1)
        data = base64.b64decode(encoded)
        dest = file_map.get(item_id)
        if dest:
            with open(dest, 'wb') as f:
                f.write(data)
            print(f"Saved {dest} ({len(data)} bytes)")

print("Done saving images from Firebase!")
