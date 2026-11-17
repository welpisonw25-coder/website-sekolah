import glob
import re

html_files = glob.glob('*.html')
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        c = f.read()
    logos = re.findall(r'<link[^>]*rel=[\'"][^\'"]*icon[^\'"]*[\'"][^>]*href=[\'"]([^\'"]+)[\'"]', c)
    if logos:
        print(f"{hf} favicon: {logos}")
    img_logos = re.findall(r'<img[^>]*src=[\'"]([^\'"]*(?:logo|icon|tutwuri)[^\'"]*)[\'"]', c, re.I)
    if img_logos:
        print(f"{hf} img logos: {set(img_logos)}")
