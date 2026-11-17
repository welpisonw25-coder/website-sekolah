# -*- coding: utf-8 -*-
with open('kontak.html', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('Hubungi Kami')
print(txt[idx-50:idx+1500])
