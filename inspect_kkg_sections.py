with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
sections = re.findall(r'<section[^>]*>.*?</section>', text, re.DOTALL)
print(f"Total sections in pengembangan-guru.html: {len(sections)}")

for i, sec in enumerate(sections, 1):
    h2 = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', sec)
    print(f"\n--- Section {i} (Length: {len(sec)}) ---")
    print("Headings:", [re.sub(r'<[^>]+>', '', h).strip() for h in h2])
    imgs = re.findall(r'<img[^>]+src="([^">]+)"', sec)
    print("Images count:", len(imgs), imgs[:5])
