import glob
import re

html_files = glob.glob('*.html')
count_bumped = 0

old_ver = 'v=20261115_v33'
new_ver = 'v=20261115_v34'

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_ver in content:
        content = content.replace(old_ver, new_ver)
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(content)
        count_bumped += 1
        print(f"Bumped cache version in {hf}")

print(f"Total files bumped to {new_ver}: {count_bumped}")
