with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    pg = f.read()

# 1. Deskripsi
pg = pg.replace(
    '<p style="font-size: 14px; color: #475569; line-height: 1.7; margin-bottom: 18px;">\n                    Gugus Sekolah 1 (Gusek 1)',
    '<p id="pgGusekDeskripsi" style="font-size: 14px; color: #475569; line-height: 1.7; margin-bottom: 18px;">\n                    Gugus Sekolah 1 (Gusek 1)'
)

# 2. Identitas Gugus
pg = pg.replace(
    '<div>📍 <strong>Sekretariat:</strong> Jalan Melati Barat Arso I, Kampung Sanggaria, Distrik Arso Barat 99473</div>',
    '<div>📍 <strong>Sekretariat:</strong> <span id="pgGusekSekretariat">Jalan Melati Barat Arso I, Kampung Sanggaria, Distrik Arso Barat 99473</span></div>'
)
pg = pg.replace(
    '<div>👤 <strong>Ketua Pengelola:</strong> Robi Ulludin, S.Pd.SD. (NIP 196906201992031018)</div>',
    '<div>👤 <strong>Ketua Pengelola:</strong> <span id="pgGusekKetua">Robi Ulludin, S.Pd.SD. (NIP 196906201992031018)</span></div>'
)
pg = pg.replace(
    '<div>⏱️ <strong>Waktu Pertemuan:</strong> Hari Rabu Bergilir (Semester Gasal TP 2026/2027)</div>',
    '<div>⏱️ <strong>Waktu Pertemuan:</strong> <span id="pgGusekWaktu">Hari Rabu Bergilir (Semester Gasal TP 2026/2027)</span></div>'
)
pg = pg.replace(
    '<div>📜 <strong>Dasar Penetapan:</strong> SK Resmi Gusek 1 Arso Barat, 23 Juli 2026</div>',
    '<div>📜 <strong>Dasar Penetapan:</strong> <span id="pgGusekDasarSK">SK Resmi Gusek 1 Arso Barat, 23 Juli 2026</span></div>'
)

# 3. K3S
pg = pg.replace(
    '<ul style="margin: 0; padding-left: 20px; font-size: 13.5px; color: #334155; line-height: 1.8;">\n                        <li>Harmonisasi kalender pendidikan',
    '<ul id="pgK3SProgramsList" style="margin: 0; padding-left: 20px; font-size: 13.5px; color: #334155; line-height: 1.8;">\n                        <li>Harmonisasi kalender pendidikan'
)
pg = pg.replace(
    '<div style="font-size: 13px; color: #64748b;">\n                    👤 Ketua Pengelola KKKS Gusek 1:',
    '<div id="pgK3SKetuaBox" style="font-size: 13px; color: #64748b;">\n                    👤 Ketua Pengelola KKKS Gusek 1:'
)

# 4. Kelompok A
pg = pg.replace(
    '<h3 style="font-size: 19px; font-weight: 800; color: #0f172a; margin-bottom: 8px;">\n                            Guru Kelas I, II, III & Guru Bidang Keagamaan\n                        </h3>',
    '<h3 id="pgKelompokAJudul" style="font-size: 19px; font-weight: 800; color: #0f172a; margin-bottom: 8px;">\n                            Guru Kelas I, II, III & Guru Bidang Keagamaan\n                        </h3>'
)
pg = pg.replace(
    '<strong>Cakupan Anggota:</strong> Guru Kelas 1, Guru Kelas 2, Guru Kelas 3, serta Guru Pendidikan Agama Islam (PAI), Kristen Protestan, dan Katolik se-Gugus 1.',
    '<strong>Cakupan Anggota:</strong> <span id="pgKelompokACakupan">Guru Kelas 1, Guru Kelas 2, Guru Kelas 3, serta Guru Pendidikan Agama Islam (PAI), Kristen Protestan, dan Katolik se-Gugus 1.</span>'
)
pg = pg.replace(
    '<ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #334155; line-height: 1.7;">\n                                <li>Bedah modul ajar Kurikulum Merdeka Fase A',
    '<ul id="pgKelompokAProgramsList" style="margin: 0; padding-left: 18px; font-size: 13px; color: #334155; line-height: 1.7;">\n                                <li>Bedah modul ajar Kurikulum Merdeka Fase A'
)
pg = pg.replace(
    '⏱️ Jadwal: <strong>Hari Rabu Bergilir di Sekolah Anggota Gugus</strong>',
    '⏱️ Jadwal: <strong id="pgKelompokAJadwal">Hari Rabu Bergilir di Sekolah Anggota Gugus</strong>'
)

# 5. Kelompok B
pg = pg.replace(
    '<h3 style="font-size: 19px; font-weight: 800; color: #0f172a; margin-bottom: 8px;">\n                            Guru Kelas IV, V, VI, Guru Penjas (PJOK) & Bahasa Inggris\n                        </h3>',
    '<h3 id="pgKelompokBJudul" style="font-size: 19px; font-weight: 800; color: #0f172a; margin-bottom: 8px;">\n                            Guru Kelas IV, V, VI, Guru Penjas (PJOK) & Bahasa Inggris\n                        </h3>'
)
pg = pg.replace(
    '<strong>Cakupan Anggota:</strong> Guru Kelas 4, Guru Kelas 5, Guru Kelas 6, Guru PJOK (Penjasorkes), dan Guru Bahasa Inggris se-Gugus 1.',
    '<strong>Cakupan Anggota:</strong> <span id="pgKelompokBCakupan">Guru Kelas 4, Guru Kelas 5, Guru Kelas 6, Guru PJOK (Penjasorkes), dan Guru Bahasa Inggris se-Gugus 1.</span>'
)
pg = pg.replace(
    '<ul style="margin: 0; padding-left: 18px; font-size: 13px; color: #334155; line-height: 1.7;">\n                                <li>Pemantapan bimbingan dan simulasi Asesmen Nasional Berbasis Komputer',
    '<ul id="pgKelompokBProgramsList" style="margin: 0; padding-left: 18px; font-size: 13px; color: #334155; line-height: 1.7;">\n                                <li>Pemantapan bimbingan dan simulasi Asesmen Nasional Berbasis Komputer'
)

with open('pengembangan-guru.html', 'w', encoding='utf-8') as f:
    f.write(pg)

print("pengembangan-guru.html updated with dynamic IDs!")
