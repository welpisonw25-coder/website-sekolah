import requests

res = requests.options('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/berita.json', headers={
    'Origin': 'https://sdninpresarso8.sch.id',
    'Access-Control-Request-Method': 'PUT'
})
print("OPTIONS status:", res.status_code)
print("Access-Control-Allow-Origin:", res.headers.get('Access-Control-Allow-Origin'))
