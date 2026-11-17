# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

# Let's inspect sidebar where items are listed
sidebar_idx = admin_html.find('class="admin-sidebar">')
print(admin_html[sidebar_idx:sidebar_idx+1500])
