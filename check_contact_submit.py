# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_txt = f.read()

idx = main_txt.find('function initContactForm()')
print(main_txt[idx+500:idx+1500])
