# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

# search for save functions, syncFirebase, PUT, POST
import re
functions = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', admin_txt)
print("Total functions in admin.js:", len(functions))

sync_matches = [f for f in functions if 'sync' in f.lower() or 'save' in f.lower() or 'publish' in f.lower() or 'cloud' in f.lower()]
print("Sync / Save / Cloud functions:", sync_matches)

# Search for fetch calls in admin.js
fetch_blocks = re.findall(r'fetch\([^\)]*\)', admin_txt)
print("\nTotal fetch() calls in admin.js:", len(fetch_blocks))
for fb in fetch_blocks[:5]:
    print(" -", fb)
