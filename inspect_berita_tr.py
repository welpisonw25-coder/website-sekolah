# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

idx_rb = admin_txt.find('function renderBerita()')
idx_tr = admin_txt.find('tr.innerHTML =', idx_rb)
print(admin_txt[idx_tr-50:idx_tr+800])
