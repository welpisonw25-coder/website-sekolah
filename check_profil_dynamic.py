# -*- coding: utf-8 -*-
with open('profil.html', 'r', encoding='utf-8') as f:
    profil_html = f.read()

import re
# check what IDs exist in profil.html
ids = re.findall(r'id=["\']([^"\']+)["\']', profil_html)
print("IDs in profil.html:", ids)

# check if there's any dynamic loader for profil in main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_txt = f.read()

print("Is there loadDynamicProfil in main.js?:", 'loadDynamicProfil' in main_txt)
print("Is there profil in SDN_DATABASE?:", 'db.profil' in main_txt)
