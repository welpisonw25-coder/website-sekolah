# -*- coding: utf-8 -*-
with open('profil.html', 'r', encoding='utf-8') as f:
    txt = f.read()

idx_main = txt.find('<!-- MISI SEKOLAH -->')
print(txt[idx_main:idx_main+2500])
