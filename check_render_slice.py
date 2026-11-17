# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    txt = f.read()

start_fn = 'function renderShowcaseSlides(newsData)'
start = txt.find(start_fn)
end_fn = '/* -------------------------------------------------------------------\n   10B. SINKRONISASI SAMBUTAN KEPALA SEKOLAH'
end = txt.find(end_fn, start)

print('renderShowcaseSlides range:', start, end)
print(txt[start:start+400])
