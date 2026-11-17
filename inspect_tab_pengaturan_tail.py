# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

idx = admin_html.find('id="tab-pengaturan"')
end = admin_html.find('</main>', idx)
print("tab-pengaturan length:", end - idx)
print(admin_html[end-600:end])
