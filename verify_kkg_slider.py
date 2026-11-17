import re

with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert 'id="kkgShowcaseSliderWrapper"' in html, "Missing kkgShowcaseSliderWrapper"
assert 'id="kkgShowcasePrevBtn"' in html, "Missing kkgShowcasePrevBtn"
assert 'id="kkgShowcaseNextBtn"' in html, "Missing kkgShowcaseNextBtn"
assert 'id="kkgShowcaseSliderTrack"' in html, "Missing kkgShowcaseSliderTrack"
assert 'id="kkgShowcaseDotsBar"' in html, "Missing kkgShowcaseDotsBar"

# Find slides within kkgShowcaseSliderWrapper
track_start = html.find('id="kkgShowcaseSliderTrack"')
track_end = html.find('id="kkgShowcaseDotsBar"')
track_html = html[track_start:track_end]

slides = re.findall(r'class="showcase-slide(?:\s|")[^"]*"', track_html)
print(f"KKG Showcase Slides count: {len(slides)}")
assert len(slides) == 7, f"Expected 7 slides, found {len(slides)}"

dots = re.findall(r'class="showcase-dot(?:\s|")[^"]*"', html[track_end:track_end+600])
print(f"KKG Showcase Dots count: {len(dots)}")
assert len(dots) == 7, f"Expected 7 dots, found {len(dots)}"

with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

assert 'function initKKGShowcaseSlider()' in js, "Missing initKKGShowcaseSlider in js"
assert 'initKKGShowcaseSlider();' in js, "Missing call to initKKGShowcaseSlider in DOMContentLoaded"

print("ALL KKG SHOWCASE SLIDER INTEGRITY CHECKS PASSED 100% PERFECTLY!")
