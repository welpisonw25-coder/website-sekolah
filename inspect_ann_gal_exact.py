# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('function loadDynamicAnnouncements()')
print("loadDynamicAnnouncements:")
print(txt[idx+300:idx+800])

idx_gal = txt.find('function loadDynamicGallery()')
print("\nloadDynamicGallery:")
print(txt[idx_gal+300:idx_gal+800])
