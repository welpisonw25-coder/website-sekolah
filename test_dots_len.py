import re

with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    html = f.read()

track_start = html.find('id="kkgShowcaseSliderTrack"')
track_end = html.find('id="kkgShowcaseDotsBar"')
track_html = html[track_start:track_end]

slides = re.findall(r'class="showcase-slide(?:\s|")[^"]*"', track_html)
print(f"KKG Showcase Slides count: {len(slides)}")

dots = re.findall(r'class="showcase-dot(?:\s|")[^"]*"', html[track_end:track_end+1200])
print(f"KKG Showcase Dots count: {len(dots)}")
assert len(dots) == 7, f"Expected 7 dots, found {len(dots)}"

print("ALL CHECKS PASSED!")
