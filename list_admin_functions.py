# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

import re
fns = re.findall(r'(?:function\s+([a-zA-Z0-9_]+)\s*\(|window\.([a-zA-Z0-9_]+)\s*=)', admin_txt)
fn_names = [f[0] or f[1] for f in fns]
print("Total functions/window properties in admin.js:", len(fn_names))
print("Sample functions:")
for name in fn_names:
    print(" -", name)
