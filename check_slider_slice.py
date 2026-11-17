# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    txt = f.read()

start_fn = 'function initFeaturedShowcaseSlider()'
start = txt.find(start_fn)
end_fn = '/* -------------------------------------------------------------------\n   CEK MANDIRI STATUS KELULUSAN'
end = txt.find(end_fn, start)

print('initFeaturedShowcaseSlider range:', start, end)
print(txt[start:start+300])
print('=== TAIL ===')
print(txt[end-200:end])
