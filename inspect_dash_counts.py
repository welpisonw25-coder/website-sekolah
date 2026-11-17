# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

import re
matches = re.findall(r'dashCount[a-zA-Z0-9_]+', admin_txt)
print("Unique dashCount elements in admin.js:", set(matches))

for m in set(matches):
    idx = admin_txt.find(m)
    print(f"--- {m} ---")
    print(admin_txt[idx-30:idx+120])
