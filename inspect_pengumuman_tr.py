# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('function renderTable()', txt.find('function initPengumumanManager()'))
idx_tr = txt.find('tr.innerHTML =', idx)
print(txt[idx_tr:idx_tr+1200])
