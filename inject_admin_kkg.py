# Script to update admin.html with full tab-sop and tab-kkg forms

with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

# 1. Update TAB KKG
old_kkg_summary = """                <!-- RINGKASAN PENGELOMPOKAN KERJA GUSEK 1 -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 24px;">
                    <div class="card" style="padding: 18px; border-left: 4px solid #0284c7;">
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                            <span style="font-size: 24px;">🏛️</span>
                            <strong style="font-size: 14px; color: #0f172a;">K3S Gugus 1 Arso Barat</strong>
                        </div>
                        <p style="font-size: 12.5px; color: #475569; margin: 0; line-height: 1.5;">KKKS Gusek 1 Arso Barat (Ketua: Robi Ulludin, S.Pd.SD. - Sekretariat: Jl. Melati Barat Arso I, Sanggaria). Hari: Rabu Bergilir.</p>
                    </div>
                    <div class="card" style="padding: 18px; border-left: 4px solid #10b981;">
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                            <span style="font-size: 24px;">🟢</span>
                            <strong style="font-size: 14px; color: #065f46;">KKG Kelompok A</strong>
                        </div>
                        <p style="font-size: 12.5px; color: #475569; margin: 0; line-height: 1.5;">Guru Kelas Awal (Kelas 1, 2, 3 & Agama). Materi: Modul Ajar Mendalam, Kisi-kisi ATS & AAS. Hari: Rabu Bergilir.</p>
                    </div>
                    <div class="card" style="padding: 18px; border-left: 4px solid #0284c7;">
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                            <span style="font-size: 24px;">🔵</span>
                            <strong style="font-size: 14px; color: #0369a1;">KKG Kelompok B</strong>
                        </div>
                        <p style="font-size: 12.5px; color: #475569; margin: 0; line-height: 1.5;">Guru Kelas Tinggi (Kelas 4, 5, 6, PJOK, Seni, B.Inggris). Materi: Deep Learning, Kisi-kisi ATS & AAS. Hari: Rabu Bergilir.</p>
                    </div>
                </div>"""

