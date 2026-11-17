# -*- coding: utf-8 -*-
with open('login.html', 'r', encoding='utf-8') as f:
    login_html = f.read()

print("Login HTML length:", len(login_html))

# search for script tags or form submit handlers in login.html
import re
scripts = re.findall(r'<script[\s\S]*?</script>', login_html)
print(f"Total script tags in login.html: {len(scripts)}")
for i, s in enumerate(scripts):
    print(f"--- Script {i} ---")
    print(s[:500])
