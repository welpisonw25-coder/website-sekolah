# -*- coding: utf-8 -*-
import re

with open('admin.html', 'r', encoding='utf-8') as f:
    txt = f.read()

tabs = re.findall(r'data-tab=["\']([^"\']+)["\']', txt)
print('Tabs found in admin.html:', set(tabs))

sections = re.findall(r'<section[^>]+id=["\']tab-([^"\']+)["\']', txt)
print('Section tabs found in admin.html:', sections)

nav_links = re.findall(r'<a[^>]+class=["\'][^"\']*nav-item[^"\']*["\'][^>]*>(.*?)</a>', txt, re.DOTALL)
if not nav_links:
    nav_links = re.findall(r'<a[^>]+data-tab[^>]*>(.*?)</a>', txt, re.DOTALL)
print('Nav links count:', len(nav_links))
for nl in nav_links:
    clean = re.sub(r'<[^>]+>', '', nl).strip()
    clean = ' '.join(clean.split())
    print(' -', clean)
