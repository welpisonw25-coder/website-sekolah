with open('css/style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'\.showcase-slider-wrapper', text)]
print("Showcase slider matches in css/style.css:", len(matches))
for idx in matches:
    print(text[idx:idx+800])
    print("=" * 50)