new_kkg_profil_form = """                <!-- PENGELOLA PROFIL GUGUS 1, K3S & KKG KELOMPOK A/B (DINAMIS & DAPAT DIUBAH) -->
                <div class="card" style="padding: 24px; margin-bottom: 25px; border-left: 5px solid #0284c7;" id="cardKKGProfilManager">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
                        <div>
                            <h3 style="font-size: 17px; font-weight: 800; color: #0f172a; margin: 0; display: flex; align-items: center; gap: 8px;">
                                <span>🏛️</span> <span>Pengelola Profil Gugus 1, Program Strategis K3S & KKG Kelompok A / B</span>
                            </h3>
                            <p style="font-size: 13px; color: var(--dark-muted); margin: 3px 0 0;">
                                Kelola alamat sekretariat bila ada perpindahan, pimpinan pengelola, waktu pertemuan rutin, dasar penetapan SK, uraian program kerja K3S, dan fokus kerja Kelompok A & B secara dinamis.
                            </p>
                        </div>
                        <div style="display: flex; gap: 8px;">
                            <button type="button" id="btnSimpanKKGProfil" class="btn btn-primary" style="font-size: 12.5px; padding: 7px 16px;">
                                💾 Simpan Profil & Program Gugus
                            </button>
                            <button type="button" id="btnResetKKGProfil" class="btn btn-secondary" style="font-size: 12.5px; padding: 7px 14px;">
                                ↺ Pulihkan Default
                            </button>
                        </div>
                    </div>

                    <!-- BAGIAN 1: IDENTITAS RESMI GUGUS 1 -->
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; margin-bottom: 18px;">
                        <h4 style="font-size: 14.5px; font-weight: 800; color: #0369a1; margin: 0 0 12px 0;">
                            📌 1. Identitas Resmi Gugus 1 Arso Barat:
                        </h4>
                        <div class="form-row">
                            <div class="form-group" style="flex: 2;">
                                <label class="form-label">Alamat Sekretariat Gugus 1 * (Dapat diganti bila ada perubahan kantor)</label>
                                <input type="text" id="kkgSekretariatInput" class="form-control" placeholder="Contoh: Jalan Melati Barat Arso I, Kampung Sanggaria, Distrik Arso Barat 99473">
                            </div>
                            <div class="form-group" style="flex: 1.2;">
                                <label class="form-label">Waktu Pertemuan Rutin *</label>
                                <input type="text" id="kkgWaktuInput" class="form-control" placeholder="Contoh: Hari Rabu Bergilir (Semester Gasal TP 2026/2027)">
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-group" style="flex: 1.5;">
                                <label class="form-label">Ketua Pengelola Gugus (Nama Lengkap & Gelar) *</label>
                                <input type="text" id="kkgKetuaInput" class="form-control" placeholder="Contoh: Robi Ulludin, S.Pd.SD.">
                            </div>
                            <div class="form-group" style="flex: 1;">
                                <label class="form-label">NIP Ketua Pengelola *</label>
                                <input type="text" id="kkgNIPKetuaInput" class="form-control" placeholder="Contoh: 196906201992031018">
                            </div>
                            <div class="form-group" style="flex: 1.5;">
                                <label class="form-label">Dasar Penetapan Gugus (SK Resmi & Tanggal) *</label>
                                <input type="text" id="kkgDasarSKInput" class="form-control" placeholder="Contoh: SK Resmi Gusek 1 Arso Barat, 23 Juli 2026">
                            </div>
                        </div>
                        <div class="form-group" style="margin-bottom: 0;">
                            <label class="form-label">Deskripsi & Tujuan Gugus Sekolah 1</label>
                            <textarea id="kkgDeskripsiInput" class="form-control" rows="2" placeholder="Deskripsi umum gugus kemitraan antar-satuan pendidikan..."></textarea>
                        </div>
                    </div>

                    <!-- BAGIAN 2: URAIAN PROGRAM KERJA STRATEGIS K3S -->
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; margin-bottom: 18px;">
                        <h4 style="font-size: 14.5px; font-weight: 800; color: #0284c7; margin: 0 0 6px 0;">
                            📋 2. Uraian Program Kerja Strategis K3S (Kelompok Kerja Kepala Sekolah):
                        </h4>
                        <p style="font-size: 12px; color: #64748b; margin: 0 0 10px 0;">
                            Tuliskan 1 poin program kerja per baris. Program ini akan tampil langsung di halaman publik Pengembangan Guru.
                        </p>
                        <textarea id="k3sProgramsInput" class="form-control" rows="5" placeholder="Tuliskan program kerja K3S (1 poin per baris)..."></textarea>
                    </div>

                    <!-- BAGIAN 3 & 4: KELOMPOK KERJA A & B -->
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px;">
                        <!-- KELOMPOK A -->
                        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 18px;">
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
                                <span style="font-size: 20px;">🟢</span>
                                <h4 style="font-size: 14.5px; font-weight: 800; color: #166534; margin: 0;">KKG Kelompok A (Kelas Awal & Agama)</h4>
                            </div>
                            <div class="form-group">
                                <label class="form-label" style="font-size: 12px;">Judul Kelompok Kerja:</label>
                                <input type="text" id="kkgKelAJudul" class="form-control" placeholder="Guru Kelas I, II, III & Guru Pendidikan Agama">
                            </div>
                            <div class="form-group">
                                <label class="form-label" style="font-size: 12px;">Cakupan Anggota Guru:</label>
                                <input type="text" id="kkgKelACakupan" class="form-control" placeholder="Guru Kelas 1, Kelas 2, Kelas 3, dan Guru Agama">
                            </div>
                            <div class="form-group">
                                <label class="form-label" style="font-size: 12px;">Hari / Jadwal Pertemuan:</label>
                                <input type="text" id="kkgKelAJadwal" class="form-control" placeholder="Hari Rabu Bergilir di Sekolah Anggota Gugus">
                            </div>
                            <div class="form-group" style="margin-bottom: 0;">
                                <label class="form-label" style="font-size: 12px;">Uraian Program Nyata Kelompok A (1 Poin Per Baris):</label>
                                <textarea id="kkgKelAPrograms" class="form-control" rows="5" placeholder="Tuliskan program materi/fokus Kelompok A (1 poin per baris)..."></textarea>
                            </div>
                        </div>

                        <!-- KELOMPOK B -->
                        <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 10px; padding: 18px;">
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
                                <span style="font-size: 20px;">🔵</span>
                                <h4 style="font-size: 14.5px; font-weight: 800; color: #1e40af; margin: 0;">KKG Kelompok B (Kelas Tinggi & Mapel)</h4>
                            </div>
                            <div class="form-group">
                                <label class="form-label" style="font-size: 12px;">Judul Kelompok Kerja:</label>
                                <input type="text" id="kkgKelBJudul" class="form-control" placeholder="Guru Kelas IV, V, VI, PJOK & Bahasa Inggris">
                            </div>
                            <div class="form-group">
                                <label class="form-label" style="font-size: 12px;">Cakupan Anggota Guru:</label>
                                <input type="text" id="kkgKelBCakupan" class="form-control" placeholder="Guru Kelas 4, Kelas 5, Kelas 6, Guru PJOK, Seni & B.Inggris">
                            </div>
                            <div class="form-group">
                                <label class="form-label" style="font-size: 12px;">Hari / Jadwal Pertemuan:</label>
                                <input type="text" id="kkgKelBJadwal" class="form-control" placeholder="Hari Rabu Bergilir di Sekolah Anggota Gugus">
                            </div>
                            <div class="form-group" style="margin-bottom: 0;">
                                <label class="form-label" style="font-size: 12px;">Uraian Program Nyata Kelompok B (1 Poin Per Baris):</label>
                                <textarea id="kkgKelBPrograms" class="form-control" rows="5" placeholder="Tuliskan program materi/fokus Kelompok B (1 poin per baris)..."></textarea>
                            </div>
                        </div>
                    </div>
                </div>"""

admin_html = admin_html.replace(old_kkg_summary, new_kkg_profil_form, 1)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)

print("admin.html updated with KKG Profil Manager form!")
