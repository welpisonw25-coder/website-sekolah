# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

idx = admin_txt.find('refreshAdminManagers')
while idx != -1:
    print("Found refreshAdminManagers at:", idx)
    print(admin_txt[max(0, idx-50):idx+200])
    idx = admin_txt.find('refreshAdminManagers', idx + 1)
