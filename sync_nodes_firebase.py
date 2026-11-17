import json, requests

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Sync profil node
url_profil = "https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/profil.json"
resp1 = requests.put(url_profil, json=data['profil'], timeout=30)
print("Profil sync status:", resp1.status_code)

# Sync admin_users node
url_users = "https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/admin_users.json"
resp2 = requests.put(url_users, json=data['admin_users'], timeout=30)
print("Admin users sync status:", resp2.status_code)
