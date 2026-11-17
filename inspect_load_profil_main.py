with open('js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'loadDynamicProfil|sdn_profil_data', text)]
print('loadDynamicProfil matches:', len(matches))
for idx in matches:
    print(text[max(0, idx-50):min(len(text), idx+400)].replace('\n', ' '))
    print("=" * 50)
