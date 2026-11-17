with open('js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'kkgDokumentasiGrid', text)]
print('Matches in js/main.js:', len(matches))
for idx in matches:
    print(text[max(0, idx-50):min(len(text), idx+1000)].replace('\n', ' '))
    print("=" * 50)
