with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = '<div class="card" style="padding: 24px; margin-bottom: 25px;" id="cardGuruForm">'

card_bagan = '''<!-- PENGELOLAAN BAGAN STRUKTUR ORGANISASI SEKOLAH -->
                <div class="card" style="padding: 24px; margin-bottom: 25px; border-left: 4px solid var(--secondary); background: #ffffff; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 14px; margin-bottom: 16px;">
                        <div>
                            <h3 style="font-size: 16.5px; font-weight: 800; color: var(--primary-dark); margin-bottom: 4px; display: flex; align-items: center; gap: 8px;">
                                <span>🏛️</span> Pengelolaan Bagan Struktur Organisasi Dewan Guru
                            </h3>
                            <p style="font-size: 13px; color: var(--dark-muted); margin: 0;">
                                Sistem ini mendukung dua mode: <strong>Bagan Interaktif Otomatis</strong> (nama guru langsung terhubung dari data di bawah) atau <strong>Unggah File Bagan Baru</strong>.
                            </p>
                        </div>
                        <span id="baganStatusBadge" class="badge" style="padding: 6px 12px; font-size: 12px; font-weight: 700; background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd;">
                            ✨ Mode: Terkoneksi Otomatis dengan Data Guru
                        </span>
                    </div>

                    <!-- Panel Unggah File Bagan Kustom -->
                    <div style="background: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 10px; padding: 18px; margin-bottom: 14px;">
                        <label class="form-label" style="font-weight: 700; color: #1e293b; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
                            <span>📁</span> Ganti / Masukkan Berkas Bagan Struktur Baru (Foto / Desain Gambar):
                        </label>
                        <p style="font-size: 12px; color: #64748b; margin-bottom: 12px;">
                            Bila sekolah memiliki berkas gambar bagan baru (hasil foto papan struktur sekolah atau desain grafis JPG/PNG/WEBP), unggah di sini agar langsung tayang menggantikan bagan lama di website publik.
                        </p>
                        <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
                            <input type="file" id="inputCustomBaganFile" class="form-control" accept="image/*" style="flex: 1; min-width: 240px; padding: 7px 12px;">
                            <button type="button" id="btnUploadCustomBagan" class="btn btn-primary" style="padding: 9px 18px; font-size: 13px; font-weight: 700;">
                                📤 Pasang Bagan Gambar Baru
                            </button>
                            <button type="button" id="btnResetBaganToSvg" class="btn btn-secondary" style="padding: 9px 16px; font-size: 13px; font-weight: 700;" title="Kembalikan ke bagan interaktif yang terkoneksi otomatis dengan nama-nama guru">
                                ↺ Kembalikan ke Bagan Interaktif Otomatis
                            </button>
                        </div>
                    </div>

                    <!-- Area Pratinjau Bagan Kustom Saat Ini -->
                    <div id="adminBaganPreviewContainer" style="display: none; padding: 14px; background: #f1f5f9; border: 1px solid #e2e8f0; border-radius: 10px; margin-top: 10px;">
                        <div style="font-size: 12.5px; font-weight: 700; color: #334155; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                            <span>👁️ Gambar Bagan Kustom yang Sedang Tayang di Website:</span>
                            <button type="button" id="btnHapusCustomBagan" class="btn btn-danger" style="padding: 5px 12px; font-size: 12px; font-weight: 700;">🗑️ Hapus Gambar & Pakai Bagan Otomatis</button>
                        </div>
                        <div style="text-align: center; background: #ffffff; padding: 10px; border-radius: 8px; border: 1px solid #cbd5e1;">
                            <img id="adminBaganPreviewImg" src="" alt="Pratinjau Bagan Struktur Sekolah" style="max-height: 240px; width: auto; max-width: 100%; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
                        </div>
                    </div>

                    <!-- Keterangan Sinkronisasi Otomatis -->
                    <div style="font-size: 12px; color: #0369a1; background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 8px; padding: 10px 14px; margin-top: 12px; display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 16px;">💡</span>
                        <span><strong>Info Sinkronisasi Cerdas:</strong> Saat menggunakan Bagan Interaktif Bawaan, setiap kali Kaka menambah, mengedit, atau mengganti guru (misal: Kepala Sekolah, Wali Kelas 1-6, Guru PJOK, atau Guru Agama) pada tabel di bawah, nama di bagan struktur otomatis ikut terbarukan seketika tanpa perlu mengubah manual satu per satu!</span>
                    </div>
                </div>

                '''

if target in html:
    html = html.replace(target, card_bagan + target, 1)
    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added Bagan Management Card to admin.html successfully!")
else:
    print("Target not found in admin.html!")
