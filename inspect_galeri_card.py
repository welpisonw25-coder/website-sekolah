# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('function renderGaleriList()')
idx_card = txt.find('card.innerHTML =', idx)
print(txt[idx_card:idx_card+1200])
