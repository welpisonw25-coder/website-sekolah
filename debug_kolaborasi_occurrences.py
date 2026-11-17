with open('kolaborasi.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'kolaborasiListContainer', text)]
print('kolaborasiListContainer occurrences:', len(matches))

matches_slider = [m.start() for m in re.finditer(r'mitraSliderWrapper', text)]
print('mitraSliderWrapper occurrences:', len(matches_slider))

matches_slide = [m.start() for m in re.finditer(r'class="mitra-slide', text)]
print('mitra-slide occurrences:', len(matches_slide))

for i, p in enumerate(matches_slide):
    print(f"Slide {i+1} at pos {p}: {text[p:p+60]}")
