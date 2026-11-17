with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

# Let's inspect the exact lines of tab-sop
start_marker = '<div id="tab-sop" class="admin-tab-panel">'
end_marker = '<!-- ==============================================\n                 8. TAB PENGATURAN AKUN'

start_idx = admin_html.find(start_marker)
end_idx = admin_html.find(end_marker)

print(f"start_idx: {start_idx}, end_idx: {end_idx}")

new_tab_sop = """<div id="tab-sop" class="admin-tab-panel">
                <div style="margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                    <div>
                        <h2 style="font-size: 22px; font-weight: 800; color: var(--primary-dark);">📜 Kelola SOP, Tata Tertib, Piket, Seragam & Pembina Pramuka</h2>
                        <p style="font-size: 13.5px; color: var(--dark-muted);">Kelola poin tata tertib pendidik & peserta didik, jadwal piket harian guru, rotasi seragam dinas 5 minggu, dan tim pembina kepramukaan yang tersinkronisasi dinamis ke halaman publik.</p>
                    </div>
                    <div style="display: flex; gap: 8px;">
                        <a href="sop.html" target="_blank" class="btn btn-secondary" style="font-size: 12.5px; padding: 7px 16px; text-decoration: none;">
                            🌐 Buka Halaman SOP Publik
                        </a>
                        <a href="guru.html" target="_blank" class="btn btn-secondary" style="font-size: 12.5px; padding: 7px 16px; text-decoration: none;">
                            👨‍🏫 Buka Halaman Dewan Guru
                        </a>
                    </div>
                </div>

                <!-- 1. KELOLA POIN TATA TERTIB GURU & SISWA -->
                <div class="card" style="padding: 24px; margin-bottom: 25px; border-left: 5px solid #0284c7;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
                        <div>
                            <h3 style="font-size: 17px; font-weight: 800; color: #0f172a; margin: 0; display: flex; align-items: center; gap: 8px;">
                                <span>📋</span> <span>1. Kelola Poin-Poin Tata Tertib & Kedisiplinan Sekolah</span>
                            </h3>
                            <p style="font-size: 13px; color: var(--dark-muted); margin: 3px 0 0;">
                                Ubah, tambah, atau kurangi tata tertib guru dan siswa bila ada aturan baru. Tuliskan 1 poin per baris (awali dengan judul singkat dan tanda '–').
                            </p>
                        </div>
                        <div style="display: flex; gap: 8px;">
                            <button type="button" id="btnSimpanSOPTatib" class="btn btn-primary" style="font-size: 12.5px; padding: 7px 16px;">
                                💾 Simpan Tata Tertib
                            </button>
                            <button type="button" id="btnResetSOPTatib" class="btn btn-secondary" style="font-size: 12.5px; padding: 7px 14px;">
                                ↺ Pulihkan Default
                            </button>
                        </div>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px;">
                        <!-- TATA TERTIB GURU -->
                        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px;">
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                                <span style="font-size: 20px;">👨‍🏫</span>
                                <h4 style="font-size: 14.5px; font-weight: 800; color: #0f172a; margin: 0;">Tata Tertib Guru & Tenaga Kependidikan</h4>
                            </div>
                            <p style="font-size: 12px; color: #64748b; margin: 0 0 10px 0;">Poin disiplin pendidik, kehadiran jam 07.00, budaya 5S, dan keteladanan.</p>
                            <textarea id="sopTatibGuruInput" class="form-control" rows="10" placeholder="Tuliskan 1 poin per baris..."></textarea>
                        </div>

                        <!-- TATA TERTIB SISWA -->
                        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px;">
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                                <span style="font-size: 20px;">👨‍🎓</span>
                                <h4 style="font-size: 14.5px; font-weight: 800; color: #0f172a; margin: 0;">Tata Tertib & Larangan Peserta Didik</h4>
                            </div>
                            <p style="font-size: 12px; color: #64748b; margin: 0 0 10px 0;">Poin disiplin murid, jam masuk, upacara bendera, piket kelas, dan aturan belajar.</p>
                            <textarea id="sopTatibSiswaInput" class="form-control" rows="10" placeholder="Tuliskan 1 poin per baris..."></textarea>
                        </div>
                    </div>
                </div>

                <!-- 2. KELOLA JADWAL PIKET HARIAN GURU (SENIN S/D JUMAT) -->
                <div class="card" style="padding: 24px; margin-bottom: 25px; border-left: 5px solid #10b981;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
                        <div>
                            <h3 style="font-size: 17px; font-weight: 800; color: #0f172a; margin: 0; display: flex; align-items: center; gap: 8px;">
                                <span>👥</span> <span>2. Kelola Jadwal Piket Harian Guru (Senin – Jumat)</span>
                            </h3>
                            <p style="font-size: 13px; color: var(--dark-muted); margin: 3px 0 0;">
                                Pilih nama guru piket dari menu dropdown yang terhubung otomatis dengan database Dewan Guru SDN Inpres Arso VIII.
                            </p>
                        </div>
                        <div style="display: flex; gap: 8px;">
                            <button type="button" id="btnSimpanSOPPiket" class="btn btn-primary" style="font-size: 12.5px; padding: 7px 16px; background: #059669; border-color: #059669;">
                                💾 Simpan Jadwal Piket
                            </button>
                            <button type="button" id="btnResetSOPPiket" class="btn btn-secondary" style="font-size: 12.5px; padding: 7px 14px;">
                                ↺ Pulihkan Default
                            </button>
                        </div>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px;">
                        <!-- SENIN -->
                        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px;">
                            <div style="font-weight: 800; color: #0f172a; font-size: 14px; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                                <span>📅</span> <span>SENIN</span>
                            </div>
                            <div class="form-group" style="margin-bottom: 8px;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 1:</label>
                                <select id="sopPiket_senin_1" class="form-control guru-dropdown"></select>
                            </div>
                            <div class="form-group" style="margin-bottom: 0;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 2:</label>
                                <select id="sopPiket_senin_2" class="form-control guru-dropdown"></select>
                            </div>
                        </div>

                        <!-- SELASA -->
                        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px;">
                            <div style="font-weight: 800; color: #0f172a; font-size: 14px; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                                <span>📅</span> <span>SELASA</span>
                            </div>
                            <div class="form-group" style="margin-bottom: 8px;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 1:</label>
                                <select id="sopPiket_selasa_1" class="form-control guru-dropdown"></select>
                            </div>
                            <div class="form-group" style="margin-bottom: 0;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 2:</label>
                                <select id="sopPiket_selasa_2" class="form-control guru-dropdown"></select>
                            </div>
                        </div>

                        <!-- RABU -->
                        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px;">
                            <div style="font-weight: 800; color: #0f172a; font-size: 14px; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                                <span>📅</span> <span>RABU</span>
                            </div>
                            <div class="form-group" style="margin-bottom: 8px;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 1:</label>
                                <select id="sopPiket_rabu_1" class="form-control guru-dropdown"></select>
                            </div>
                            <div class="form-group" style="margin-bottom: 0;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 2:</label>
                                <select id="sopPiket_rabu_2" class="form-control guru-dropdown"></select>
                            </div>
                        </div>

                        <!-- KAMIS -->
                        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px;">
                            <div style="font-weight: 800; color: #0f172a; font-size: 14px; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                                <span>📅</span> <span>KAMIS</span>
                            </div>
                            <div class="form-group" style="margin-bottom: 8px;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 1:</label>
                                <select id="sopPiket_kamis_1" class="form-control guru-dropdown"></select>
                            </div>
                            <div class="form-group" style="margin-bottom: 0;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 2:</label>
                                <select id="sopPiket_kamis_2" class="form-control guru-dropdown"></select>
                            </div>
                        </div>

                        <!-- JUMAT -->
                        <div style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px;">
                            <div style="font-weight: 800; color: #0f172a; font-size: 14px; margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
                                <span>📅</span> <span>JUMAT</span>
                            </div>
                            <div class="form-group" style="margin-bottom: 8px;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 1:</label>
                                <select id="sopPiket_jumat_1" class="form-control guru-dropdown"></select>
                            </div>
                            <div class="form-group" style="margin-bottom: 0;">
                                <label style="font-size: 11px; font-weight: 700; color: #475569;">Guru Piket 2:</label>
                                <select id="sopPiket_jumat_2" class="form-control guru-dropdown"></select>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 3. KELOLA JADWAL PEMAKAIAN SERAGAM GURU (5 SIKLUS MINGGUAN) -->
                <div class="card" style="padding: 24px; margin-bottom: 25px; border-left: 5px solid #f59e0b;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
                        <div>
                            <h3 style="font-size: 17px; font-weight: 800; color: #0f172a; margin: 0; display: flex; align-items: center; gap: 8px;">
                                <span>👔</span> <span>3. Kelola Jadwal Pemakaian Seragam Guru (5 Siklus Mingguan)</span>
                            </h3>
                            <p style="font-size: 13px; color: var(--dark-muted); margin: 3px 0 0;">
                                Tentukan ketentuan seragam dinas guru untuk Senin–Selasa, Rabu, Kamis, dan Jumat pada setiap siklus pekan 1 sampai 5.
                            </p>
                        </div>
                        <div style="display: flex; gap: 8px;">
                            <button type="button" id="btnSimpanSOPSeragam" class="btn btn-primary" style="font-size: 12.5px; padding: 7px 16px; background: #d97706; border-color: #d97706;">
                                💾 Simpan Jadwal Seragam
                            </button>
                            <button type="button" id="btnResetSOPSeragam" class="btn btn-secondary" style="font-size: 12.5px; padding: 7px 14px;">
                                ↺ Pulihkan Default
                            </button>
                        </div>
                    </div>

                    <div style="overflow-x: auto;">
                        <table style="width: 100%; border-collapse: collapse; font-size: 13px;">
                            <thead>
                                <tr style="background: #f8fafc; border-bottom: 2px solid #cbd5e1; text-align: left;">
                                    <th style="padding: 10px; width: 14%;">Siklus</th>
                                    <th style="padding: 10px; width: 24%;">Senin & Selasa</th>
                                    <th style="padding: 10px; width: 20%;">Rabu</th>
                                    <th style="padding: 10px; width: 22%;">Kamis</th>
                                    <th style="padding: 10px; width: 20%;">Jumat</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- MINGGU 1 -->
                                <tr style="border-bottom: 1px solid #f1f5f9;">
                                    <td style="padding: 10px;"><strong>Minggu Ke-1</strong></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m1_senin" class="form-control" placeholder="Contoh: Seragam Keki (Khaki)"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m1_rabu" class="form-control" placeholder="Contoh: Putih - Hitam"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m1_kamis" class="form-control" placeholder="Contoh: Batik Papua Warna Hijau"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m1_jumat" class="form-control" placeholder="Contoh: Kaos Merah Maroon"></td>
                                </tr>
                                <!-- MINGGU 2 -->
                                <tr style="border-bottom: 1px solid #f1f5f9;">
                                    <td style="padding: 10px;"><strong>Minggu Ke-2</strong></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m2_senin" class="form-control" placeholder="Seragam Keki (Khaki)"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m2_rabu" class="form-control" placeholder="Putih - Hitam"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m2_kamis" class="form-control" placeholder="Batik Papua Merah"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m2_jumat" class="form-control" placeholder="Kaos Hitam"></td>
                                </tr>
                                <!-- MINGGU 3 -->
                                <tr style="border-bottom: 1px solid #f1f5f9;">
                                    <td style="padding: 10px;"><strong>Minggu Ke-3</strong></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m3_senin" class="form-control" placeholder="Seragam Keki (Khaki)"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m3_rabu" class="form-control" placeholder="Putih - Hitam"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m3_kamis" class="form-control" placeholder="Batik Papua Cenderawasih"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m3_jumat" class="form-control" placeholder="Kaos Biru Lengan Panjang"></td>
                                </tr>
                                <!-- MINGGU 4 -->
                                <tr style="border-bottom: 1px solid #f1f5f9;">
                                    <td style="padding: 10px;"><strong>Minggu Ke-4</strong></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m4_senin" class="form-control" placeholder="Seragam Keki (Khaki)"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m4_rabu" class="form-control" placeholder="Putih - Hitam"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m4_kamis" class="form-control" placeholder="Batik Jawa Lengan Panjang"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m4_jumat" class="form-control" placeholder="Kaos Merah Lengan Panjang"></td>
                                </tr>
                                <!-- MINGGU 5 -->
                                <tr>
                                    <td style="padding: 10px;"><strong>Minggu Ke-5</strong></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m5_senin" class="form-control" placeholder="Seragam Keki (Khaki)"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m5_rabu" class="form-control" placeholder="Putih - Hitam"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m5_kamis" class="form-control" placeholder="Batik Papua Bebas"></td>
                                    <td style="padding: 8px;"><input type="text" id="sopSeragam_m5_jumat" class="form-control" placeholder="Kaos Kuning Lengan Panjang"></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 4. KELOLA TIM PEMBINA PRAMUKA (SIAGA & PENGGALANG) -->
                <div class="card" style="padding: 24px; margin-bottom: 25px; border-left: 5px solid #8b5cf6;">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
                        <div>
                            <h3 style="font-size: 17px; font-weight: 800; color: #0f172a; margin: 0; display: flex; align-items: center; gap: 8px;">
                                <span>⛺</span> <span>4. Kelola Tim Pembina Gerakan Pramuka (Siaga & Penggalang)</span>
                            </h3>
                            <p style="font-size: 13px; color: var(--dark-muted); margin: 3px 0 0;">
                                Atur jadwal latihan dan daftar nama pembina pendamping Pramuka Siaga (Kelas 1–3) dan Pramuka Penggalang (Kelas 4–6).
                            </p>
                        </div>
                        <div style="display: flex; gap: 8px;">
                            <button type="button" id="btnSimpanSOPPramuka" class="btn btn-primary" style="font-size: 12.5px; padding: 7px 16px; background: #7c3aed; border-color: #7c3aed;">
                                💾 Simpan Pembina Pramuka
                            </button>
                            <button type="button" id="btnResetSOPPramuka" class="btn btn-secondary" style="font-size: 12.5px; padding: 7px 14px;">
                                ↺ Pulihkan Default
                            </button>
                        </div>
                    </div>

                    <div class="form-group" style="margin-bottom: 18px;">
                        <label class="form-label">Waktu & Jadwal Pelaksanaan Latihan Pramuka:</label>
                        <input type="text" id="sopPramukaJadwalInput" class="form-control" placeholder="Dilaksanakan 2 (dua) kali setiap bulan pada hari Jumat pukul 15.00 – 17.00 WIT di lingkungan sekolah.">
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px;">
                        <!-- PRAMUKA SIAGA -->
                        <div style="background: #fffbeb; border: 1.5px solid #fde68a; border-radius: 10px; padding: 18px;">
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                                <span style="font-size: 20px;">🟡</span>
                                <h4 style="font-size: 14.5px; font-weight: 800; color: #92400e; margin: 0;">PRAMUKA SIAGA (Kelas 1, 2, dan 3)</h4>
                            </div>
                            <p style="font-size: 12px; color: #78350f; margin: 0 0 8px 0;">Daftar guru pembina pendamping (1 nama per baris):</p>
                            <textarea id="sopPramukaSiagaInput" class="form-control" rows="6" placeholder="Tuliskan nama pembina (1 per baris)..."></textarea>
                            <div style="margin-top: 8px;">
                                <select id="sopPramukaSiagaAddGuru" class="form-control guru-dropdown" style="font-size: 12px; background: #ffffff;">
                                    <option value="">➕ Tambah Guru dari Database Dewan Guru...</option>
                                </select>
                            </div>
                        </div>

                        <!-- PRAMUKA PENGGALANG -->
                        <div style="background: #eff6ff; border: 1.5px solid #bfdbfe; border-radius: 10px; padding: 18px;">
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                                <span style="font-size: 20px;">🔵</span>
                                <h4 style="font-size: 14.5px; font-weight: 800; color: #1e40af; margin: 0;">PRAMUKA PENGGALANG (Kelas 4, 5, dan 6)</h4>
                            </div>
                            <p style="font-size: 12px; color: #1e3a8a; margin: 0 0 8px 0;">Daftar guru pembina pendamping (1 nama per baris):</p>
                            <textarea id="sopPramukaPenggalangInput" class="form-control" rows="6" placeholder="Tuliskan nama pembina (1 per baris)..."></textarea>
                            <div style="margin-top: 8px;">
                                <select id="sopPramukaPenggalangAddGuru" class="form-control guru-dropdown" style="font-size: 12px; background: #ffffff;">
                                    <option value="">➕ Tambah Guru dari Database Dewan Guru...</option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 5. PEDOMAN RINGKAS SOP RESMI (REFERENSI KELEMBAGAAN) -->
                <div style="margin-top: 35px; margin-bottom: 12px;">
                    <h3 style="font-size: 16px; font-weight: 800; color: #475569; margin: 0 0 14px 0;">
                        📖 Referensi Dokumen Standar Operasional Prosedur (SOP) Kelembagaan
                    </h3>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                    <div class="card" style="padding: 20px;">
                        <span class="badge-tag" style="background: #e0f2fe; color: #0369a1; font-weight: 700; margin-bottom: 8px; display: inline-block;">SOP-01 : AKADEMIK & PEMBELAJARAN</span>
                        <h4 style="font-size: 15px; font-weight: 800; color: var(--primary-dark); margin-bottom: 6px;">Jam Kerja Guru & Kehadiran Peserta Didik</h4>
                        <p style="font-size: 12.5px; color: #475569; line-height: 1.6; margin: 0;">
                            Guru dan siswa hadir selambat-lambatnya pukul <strong>07.15 WIT</strong>. Upacara Senin & Senam Jumat dimulai pukul <strong>07.30 WIT</strong>. Jam pembelajaran efektif 07.45 s.d. 12.30 WIT.
                        </p>
                    </div>

                    <div class="card" style="padding: 20px;">
                        <span class="badge-tag" style="background: #fef3c7; color: #92400e; font-weight: 700; margin-bottom: 8px; display: inline-block;">SOP-02 : KEDISIPLINAN & SERAGAM</span>
                        <h4 style="font-size: 15px; font-weight: 800; color: var(--primary-dark); margin-bottom: 6px;">Ketentuan Seragam Resmi 5 Hari Sekolah</h4>
                        <p style="font-size: 12.5px; color: #475569; line-height: 1.6; margin: 0;">
                            <strong>Senin:</strong> Merah Putih lengkap topi & dasi.<br>
                            <strong>Selasa & Rabu:</strong> Batik Sekolah / Pramuka.<br>
                            <strong>Kamis:</strong> Pakaian Adat / Batik Papua.<br>
                            <strong>Jumat:</strong> Kaos Olahraga & Senam Pagi.
                        </p>
                    </div>

                    <div class="card" style="padding: 20px;">
                        <span class="badge-tag" style="background: #dcfce7; color: #166534; font-weight: 700; margin-bottom: 8px; display: inline-block;">SOP-03 : TEKNOLOGI & TIK</span>
                        <h4 style="font-size: 15px; font-weight: 800; color: var(--primary-dark); margin-bottom: 6px;">Pemanfaatan Ruang Komputer & Jaringan Starlink</h4>
                        <p style="font-size: 12.5px; color: #475569; line-height: 1.6; margin: 0;">
                            Fasilitas satelit Starlink diutamakan untuk ANBK, pelaporan Dapodik, dan pembelajaran TIK. Komputer wajib dimatikan dan kabel dirapikan setelah digunakan.
                        </p>
                    </div>

                    <div class="card" style="padding: 20px;">
                        <span class="badge-tag" style="background: #f1f5f9; color: #334155; font-weight: 700; margin-bottom: 8px; display: inline-block;">SOP-04 : KESISWAAN</span>
                        <h4 style="font-size: 15px; font-weight: 800; color: var(--primary-dark); margin-bottom: 6px;">Penerimaan Peserta Didik Baru (PPDB Online)</h4>
                        <p style="font-size: 12.5px; color: #475569; line-height: 1.6; margin: 0;">
                            Pendaftaran tidak dipungut biaya (Gratis). Berkas Akta Kelahiran, KK, dan KTP Orang Tua diverifikasi dalam 1x24 jam kerja.
                        </p>
                    </div>
                </div>
            </div>\n\n            """

admin_html = admin_html[:start_idx] + new_tab_sop + admin_html[end_idx:]

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)

print("admin.html updated successfully with complete tab-sop!")
