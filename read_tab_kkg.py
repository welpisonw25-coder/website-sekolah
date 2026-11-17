with open('admin.html', encoding='utf-8') as f:
    text = f.read()

import re
kkg_match = re.search(r'(<div id="tab-kkg"[^>]*>[\s\S]*?)(?=<div id="tab-|<footer|<!-- =+)', text)
if kkg_match:
    lines = kkg_match.group(1).split('\n')
    print("Total lines in tab-kkg:", len(lines))
    for i, l in enumerate(lines[:80], 1):
        print(f"{i}: {l}")
