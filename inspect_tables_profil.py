with open('profil.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<table', text)]
print('Tables in profil.html:', len(matches))
for idx in matches:
    print(text[idx:idx+1500])
    print("=" * 50)
