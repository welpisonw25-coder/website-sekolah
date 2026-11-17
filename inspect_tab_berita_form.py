# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    txt = f.read()

idx_fb = txt.find('id="tab-berita"')
print("tab-berita form:")
print(txt[idx_fb:idx_fb+1500])
