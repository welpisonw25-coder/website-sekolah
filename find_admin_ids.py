with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
tbodies = re.findall(r'<tbody[^>]*id=[\"\']([^\"\']+)[\"\']', text)
print("All tbody IDs in admin.html:", tbodies)

# Also check for galeri list container
gal_matches = re.findall(r'id=[\"\']([^\"\']*gal[^\"]*)[\"\']', text, re.IGNORECASE)
print("Galeri IDs in admin.html:", gal_matches)

# Also check for berita IDs
berita_matches = re.findall(r'id=[\"\']([^\"\']*berita[^\"]*)[\"\']', text, re.IGNORECASE)
print("Berita IDs in admin.html:", berita_matches)

# Also check for pengumuman IDs
peng_matches = re.findall(r'id=[\"\']([^\"\']*pengumuman[^\"]*)[\"\']', text, re.IGNORECASE)
print("Pengumuman IDs in admin.html:", peng_matches)

# Also check for sarpras IDs
sar_matches = re.findall(r'id=[\"\']([^\"\']*sarpras[^\"]*)[\"\']', text, re.IGNORECASE)
print("Sarpras IDs in admin.html:", sar_matches)
