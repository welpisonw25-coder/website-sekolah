# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

sidebar_start = admin_html.find('class="admin-sidebar">')
sidebar_end = admin_html.find('</aside>', sidebar_start)
if sidebar_end == -1:
    sidebar_end = admin_html.find('</div>', sidebar_start + 1500)

print(admin_html[sidebar_start:sidebar_start+2500])
