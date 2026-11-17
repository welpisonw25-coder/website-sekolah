# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

sidebar_start = admin_html.find('data-tab="tab-sop"')
print(admin_html[sidebar_start:sidebar_start+800])
