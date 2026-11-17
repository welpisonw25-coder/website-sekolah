import requests
import json

# Check Firebase data_sekolah.json
r = requests.get('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json', timeout=10)
data = r.json()
print("Firebase berita count:", len(data.get('berita', [])))
for b in data.get('berita', []):
    print(f"ID {b.get('id')}: {b.get('judul')} ({b.get('tanggal')})")
