# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    txt = f.read()

start_marker = 'id="showcaseSliderTrack"'
end_marker = '</section>'
start = txt.find(start_marker)
end = txt.find(end_marker, start)
print('Found section:', start, end)
print(txt[start:start+350])
