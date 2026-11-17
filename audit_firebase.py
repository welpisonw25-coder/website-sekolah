# -*- coding: utf-8 -*-
import re

with open('js/main.js', 'r', encoding='utf-8') as f:
    main_txt = f.read()

with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_txt = f.read()

firebase_urls_main = re.findall(r'https://[a-zA-Z0-9\-\.]*firebaseio\.com[^\s\'\"\`]*', main_txt)
firebase_urls_admin = re.findall(r'https://[a-zA-Z0-9\-\.]*firebaseio\.com[^\s\'\"\`]*', admin_txt)

print('Firebase URLs in main.js:')
for u in sorted(set(firebase_urls_main)):
    print(' -', u)

print('\nFirebase URLs in admin.js:')
for u in sorted(set(firebase_urls_admin)):
    print(' -', u)
