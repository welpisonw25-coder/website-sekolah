with open('berita.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('news-grid')
if pos != -1:
    print(text[pos-250:pos+800])
else:
    print("news-grid not found")
