import requests

check_urls = [
    'https://sdninpresarso8.sch.id/images/logo-keerom.png',
    'https://sdninpresarso8.sch.id/favicon.ico',
    'https://sdninpresarso8.sch.id/images/dewan-guru.jpg',
    'https://sdninpresarso8.sch.id/images/gapura-kehormatan.jpg',
    'https://sdninpresarso8.sch.id/images/kepala-sekolah.jpg'
]

for u in check_urls:
    try:
        r = requests.get(u, timeout=10)
        print(f"{u} -> Status: {r.status_code}, Length: {len(r.content)}, Content-Type: {r.headers.get('content-type')}")
    except Exception as e:
        print(f"{u} -> Error: {e}")
