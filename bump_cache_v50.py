import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
old_version_pattern = re.compile(r'v=20261115_v\d+')
new_version = 'v=20261115_v50'

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    if old_version_pattern.search(content):
        updated = old_version_pattern.sub(new_version, content)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(updated)

print(f"Bumped cache to {new_version}")
