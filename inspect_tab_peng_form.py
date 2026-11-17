# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    txt = f.read()

idx_p = txt.find('id="tab-pengumuman"')
print("tab-pengumuman form:")
print(txt[idx_p:idx_p+1500])
