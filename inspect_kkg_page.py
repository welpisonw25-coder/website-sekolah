with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of pengembangan-guru.html:", len(text))

import re
matches = [m.start() for m in re.finditer(r'galeri|foto|dokumentasi|kegiatan', text, re.IGNORECASE)]
print("Keyword matches in pengembangan-guru.html:", len(matches))
for idx in matches[:10]:
    print(text[max(0, idx-50):min(len(text), idx+150)].replace('\n', ' '))
    print("-" * 50)
