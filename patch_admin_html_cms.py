# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Sidebar Nav Items
target_sidebar_sambutan = '''            <a href="#" class="admin-nav-item" data-tab="tab-sambutan" onclick="switchAdminTab('tab-sambutan'); return false;">
                <span>🎙️</span> <span>Sambutan Kepala Sekolah</span>
            </a>'''

replacement_sidebar_nav = '''            <a href="#" class="admin-nav-item" data-tab="tab-sambutan" onclick="switchAdminTab('tab-sambutan'); return false;">
                <span>🎙️</span> <span>Beranda & Sambutan</span>
            </a>
            <a href="#" class="admin-nav-item" data-tab="tab-profil" onclick="switchAdminTab('tab-profil'); return false;">
                <span>🏛️</span> <span>Profil Sekolah (Visi Misi)</span>
            </a>'''

if target_sidebar_sambutan in html:
    html = html.replace(target_sidebar_sambutan, replacement_sidebar_nav)
    print("Added Profil Sekolah to sidebar")

# Add Kontak to sidebar under Kemitraan & Keprofesian or Layanan
target_sidebar_kkg = '''            <a href="#" class="admin-nav-item" data-tab="tab-kkg" onclick="switchAdminTab('tab-kkg'); return false;">
                <span>📚</span> <span>Pengembangan Guru (K3S/KKG)</span>
            </a>'''

replacement_sidebar_kkg = '''            <a href="#" class="admin-nav-item" data-tab="tab-kkg" onclick="switchAdminTab('tab-kkg'); return false;">
                <span>📚</span> <span>Pengembangan Guru (K3S/KKG)</span>
            </a>
            <a href="#" class="admin-nav-item" data-tab="tab-kontak" onclick="switchAdminTab('tab-kontak'); return false;">
                <span>📞</span> <span>Kontak & Pesan Masuk</span>
            </a>'''

if target_sidebar_kkg in html:
    html = html.replace(target_sidebar_kkg, replacement_sidebar_kkg)
    print("Added Kontak & Pesan Masuk to sidebar")

# 2. Insert tab-profil after tab-sambutan
target_tab_sambutan_end = '<!-- ==============================================\n                 3. TAB BERITA'
if target_tab_sambutan_end not in html:
    target_tab_sambutan_end = html.find('id="tab-berita"')
    # find comment before it
    idx_com = html.rfind('<!--', 0, target_tab_sambutan_end)
    target_tab_sambutan_end = html[idx_com:target_tab_sambutan_end]

