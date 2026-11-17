# -*- coding: utf-8 -*-
with open('profil.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. profilVisiQuote
t_visi = '<blockquote style="font-size: 22px; font-weight: 800; line-height: 1.5; margin: 24px auto; max-width: 900px; color: #ffffff;">'
r_visi = '<blockquote id="profilVisiQuote" style="font-size: 22px; font-weight: 800; line-height: 1.5; margin: 24px auto; max-width: 900px; color: #ffffff;">'
if t_visi in html: html = html.replace(t_visi, r_visi)

# 2. profilMisiList
t_misi = '<!-- MISI SEKOLAH -->\n                <div class="card" style="padding: 30px; border-top: 4px solid var(--secondary);">'
# find the <ol> right after
idx_m = html.find(t_misi)
if idx_m != -1:
    idx_ol = html.find('<ol', idx_m)
    idx_ol_end = html.find('>', idx_ol)
    html = html[:idx_ol] + '<ol id="profilMisiList"' + html[idx_ol+3:]

# 3. profilTujuanList
t_tujuan = '<!-- TUJUAN SEKOLAH -->\n                <div class="card" style="padding: 30px; border-top: 4px solid var(--primary);">'
idx_t = html.find(t_tujuan)
if idx_t != -1:
    idx_ol = html.find('<ol', idx_t)
    html = html[:idx_ol] + '<ol id="profilTujuanList"' + html[idx_ol+3:]

# 4. profilSejarahText
t_sej = '<!-- SEJARAH SINGKAT & KONTEKS KAMPUNG DUKWIA -->\n            <div class="card" style="padding: 32px;">'
r_sej = '<!-- SEJARAH SINGKAT & KONTEKS KAMPUNG DUKWIA -->\n            <div class="card" style="padding: 32px;" id="profilSejarahCard">'
if t_sej in html: html = html.replace(t_sej, r_sej)

# 5. Table IDs
# NPSN
if '<td style="padding: 8px 0; font-weight: 700; color: var(--primary);">60300868</td>' in html:
    html = html.replace('<td style="padding: 8px 0; font-weight: 700; color: var(--primary);">60300868</td>', '<td id="profilNPSN" style="padding: 8px 0; font-weight: 700; color: var(--primary);">60301140</td>')
elif '60300868' in html:
    html = html.replace('60300868', '60301140')

with open('profil.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated profil.html with dynamic target IDs!")

# Update kontak.html
with open('kontak.html', 'r', encoding='utf-8') as f:
    k_html = f.read()

# Alamat card
t_alamat = '<h4 style="font-size: 15px; font-weight: 800; color: var(--dark); margin-bottom: 4px;">Alamat Sekolah</h4>\n                                <p style="font-size: 13.5px; color: #475569;">'
r_alamat = '<h4 style="font-size: 15px; font-weight: 800; color: var(--dark); margin-bottom: 4px;">Alamat Sekolah</h4>\n                                <p id="kontakAlamatText" style="font-size: 13.5px; color: #475569;">'
if t_alamat in k_html: k_html = k_html.replace(t_alamat, r_alamat)

# Telepon
t_tel = '<h4 style="font-size: 15px; font-weight: 800; color: var(--dark); margin-bottom: 4px;">Telepon & WhatsApp</h4>\n                                <p style="font-size: 14px; font-weight: 700; color: #0f172a; margin-bottom: 2px;">0812-4821-9125</p>'
r_tel = '<h4 style="font-size: 15px; font-weight: 800; color: var(--dark); margin-bottom: 4px;">Telepon & WhatsApp</h4>\n                                <p id="kontakTeleponText" style="font-size: 14px; font-weight: 700; color: #0f172a; margin-bottom: 2px;">0812-4821-9125</p>'
if t_tel in k_html: k_html = k_html.replace(t_tel, r_tel)

# Email
t_email = '<h4 style="font-size: 15px; font-weight: 800; color: var(--dark); margin-bottom: 4px;">Email Resmi</h4>\n                                <p style="font-size: 14px; font-weight: 700; color: #0f172a; margin-bottom: 2px;">sdninpresarso8@gmail.com</p>'
r_email = '<h4 style="font-size: 15px; font-weight: 800; color: var(--dark); margin-bottom: 4px;">Email Resmi</h4>\n                                <p id="kontakEmailText" style="font-size: 14px; font-weight: 700; color: #0f172a; margin-bottom: 2px;">sdninpresarso8@gmail.com</p>'
if t_email in k_html: k_html = k_html.replace(t_email, r_email)

# Jam Kerja
t_jam = '<h4 style="font-size: 15px; font-weight: 800; color: var(--dark); margin-bottom: 4px;">Jam Operasional Dinas</h4>\n                                <p style="font-size: 13.5px; color: #475569;">'
r_jam = '<h4 style="font-size: 15px; font-weight: 800; color: var(--dark); margin-bottom: 4px;">Jam Operasional Dinas</h4>\n                                <p id="kontakJamKerjaText" style="font-size: 13.5px; color: #475569;">'
if t_jam in k_html: k_html = k_html.replace(t_jam, r_jam)

with open('kontak.html', 'w', encoding='utf-8') as f:
    f.write(k_html)
print("Updated kontak.html with dynamic target IDs!")
