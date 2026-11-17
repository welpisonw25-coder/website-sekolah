# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

print("admin.js tail:")
print(admin_txt[-1500:])
