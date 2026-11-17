with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    text = f.read()

p = text.find('id="kkgDokumentasiGrid"')
if p != -1:
    print(text[p-200:p+300])
else:
    print("kkgDokumentasiGrid not found")
