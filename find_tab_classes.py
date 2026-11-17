# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

import re
matches = re.findall(r'<div[^>]+id=["\'](tab-[^"\']+)["\']', admin_html)
print("Divs with id tab-*: ", matches)

matches_sec = re.findall(r'<section[^>]+id=["\'](tab-[^"\']+)["\']', admin_html)
print("Sections with id tab-*: ", matches_sec)

# search for tab-ringkasan
idx = admin_html.find('tab-ringkasan')
while idx != -1:
    print("Found tab-ringkasan at:", idx)
    print(admin_html[max(0, idx-50):idx+150])
    idx = admin_html.find('tab-ringkasan', idx + 1)