tab_profil_html = '''<!-- ==============================================
                 TAB PROFIL SEKOLAH (VISI, MISI, SEJARAH, IDENTITAS)
                 ============================================== -->
            <div id="tab-profil" class="admin-tab-panel">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px; flex-wrap: wrap; gap: 14px;">
                    <div>
                        <h2 style="font-size: 24px; font-weight: 800; color: var(--primary-dark); margin: 0 0 6px;">
                            🏛️ Kelola Profil Sekolah & Identitas
                        </h2>
                        <p style="font-size: 14px; color: var(--dark-muted); margin: 0;">
                            Kelola Visi, Misi, Tujuan, Sejarah Singkat, dan Data Pokok Legalitas SDN Inpres Arso VIII yang tampil di halaman Profil Sekolah.
                        </p>
                    </div>
                    <button type="button" class="btn btn-primary" onclick="saveProfilData();" style="display: flex; align-items: center; gap: 8px; font-weight: 700; padding: 10px 22px;">
                        <span>💾</span> <span>Simpan Profil ke Cloud</span>
                    </button>
                </div>

                <form id="formProfilSekolah" onsubmit="event.preventDefault(); saveProfilData();">
                    <!-- VISI SEKOLAH -->
                    <div class="card" style="padding: 24px; margin-bottom: 24px; border-left: 4px solid var(--primary);">
                        <h3 style="font-size: 17px; font-weight: 800; color: var(--primary-dark); margin-bottom: 12px;">
                            🎯 Visi Sekolah
                        </h3>
                        <div class="form-group" style="margin-bottom: 16px;">
                            <label style="font-weight: 700; font-size: 13.5px;">Rumusan Visi Sekolah:</label>
                            <textarea id="profilVisiInput" class="form-control" rows="3" style="width: 100%; font-size: 14.5px; font-weight: 600; line-height: 1.6; border-radius: 8px; padding: 12px; border: 1.5px solid #cbd5e1;"></textarea>
                            <small style="color: #64748b;">Visi ini ditampilkan secara menonjol pada banner hijau di halaman profil.html.</small>
                        </div>
                    </div>

                    <!-- MISI & TUJUAN -->
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 24px; margin-bottom: 24px;">
                        <div class="card" style="padding: 24px; border-left: 4px solid var(--secondary);">
                            <h3 style="font-size: 17px; font-weight: 800; color: var(--primary-dark); margin-bottom: 12px;">
                                🚀 Misi Sekolah (1 butir per baris)
                            </h3>
                            <div class="form-group">
                                <textarea id="profilMisiInput" class="form-control" rows="7" style="width: 100%; font-size: 13.5px; line-height: 1.6; border-radius: 8px; padding: 12px; border: 1.5px solid #cbd5e1;"></textarea>
                                <small style="color: #64748b;">Tuliskan setiap butir misi sekolah di baris baru (tekan Enter untuk butir berikutnya).</small>
                            </div>
                        </div>

                        <div class="card" style="padding: 24px; border-left: 4px solid #16a34a;">
                            <h3 style="font-size: 17px; font-weight: 800; color: var(--primary-dark); margin-bottom: 12px;">
                                🏆 Tujuan Sekolah
                            </h3>
                            <div class="form-group">
                                <textarea id="profilTujuanInput" class="form-control" rows="7" style="width: 100%; font-size: 13.5px; line-height: 1.6; border-radius: 8px; padding: 12px; border: 1.5px solid #cbd5e1;"></textarea>
                                <small style="color: #64748b;">Rumusan tujuan pendidikan dasar yang ingin dicapai sekolah.</small>
                            </div>
                        </div>
                    </div>

                    <!-- SEJARAH SINGKAT -->
                    <div class="card" style="padding: 24px; margin-bottom: 24px; border-left: 4px solid #8b5cf6;">
                        <h3 style="font-size: 17px; font-weight: 800; color: var(--primary-dark); margin-bottom: 12px;">
                            📜 Kilas Sejarah & Konteks Geografis Sekolah
                        </h3>
                        <div class="form-group">
                            <textarea id="profilSejarahInput" class="form-control" rows="5" style="width: 100%; font-size: 13.5px; line-height: 1.7; border-radius: 8px; padding: 12px; border: 1.5px solid #cbd5e1;"></textarea>
                            <small style="color: #64748b;">Gunakan 2 kali Enter (baris kosong) untuk memisahkan antar paragraf sejarah.</small>
                        </div>
                    </div>

                    <!-- DATA IDENTITAS & LEGALITAS SEKOLAH -->
                    <div class="card" style="padding: 24px; margin-bottom: 24px; border-left: 4px solid #0284c7;">
                        <h3 style="font-size: 17px; font-weight: 800; color: var(--primary-dark); margin-bottom: 16px;">
                            📌 Data Pokok Legalitas & Identitas Satuan Pendidikan
                        </h3>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px;">
                            <div>
                                <label style="font-weight: 700; font-size: 13px; color: #334155;">NPSN:</label>
                                <input type="text" id="identitasNPSN" class="form-control" style="width: 100%; font-weight: 700;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px; color: #334155;">NSS:</label>
                                <input type="text" id="identitasNSS" class="form-control" style="width: 100%;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px; color: #334155;">Status Akreditasi:</label>
                                <input type="text" id="identitasAkreditasi" class="form-control" style="width: 100%; font-weight: 700; color: #16a34a;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px; color: #334155;">Status Kepemilikan:</label>
                                <input type="text" id="identitasKepemilikan" class="form-control" style="width: 100%;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px; color: #334155;">SK Pendirian Sekolah:</label>
                                <input type="text" id="identitasSKPendirian" class="form-control" style="width: 100%;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px; color: #334155;">SK Izin Operasional:</label>
                                <input type="text" id="identitasSKOperasional" class="form-control" style="width: 100%;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px; color: #334155;">Luas Tanah (m²):</label>
                                <input type="text" id="identitasLuasTanah" class="form-control" style="width: 100%;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px; color: #334155;">Daya Listrik:</label>
                                <input type="text" id="identitasDayaListrik" class="form-control" style="width: 100%;">
                            </div>
                            <div style="grid-column: 1 / -1;">
                                <label style="font-weight: 700; font-size: 13px; color: #334155;">Alamat Lengkap Satuan Pendidikan:</label>
                                <input type="text" id="identitasAlamat" class="form-control" style="width: 100%;">
                            </div>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: flex-end; gap: 12px; margin-top: 20px;">
                        <button type="button" class="btn btn-secondary" onclick="populateProfilForm();">Batal / Muat Ulang</button>
                        <button type="submit" class="btn btn-primary" style="padding: 10px 24px; font-weight: 800;">
                            💾 Simpan Perubahan Profil ke Cloud
                        </button>
                    </div>
                </form>
            </div>

            '''

