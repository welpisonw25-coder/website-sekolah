with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'showcase-slider-wrapper', text)]
print('Matches in index.html:', len(matches))
for idx in matches:
    print(text[max(0, idx-100):min(len(text), idx+1500)])
