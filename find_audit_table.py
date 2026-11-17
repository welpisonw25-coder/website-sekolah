with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'riwayat aktivitas|audit', text, re.IGNORECASE)]
print("Matches in admin.html:", len(matches))
for idx in matches:
    print(text[max(0, idx-50):min(len(text), idx+500)])
    print("=" * 50)
