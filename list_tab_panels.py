# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

import re
panels = re.findall(r'<div[^>]+class=["\'][^"\']*admin-tab-panel[^"\']*["\'][^>]*id=["\']([^"\']+)["\']', admin_html)
print("Tab panels in admin.html:", panels)
