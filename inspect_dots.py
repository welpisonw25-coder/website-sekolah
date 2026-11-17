# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    txt = f.read()

start_marker = 'id="showcaseDotsBar"'
start = txt.find(start_marker)
print(txt[start:start+600])
