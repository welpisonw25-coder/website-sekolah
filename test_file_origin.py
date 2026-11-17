import requests

res = requests.options('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/berita.json', headers={
    'Origin': 'null',
    'Access-Control-Request-Method': 'PUT',
    'Access-Control-Request-Headers': 'content-type'
})
print("OPTIONS with Origin: null -> status:", res.status_code)
print("Access-Control-Allow-Origin:", res.headers.get('Access-Control-Allow-Origin'))
