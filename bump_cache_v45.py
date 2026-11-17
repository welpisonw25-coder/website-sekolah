import glob, re

html_files = glob.glob('*.html')
print(f"Found {len(html_files)} HTML files to update cache version.")

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace v=20261115_v44 with v=20261115_v45
    new_content = re.sub(r'v=20261115_v44', 'v=20261115_v45', content)
    # Also replace any other previous version tags in case some were missed
    new_content = re.sub(r'style\.css\?v=[a-zA-Z0-9_-]+', 'style.css?v=20261115_v45', new_content)
    new_content = re.sub(r'main\.js\?v=[a-zA-Z0-9_-]+', 'main.js?v=20261115_v45', new_content)
    
    if new_content != content:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated cache version in {hf}")
    else:
        print(f"No changes needed in {hf}")

print("Cache busting bump to v=20261115_v45 completed!")
