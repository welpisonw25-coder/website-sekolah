with open('scratch/generated_slider.html', 'r', encoding='utf-8') as f:
    slider_html = f.read()

with open('kolaborasi.html', 'r', encoding='utf-8') as f:
    k_html = f.read()

start_marker = '<div id="kolaborasiListContainer"'
# Find where the 6 cards end before </section>
p_start = k_html.find(start_marker)
if p_start == -1:
    raise Exception("Could not find start marker in kolaborasi.html")

p_end = k_html.find('</section>', p_start)
if p_end == -1:
    raise Exception("Could not find end marker in kolaborasi.html")

# Find the last </div> before </section> that closes kolaborasiListContainer
# In our previous inspection, line 467 was </div> followed by </div> (container) followed by </section>
block_to_replace = k_html[p_start:p_end]
# The container closes with </div>\n        </div>
# Let's inspect the last 150 chars of block_to_replace
print("Tail of block to replace:\n", block_to_replace[-150:])

# New replacement:
new_container_html = f'<div id="kolaborasiListContainer">\n{slider_html}\n            </div>\n        </div>\n    '

# Let's replace precisely
k_html_new = k_html[:p_start] + new_container_html + k_html[p_end:]

with open('kolaborasi.html', 'w', encoding='utf-8') as f:
    f.write(k_html_new)

print("Successfully replaced kolaborasiListContainer in kolaborasi.html!")
