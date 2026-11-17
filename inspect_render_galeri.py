# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('function renderGaleriList()')
if idx == -1: idx = txt.find('renderGaleri')
print(txt[idx:idx+1200])
