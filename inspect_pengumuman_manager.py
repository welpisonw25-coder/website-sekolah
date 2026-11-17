# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('function renderPengumuman()')
if idx == -1: idx = txt.find('initPengumumanManager')
print(txt[idx:idx+1200])
