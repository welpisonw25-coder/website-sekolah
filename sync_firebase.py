import json
import requests

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sop_data = data.get('sop_data', {})
kkg = data.get('kkg', {})

url_sop = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/sop_data.json'
url_kkg = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/kkg.json'

print("Uploading sop_data to Firebase...")
try:
    res_sop = requests.put(url_sop, json=sop_data, timeout=15)
    print(f"sop_data upload status: {res_sop.status_code}")
except Exception as e:
    print(f"sop_data upload error: {e}")

print("Uploading kkg to Firebase...")
try:
    res_kkg = requests.put(url_kkg, json=kkg, timeout=15)
    print(f"kkg upload status: {res_kkg.status_code}")
except Exception as e:
    print(f"kkg upload error: {e}")
