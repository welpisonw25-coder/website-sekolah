c = open('guru.html', encoding='utf-8').read()
pos = c.find('bagan-struktur-organisasi.svg')
print(c[pos-1500:pos])
