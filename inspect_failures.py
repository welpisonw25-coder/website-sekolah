# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    txt = f.read()
print('beritaStatus in admin.html:', 'beritaStatus' in txt)
print('pengumumanStatus in admin.html:', 'pengumumanStatus' in txt)

with open('js/main.js', 'r', encoding='utf-8') as f:
    mtxt = f.read()
print('loadDynamicProfil in main.js:', 'loadDynamicProfil' in mtxt)
print('function loadDynamicProfil in main.js:', 'function loadDynamicProfil' in mtxt)
