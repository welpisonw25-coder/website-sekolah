# -*- coding: utf-8 -*-
with open('kontak.html', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('Informasi Kantor')
print(txt[idx:idx+1500])
