with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    text = f.read()

marker = '📸 Galeri Foto Kegiatan & Pertemuan K3S / KKG'
p = text.find(marker)
if p != -1:
    print("Found marker at pos:", p)
    print(text[p-200:p+2500])
else:
    print("Marker not found!")
