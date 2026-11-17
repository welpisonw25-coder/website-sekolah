# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('window.refreshDataFromCloud')
print(txt[idx:idx+1200])
