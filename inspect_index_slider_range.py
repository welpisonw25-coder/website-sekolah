# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

track_start = html.find('<div class="showcase-slider-track" id="showcaseSliderTrack">')
section_end = html.find('</section>', track_start)
assert track_start != -1 and section_end != -1, "track section not found"

print("track_start:", track_start)
print("section_end:", section_end)
print(html[track_start:track_start+200])
print("... TAIL ...")
print(html[section_end-300:section_end])
