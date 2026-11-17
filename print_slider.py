# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function initFeaturedShowcaseSlider()')
idx2 = text.find('function initHeroInteractions()', idx)
print(repr(text[idx:idx2]))
