import json, urllib.request

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

url = "https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json"
req_data = json.dumps(data).encode('utf-8')
req = urllib.request.Request(url, data=req_data, headers={'Content-Type': 'application/json'}, method='PUT')

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print("Firebase sync response status:", resp.status)
        print("SUCCESS! data_sekolah.json synchronized to Google Cloud Firebase!")
except Exception as e:
    print("Firebase sync error:", e)