# Insert tab-profil before tab-berita
idx_berita = html.find('id="tab-berita"')
idx_com_berita = html.rfind('<!--', 0, idx_berita)
html = html[:idx_com_berita] + tab_profil_html + html[idx_com_berita:]
print("Inserted tab-profil into admin.html")

# 3. Insert tab-kontak after tab-sop
tab_kontak_html = '''<!-- ==============================================
                 TAB KONTAK & KOTAK MASUK PESAN TAMU
                 ============================================== -->
            <div id="tab-kontak" class="admin-tab-panel">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px; flex-wrap: wrap; gap: 14px;">
                    <div>
                        <h2 style="font-size: 24px; font-weight: 800; color: var(--primary-dark); margin: 0 0 6px;">
                            📞 Kelola Kontak Resmi & Kotak Masuk Pesan
                        </h2>
                        <p style="font-size: 14px; color: var(--dark-muted); margin: 0;">
                            Kelola informasi saluran komunikasi resmi sekolah dan pantau pertanyaan/aspirasi masyarakat dari form kontak publik.
                        </p>
                    </div>
                    <button type="button" class="btn btn-primary" onclick="saveKontakData();" style="display: flex; align-items: center; gap: 8px; font-weight: 700; padding: 10px 22px;">
                        <span>💾</span> <span>Simpan Kontak ke Cloud</span>
                    </button>
                </div>

                <!-- 1. FORM PENGATURAN KONTAK RESMI -->
                <div class="card" style="padding: 24px; margin-bottom: 30px; border-left: 4px solid var(--primary);">
                    <h3 style="font-size: 17px; font-weight: 800; color: var(--primary-dark); margin-bottom: 16px;">
                        ⚙️ Saluran Komunikasi Resmi Sekolah
                    </h3>
                    <form id="formKontakResmi" onsubmit="event.preventDefault(); saveKontakData();">
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; margin-bottom: 18px;">
                            <div>
                                <label style="font-weight: 700; font-size: 13px;">Nomor Telepon Dinas:</label>
                                <input type="text" id="kontakInputTelepon" class="form-control" style="width: 100%; font-weight: 700;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px;">Nomor WhatsApp Resmi (Awali 62):</label>
                                <input type="text" id="kontakInputWhatsApp" class="form-control" style="width: 100%; font-weight: 700; color: #16a34a;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px;">Email Resmi Sekolah:</label>
                                <input type="email" id="kontakInputEmail" class="form-control" style="width: 100%;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px;">Jam Operasional Pelayanan:</label>
                                <input type="text" id="kontakInputJamKerja" class="form-control" style="width: 100%;">
                            </div>
                            <div style="grid-column: 1 / -1;">
                                <label style="font-weight: 700; font-size: 13px;">Alamat Surat Menyurat:</label>
                                <input type="text" id="kontakInputAlamat" class="form-control" style="width: 100%;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px;">Koordinat GPS (Lat, Long):</label>
                                <input type="text" id="kontakInputKoordinat" class="form-control" style="width: 100%;">
                            </div>
                            <div>
                                <label style="font-weight: 700; font-size: 13px;">Link Google Maps Embed (iframe src):</label>
                                <input type="text" id="kontakInputMaps" class="form-control" style="width: 100%;">
                            </div>
                        </div>
                        <div style="text-align: right;">
                            <button type="submit" class="btn btn-primary" style="padding: 9px 20px; font-weight: 700;">
                                Simpan Saluran Kontak
                            </button>
                        </div>
                    </form>
                </div>

                <!-- 2. KOTAK MASUK PESAN DARI MASYARAKAT / WALI MURID -->
                <div class="card" style="padding: 24px; border-left: 4px solid var(--secondary);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
                        <div>
                            <h3 style="font-size: 17px; font-weight: 800; color: var(--primary-dark); margin: 0 0 4px;">
                                📬 Kotak Masuk Pesan Pengunjung (Form Kontak Publik)
                            </h3>
                            <p style="font-size: 13px; color: var(--dark-muted); margin: 0;">Pesan dan pertanyaan yang dikirimkan oleh orang tua atau warga melalui kontak.html.</p>
                        </div>
                        <button type="button" class="btn btn-secondary" onclick="renderPesanKontakTable();" style="font-size: 12.5px; padding: 6px 14px;">
                            🔄 Muat Ulang Pesan
                        </button>
                    </div>

                    <div style="overflow-x: auto;">
                        <table class="table" style="width: 100%; border-collapse: collapse; font-size: 13.5px;">
                            <thead>
                                <tr style="background: #f8fafc; border-bottom: 2px solid #e2e8f0; text-align: left;">
                                    <th style="padding: 10px 12px; width: 140px;">Waktu & Tanggal</th>
                                    <th style="padding: 10px 12px; width: 180px;">Nama Pengirim</th>
                                    <th style="padding: 10px 12px; width: 130px;">No. Telepon / WA</th>
                                    <th style="padding: 10px 12px; width: 160px;">Subjek</th>
                                    <th style="padding: 10px 12px;">Isi Pesan</th>
                                    <th style="padding: 10px 12px; width: 110px;">Status</th>
                                    <th style="padding: 10px 12px; width: 130px; text-align: center;">Aksi</th>
                                </tr>
                            </thead>
                            <tbody id="pesanKontakTableBody">
                                <!-- Diisi otomatis oleh JavaScript -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            '''

