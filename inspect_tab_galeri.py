# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    txt = f.read()

idx_g = txt.find('id="tab-galeri"')
print("tab-galeri slice:")
print(txt[idx_g:idx_g+1200])
