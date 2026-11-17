with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

marker = '<!-- 3. CATATAN RIWAYAT AKTIVITAS PENGELOLA (AUDIT LOGS) -->'
p = text.find(marker)
p_end_tab = text.find('id="tab-', p)
if p_end_tab == -1:
    p_end_tab = text.find('</main>', p)

print(text[p:p_end_tab])
