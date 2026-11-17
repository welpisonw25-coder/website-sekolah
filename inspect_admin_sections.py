import re

with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

print("=== 1. SEARCH 'keluar' / 'logout' IN ADMIN.HTML ===")
for match in re.finditer(r'(?:keluar|logout)', admin_html, re.IGNORECASE):
    pos = match.start()
    print(admin_html[max(0, pos-200):min(len(admin_html), pos+300)])
    print("-" * 50)

print("\n=== 2. SEARCH 'pengumuman berjalan' IN ADMIN.HTML ===")
for match in re.finditer(r'pengumuman\s+berjalan', admin_html, re.IGNORECASE):
    pos = match.start()
    print(admin_html[max(0, pos-200):min(len(admin_html), pos+400)])
    print("-" * 50)

print("\n=== 3. SEARCH 'profil' SECTIONS IN ADMIN.HTML ===")
for match in re.finditer(r'id=["\'](?:sectionProfil|profil|formProfil)[^"\']*["\']', admin_html, re.IGNORECASE):
    pos = match.start()
    print(admin_html[max(0, pos-100):min(len(admin_html), pos+300)])
    print("-" * 50)

print("\n=== 4. SEARCH ACCOUNT/USER SETTINGS IN ADMIN.HTML ===")
for match in re.finditer(r'id=["\'](?:sectionPengaturan|akun|users|admin_users)[^"\']*["\']', admin_html, re.IGNORECASE):
    pos = match.start()
    print(admin_html[max(0, pos-100):min(len(admin_html), pos+300)])
    print("-" * 50)
