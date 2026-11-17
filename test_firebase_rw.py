import requests

test_url = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/test_sync.json'
try:
    r = requests.put(test_url, json={"test": "hello", "time": "2026-11-15"}, timeout=10)
    print("PUT test_sync status:", r.status_code, r.text)
except Exception as e:
    print("PUT test_sync error:", e)

# Also check GET
try:
    r_get = requests.get('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/berita.json', timeout=10)
    print("GET berita status:", r_get.status_code, "items count:", len(r_get.json()) if r_get.status_code == 200 and r_get.json() else 0)
except Exception as e:
    print("GET berita error:", e)
