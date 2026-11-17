with open('galeri.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('gallery-grid')
if pos != -1:
    print(text[pos-250:pos+800])
else:
    print("gallery-grid not found")
