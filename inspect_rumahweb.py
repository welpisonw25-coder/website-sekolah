with open('PANDUAN_SERAH_TERIMA_SEKOLAH.md', 'r', encoding='utf-8') as f:
    c = f.read()

pos1 = c.find('BAGIAN 4:')
pos2 = c.find('BAGIAN 5:')
print(c[pos1:pos2])
