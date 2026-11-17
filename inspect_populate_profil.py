with open('js/admin.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer('populateProfilForm', text)]
print('populateProfilForm occurrences in js/admin.js:', len(matches))
for idx in matches:
    print(text[max(0, idx-50):min(len(text), idx+150)].replace('\n', ' '))
