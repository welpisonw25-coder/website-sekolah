# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    txt = f.read()

idx = txt.find('Kategori Berita:')
print("Kategori Berita in admin.html:")
print(txt[idx-100:idx+300])

idx_p = txt.find('Kategori Pengumuman:')
print("\nKategori Pengumuman in admin.html:")
print(txt[idx_p-100:idx_p+300])
