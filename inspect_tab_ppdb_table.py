# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

idx = admin_html.find('ppdbTableBody')
print(admin_html[idx-400:idx+800])
