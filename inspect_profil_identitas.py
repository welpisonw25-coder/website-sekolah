# -*- coding: utf-8 -*-
with open('profil.html', 'r', encoding='utf-8') as f:
    txt = f.read()

idx_main = txt.find('Identitas Satuan Pendidikan')
if idx_main == -1: idx_main = txt.find('NPSN')
print(txt[idx_main-100:idx_main+2000])
