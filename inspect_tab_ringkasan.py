# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

idx = admin_html.find('id="tab-ringkasan"')
end = admin_html.find('id="tab-sambutan"')
print(admin_html[idx:idx+2500])
