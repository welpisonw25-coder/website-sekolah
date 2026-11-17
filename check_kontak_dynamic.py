# -*- coding: utf-8 -*-
with open('kontak.html', 'r', encoding='utf-8') as f:
    kontak_html = f.read()

import re
ids = re.findall(r'id=["\']([^"\']+)["\']', kontak_html)
print("IDs in kontak.html:", ids)

with open('js/main.js', 'r', encoding='utf-8') as f:
    main_txt = f.read()

print("Is there loadDynamicKontak in main.js?:", 'loadDynamicKontak' in main_txt)
print("Is there kontak in SDN_DATABASE?:", 'db.kontak' in main_txt)
