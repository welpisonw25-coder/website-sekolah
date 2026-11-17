with open('js/admin.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'KELOLA PENGGUNA|getUserData|renderUserTable', text)]
print('Matches:', len(matches))
for idx in matches[:5]:
    print(text[max(0, idx-50):min(len(text), idx+100)].replace('\n', ' '))
