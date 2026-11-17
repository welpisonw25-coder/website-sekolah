# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

track_start = h.find('id="showcaseSliderTrack"')
dots_end = h.find('id="showcaseDotsBar"')
slider_content = h[track_start:dots_end+600]
print('Gapura in index.html slider_content:', 'gapura-kehormatan.jpg' in slider_content)
print('Starlink in index.html slider_content:', 'kegiatan-anbk-komputer.jpg' in slider_content)

with open('js/main.js', 'r', encoding='utf-8') as f:
    m = f.read()
print('Gapura _baseSlide0Html in main.js:', '_baseSlide0Html' in m)
print('renderShowcaseSlides in main.js:', 'function renderShowcaseSlides' in m)
print('initFeaturedShowcaseSlider in main.js:', 'function initFeaturedShowcaseSlider' in m)
