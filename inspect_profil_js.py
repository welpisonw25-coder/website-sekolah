with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

import re

for fn in ['saveProfilData', 'initProfilManager', 'loadProfilData', 'getProfilData']:
    matches = [m.start() for m in re.finditer(fn, admin_js)]
    print(f"=== Function {fn}: {len(matches)} occurrences ===")
    for idx in matches:
        print(admin_js[max(0, idx-100):min(len(admin_js), idx+600)])
        print("-" * 50)
