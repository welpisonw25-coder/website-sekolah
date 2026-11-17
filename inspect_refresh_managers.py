# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

idx = admin_txt.find('function refreshAdminManagers()')
print(admin_txt[idx:idx+1200])
