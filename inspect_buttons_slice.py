# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    txt = f.read()

idx_b = txt.find('btn-edit-berita')
print("btn-edit-berita slice:")
print(txt[idx_b-100:idx_b+400])

idx_p = txt.find('btn-edit-pengumuman')
print("\nbtn-edit-pengumuman slice:")
print(txt[idx_p-100:idx_p+400])
