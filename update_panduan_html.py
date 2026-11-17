with open('panduan-serah-terima.html', 'r', encoding='utf-8') as f:
    panduan = f.read()

target_str = """                    <tr>
                        <td><strong>💾 Cadangkan & Pulihkan (Backup)</strong></td>
                        <td>Mengamankan seluruh data website ke dalam 1 berkas aman ke flashdisk sekolah.</td>
                        <td>Klik <strong>Unduh Cadangan (.JSON)</strong> secara berkala. Jika ada salah ketik, cukup klik <strong>Pulihkan Data</strong>.</td>
                    </tr>"""

replacement_str = """                    <tr>
                        <td><strong>📜 SOP, Tata Tertib, Piket, Seragam & Pramuka</strong></td>
                        <td>Mengatur poin tata tertib guru & siswa, jadwal piket harian guru (Senin–Jumat) yang terkoneksi langsung dengan Dewan Guru, siklus seragam dinas 5 minggu, dan tim pembina Pramuka (Siaga & Penggalang).</td>
                        <td>Buka tab Dokumen SOP Sekolah di Admin. Edit teks aturan, pilih guru piket harian dari menu dropdown, tentukan seragam mingguan, atau tambahkan pembina pramuka dengan 1 klik. Klik tombol <strong>Simpan</strong> pada masing-masing bagian. Otomatis seketika tayang di halaman <code>sop.html</code> dan <code>guru.html</code>.</td>
                    </tr>
                    <tr>
                        <td><strong>📚 Pengembangan Guru: K3S & KKG Gusek 1 Arso Barat</strong></td>
                        <td>Mengelola profil kelembagaan Gugus 1: Alamat Sekretariat (bila ada kepindahan kantor), Ketua Pengelola & NIP, Waktu Pertemuan rutin, Dasar Penetapan SK, Uraian Program Strategis K3S, serta Pengelola Kelompok A dan B.</td>
                        <td>Buka tab Pengembangan Guru (K3S/KKG). Pada bagian atas, ubah rincian sekretariat, pimpinan, atau program kerja sesuai kebutuhan, lalu klik <strong>Simpan Profil & Program Gugus</strong>. Untuk jadwal bergilir bulanan dan unggah foto dokumentasi kegiatan, kelola pada formulir di bawahnya. Otomatis tayang di <code>pengembangan-guru.html</code>.</td>
                    </tr>
                    <tr>
                        <td><strong>💾 Cadangkan & Pulihkan (Backup)</strong></td>
                        <td>Mengamankan seluruh data website ke dalam 1 berkas aman ke flashdisk sekolah (mencakup SOP, data guru, siswa, PPDB, dan foto).</td>
                        <td>Klik <strong>Unduh Cadangan (.JSON)</strong> secara berkala. Jika ada salah ketik, cukup klik <strong>Pulihkan Data</strong>.</td>
                    </tr>"""

panduan = panduan.replace(target_str, replacement_str, 1)

with open('panduan-serah-terima.html', 'w', encoding='utf-8') as f:
    f.write(panduan)

print("panduan-serah-terima.html updated with SOP and KKG management guides!")
