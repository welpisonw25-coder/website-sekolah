with open('server_otomatis.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'/api/sync_data|category', text)]
print('Matches in server_otomatis.py:', len(matches))
for idx in matches[:5]:
    print(text[max(0, idx-30):min(len(text), idx+150)].replace('\n', ' '))