idx_pengaturan = html.find('id="tab-pengaturan"')
idx_com_pengaturan = html.rfind('<!--', 0, idx_pengaturan)
html = html[:idx_com_pengaturan] + tab_kontak_html + html[idx_com_pengaturan:]
print("Inserted tab-kontak into admin.html")

# 4. In tab-sambutan: add Marquee Manager
target_sambutan_form_end = '</form>\n            </div>'
replacement_sambutan_marquee = '''</form>

                <!-- KELOLA MARQUEE / TEKS BERJALAN BERANDA -->
                <div class="card" style="padding: 24px; margin-top: 28px; border-left: 4px solid #0284c7;">
                    <h3 style="font-size: 17px; font-weight: 800; color: var(--primary-dark); margin-bottom: 12px;">
                        📢 Teks Pengumuman Berjalan Beranda (Running Text / Marquee)
                    </h3>
                    <div class="form-group" style="margin-bottom: 14px;">
                        <label style="font-weight: 700; font-size: 13px;">Isi Teks Berjalan di Atas Beranda:</label>
                        <textarea id="berandaMarqueeInput" class="form-control" rows="2" style="width: 100%; font-size: 14px; padding: 10px; border-radius: 8px; border: 1.5px solid #cbd5e1;"></textarea>
                        <small style="color: #64748b;">Teks ini bergerak perlahan di baris paling atas halaman depan (index.html) untuk menyampaikan pengumuman penting.</small>
                    </div>
                    <div style="text-align: right;">
                        <button type="button" class="btn btn-primary" onclick="saveBerandaMarquee();" style="padding: 8px 18px; font-weight: 700;">
                            💾 Simpan Teks Berjalan
                        </button>
                    </div>
                </div>
            </div>'''

