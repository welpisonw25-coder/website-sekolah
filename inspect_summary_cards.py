# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

idx = admin_txt.find('function updateSummaryCards()')
if idx == -1: idx = admin_txt.find('dashCountBerita')
print(admin_txt[idx-50:idx+800])
