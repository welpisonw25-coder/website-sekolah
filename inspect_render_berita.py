# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

idx_rb = admin_txt.find('function renderBerita()')
print("renderBerita slice:")
print(admin_txt[idx_rb:idx_rb+1200])
