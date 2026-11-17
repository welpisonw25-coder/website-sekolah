# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

with open('js/main.js', 'r', encoding='utf-8') as f:
    main_txt = f.read()

print("Does admin.js check 'draft'?:", 'draft' in admin_txt)
print("Does main.js filter 'published'?:", 'published' in main_txt)

# check how ppdb is handled in admin.js
idx = admin_txt.find('ppdb')
print("PPDB in admin.js:", idx != -1)
if idx != -1:
    print(admin_txt[idx:idx+400])