if target_sambutan_form_end in html:
    html = html.replace(target_sambutan_form_end, replacement_sambutan_marquee, 1)
    print("Added Marquee manager to tab-sambutan")

# 5. In formBerita: Add Status dropdown (Terbitkan vs Draft)
target_berita_kategori = '<div class="form-group" style="margin-bottom: 16px;">\n                            <label style="font-weight: 700; font-size: 13.5px;">Kategori Berita:</label>'
replacement_berita_status = '''<div class="form-group" style="margin-bottom: 16px;">
                            <label style="font-weight: 700; font-size: 13.5px;">Status Publikasi Konten:</label>
                            <select id="beritaStatus" class="form-control" style="width: 100%; font-weight: 700; padding: 8px 12px;">
                                <option value="published" selected>🚀 Terbitkan Langsung (Tampil di Website Publik)</option>
                                <option value="draft">💾 Simpan Sebagai Draft (Belum Ditampilkan ke Pengunjung)</option>
                            </select>
                        </div>
                        <div class="form-group" style="margin-bottom: 16px;">
                            <label style="font-weight: 700; font-size: 13.5px;">Kategori Berita:</label>'''

if target_berita_kategori in html:
    html = html.replace(target_berita_kategori, replacement_berita_status, 1)
    print("Added status selector to formBerita")

# 6. In formPengumuman: Add Status dropdown (Terbitkan vs Draft)
target_pengumuman_kategori = '<div class="form-group" style="margin-bottom: 16px;">\n                            <label style="font-weight: 700; font-size: 13.5px;">Kategori Pengumuman:</label>'
replacement_pengumuman_status = '''<div class="form-group" style="margin-bottom: 16px;">
                            <label style="font-weight: 700; font-size: 13.5px;">Status Publikasi Konten:</label>
                            <select id="pengumumanStatus" class="form-control" style="width: 100%; font-weight: 700; padding: 8px 12px;">
                                <option value="published" selected>🚀 Terbitkan Langsung (Tampil di Website Publik)</option>
                                <option value="draft">💾 Simpan Sebagai Draft (Belum Ditampilkan ke Pengunjung)</option>
                            </select>
                        </div>
                        <div class="form-group" style="margin-bottom: 16px;">
                            <label style="font-weight: 700; font-size: 13.5px;">Kategori Pengumuman:</label>'''

if target_pengumuman_kategori in html:
    html = html.replace(target_pengumuman_kategori, replacement_pengumuman_status, 1)
    print("Added status selector to formPengumuman")

# 7. In formGaleri: Add Status dropdown
target_galeri_kategori = '<div class="form-group" style="margin-bottom: 16px;">\n                            <label style="font-weight: 700; font-size: 13.5px;">Kategori Album:</label>'
replacement_galeri_status = '''<div class="form-group" style="margin-bottom: 16px;">
                            <label style="font-weight: 700; font-size: 13.5px;">Status Publikasi Foto:</label>
                            <select id="galeriStatus" class="form-control" style="width: 100%; font-weight: 700; padding: 8px 12px;">
                                <option value="published" selected>🚀 Terbitkan Langsung (Tampil di Galeri Publik)</option>
                                <option value="draft">💾 Simpan Sebagai Draft (Arsip Internal)</option>
                            </select>
                        </div>
                        <div class="form-group" style="margin-bottom: 16px;">
                            <label style="font-weight: 700; font-size: 13.5px;">Kategori Album:</label>'''

if target_galeri_kategori in html:
    html = html.replace(target_galeri_kategori, replacement_galeri_status, 1)
    print("Added status selector to formGaleri")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully patched admin.html with new tabs and status selectors!")
