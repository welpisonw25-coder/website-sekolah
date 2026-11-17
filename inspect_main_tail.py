# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    txt = f.read()

print("Tail of js/main.js:")
print(txt[-1200:])
