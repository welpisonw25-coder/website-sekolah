import requests

res = requests.options('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/berita.json', headers={
    'Origin': 'https://sdninpresarso8.sch.id',
    'Access-Control-Request-Method': 'PUT',
    'Access-Control-Request-Headers': 'content-type'
})
print("OPTIONS status:", res.status_code)
for k, v in res.headers.items():
    print(f"{k}: {v}")
