# -*- coding: utf-8 -*-
with open('profil.html', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('<table')
while idx != -1:
    print("Found table at:", idx)
    print(txt[idx:idx+500])
    idx = txt.find('<table', idx + 1)
