# -*- coding: utf-8 -*-
with open('login.html', 'r', encoding='utf-8') as f:
    login_html = f.read()

import re
scripts = re.findall(r'<script[\s\S]*?</script>', login_html)
if scripts:
    print(scripts[0])
