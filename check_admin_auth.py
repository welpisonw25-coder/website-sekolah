# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

idx = admin_html.find('sdn_admin_logged')
while idx != -1:
    print('Found sdn_admin_logged in admin.html at:', idx)
    print(admin_html[max(0, idx-50):idx+200])
    idx = admin_html.find('sdn_admin_logged', idx + 1)
