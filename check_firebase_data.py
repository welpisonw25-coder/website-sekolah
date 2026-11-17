import requests

cloudUrl = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json'
r = requests.get(cloudUrl, timeout=10)
print("status:", r.status_code)
d = r.json()
print("keys:", list(d.keys()))
berita = d.get('berita', [])
print("total berita in firebase:", len(berita))
for b in berita[:3]:
    print(f"- {b.get('judul')} (foto length: {len(b.get('foto', ''))})")
