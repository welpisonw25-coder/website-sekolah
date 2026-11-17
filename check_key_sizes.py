import requests
import json

r = requests.get('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json', timeout=10)
db = r.json()
for k in db:
    s = json.dumps(db[k])
    print(f"Key {k}: {len(s):,} bytes ({len(s)/1024:.1f} KB)")
