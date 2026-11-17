# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_txt = f.read()

idx = main_txt.find('contactForm')
print("contactForm in main.js:", idx != -1)
if idx != -1:
    print(main_txt[idx-50:idx+800])
