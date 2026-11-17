# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_end_pengaturan = '</div>\n            </div>\n\n        </main>'
if target_end_pengaturan not in html:
    # find where tab-pengaturan closes
    idx_p = html.find('id="tab-pengaturan"')
    idx_main_close = html.find('</main>', idx_p)
    target_end_pengaturan = html[idx_main_close-30:idx_main_close]

user_and_logs_html = '''                <!-- 2. KELOLA PENGGUNA & HAK AKSES BERJENJANG (MULTI-ROLE) -->
                <div class="card" style="padding: 24px; border-left: 5px solid #16a34a; margin-bottom: 24px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
                        <div>
                            <h3 style="font-size: 17px; font-weight: 800; color: #0f172a; margin: 0; display: flex; align-items: center; gap: 8px;">
                                <span>👥</span> <span>Kelola Pengguna & Hak Akses Sistem (Kepala Sekolah, Operator, Guru)</span>
                            </h3>
                            <p style="font-size: 13px; color: var(--dark-muted); margin: 3px 0 0;">
                                Pembagian wewenang pengelolaan konten sesuai tugas pokok dan fungsi (Tupoksi) masing-masing.
                            </p>
                        </div>
                        <button type="button" class="btn btn-primary" onclick="showAddUserModal();" style="font-size: 12.5px; padding: 7px 16px;">
                            ➕ Tambah Pengguna Baru
                        </button>
                    </div>

                    <div style="overflow-x: auto;">
                        <table class="table" style="width: 100%; border-collapse: collapse; font-size: 13.5px;">
                            <thead>
                                <tr style="background: #f8fafc; border-bottom: 2px solid #e2e8f0; text-align: left;">
                                    <th style="padding: 10px 12px; width: 140px;">Nama Pengguna</th>
                                    <th style="padding: 10px 12px; width: 180px;">Nama Lengkap / Jabatan</th>
                                    <th style="padding: 10px 12px; width: 140px;">Peran (Role)</th>
                                    <th style="padding: 10px 12px; width: 180px;">Email Terdaftar</th>
                                    <th style="padding: 10px 12px;">Cakupan Hak Akses</th>
                                    <th style="padding: 10px 12px; width: 90px;">Status</th>
                                    <th style="padding: 10px 12px; width: 110px; text-align: center;">Aksi</th>
                                </tr>
                            </thead>
                            <tbody id="adminUsersTableBody">
                                <!-- Diisi otomatis oleh JavaScript -->
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 3. CATATAN RIWAYAT AKTIVITAS PENGELOLA (AUDIT LOGS) -->
                <div class="card" style="padding: 24px; border-left: 5px solid #8b5cf6; margin-bottom: 24px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
                        <div>
                            <h3 style="font-size: 17px; font-weight: 800; color: #0f172a; margin: 0; display: flex; align-items: center; gap: 8px;">
                                <span>📜</span> <span>Catatan Riwayat Aktivitas Admin (Audit Trail)</span>
                            </h3>
                            <p style="font-size: 13px; color: var(--dark-muted); margin: 3px 0 0;">
                                Rekam jejak seluruh aksi penambahan, penyuntingan, penghapusan, dan publikasi data sekolah.
                            </p>
                        </div>
                        <button type="button" class="btn btn-secondary" onclick="renderActivityLogs();" style="font-size: 12.5px; padding: 6px 14px;">
                            🔄 Segarkan Log
                        </button>
                    </div>

                    <div style="overflow-x: auto; max-height: 380px; overflow-y: auto;">
                        <table class="table" style="width: 100%; border-collapse: collapse; font-size: 13px;">
                            <thead>
                                <tr style="background: #f8fafc; border-bottom: 2px solid #e2e8f0; text-align: left; position: sticky; top: 0; z-index: 1;">
                                    <th style="padding: 9px 12px; width: 170px;">Waktu & Tanggal (WIT)</th>
                                    <th style="padding: 9px 12px; width: 190px;">Pengguna (User)</th>
                                    <th style="padding: 9px 12px; width: 130px;">Peran</th>
                                    <th style="padding: 9px 12px; width: 200px;">Tindakan / Aksi</th>
                                    <th style="padding: 9px 12px;">Rincian Keterangan</th>
                                </tr>
                            </thead>
                            <tbody id="adminLogsTableBody">
                                <!-- Diisi otomatis oleh JavaScript -->
                            </tbody>
                        </table>
                    </div>
                </div>
'''

idx_p = html.find('id="tab-pengaturan"')
idx_main_close = html.find('</main>', idx_p)
idx_last_div = html.rfind('</div>', idx_p, idx_main_close)

html = html[:idx_last_div] + user_and_logs_html + html[idx_last_div:]

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully injected User Management and Audit Logs into tab-pengaturan!")
