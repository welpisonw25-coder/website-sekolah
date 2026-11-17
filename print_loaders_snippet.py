# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    txt = f.read()

idx_ann = txt.find('function loadDynamicAnnouncements()')
print("loadDynamicAnnouncements:")
print(txt[idx_ann:idx_ann+500])

idx_gal = txt.find('function loadDynamicGallery()')
print("\nloadDynamicGallery:")
print(txt[idx_gal:idx_gal+500])
