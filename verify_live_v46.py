import urllib.request

for path in ['admin.html', 'profil.html', 'kolaborasi.html']:
    url = f'https://sdninpresarso8.sch.id/{path}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        text = resp.read().decode('utf-8')
        has_v46 = 'v=20261115_v46' in text
        print(f"{path}: status {resp.status}, version v46: {has_v46}")
