import requests

urls = [
    'https://sdninpresarso8.sch.id/',
    'https://sdninpresarso8.sch.id/admin.html',
    'https://sdninpresarso8.sch.id/sop.html',
    'https://sdninpresarso8.sch.id/guru.html',
    'https://sdninpresarso8.sch.id/pengembangan-guru.html',
    'https://sdninpresarso8.sch.id/data_sekolah.json'
]

for u in urls:
    try:
        r = requests.get(u, timeout=10)
        print(f"{u} -> Status {r.status_code}, Length {len(r.content)}")
    except Exception as e:
        print(f"{u} -> Error: {e}")
