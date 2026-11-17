with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

marker = '<!-- 3. CATATAN RIWAYAT AKTIVITAS PENGELOLA (AUDIT LOGS) -->'
p = text.find(marker)
if p != -1:
    print(text[p:p+2000])
