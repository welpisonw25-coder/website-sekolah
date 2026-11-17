with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

print('admin.html length:', len(admin_html))

keywords = ['keluar', 'logout', 'profil', 'akun', 'operator', 'kepala sekolah', 'pengumuman berjalan', 'ticker', 'pengumuman_berjalan', 'running']
for k in keywords:
    print(f'Count of "{k}": {admin_html.lower().count(k)}')

with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

print('\njs/admin.js length:', len(admin_js))
for k in keywords:
    print(f'js/admin.js count of "{k}": {admin_js.lower().count(k)}')
