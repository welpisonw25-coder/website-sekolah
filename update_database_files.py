import json

sop_data_default = {
    "tata_tertib_guru": [
        "Jam 07.00 WIT – Seluruh dewan guru sudah hadir di sekolah sebelum aktivitas pembelajaran dimulai.",
        "Budaya 5S – Menerapkan pembiasaan Senyum, Salam, Sapa, Sopan, dan Santun kepada seluruh warga sekolah dan tamu.",
        "Persiapan Upacara – Pukul 07.00 WIT persiapan barisan upacara dan tepat pukul 07.15 WIT upacara bendera dimulai secara khidmat.",
        "Pembina Upacara Bergilir – Guru secara terjadwal dan bergilir bertindak sebagai Pembina Upacara sesuai jadwal yang ditetapkan.",
        "Keteladanan Karakter – Guru senantiasa meneladani peserta didik untuk selalu menjaga ketertiban, sopan santun, dan kebersihan lingkungan sekolah.",
        "Disiplin Waktu – Disiplin waktu datang dan pulang sesuai ketentuan kedinasan yang berlaku.",
        "Kewajiban Seragam – Wajib memakai seragam dinas harian sesuai ketentuan jadwal mingguan (siklus 5 minggu) yang telah ditetapkan.",
        "Ekstrakurikuler Wajib – Wajib mendampingi dan mengikuti kegiatan ekstrakurikuler Gerakan Pramuka.",
        "Pemberitahuan Izin – Guru yang berhalangan hadir atau sakit wajib memberikan surat pemberitahuan / izin resmi kepada Kepala Sekolah.",
        "Presensi Akhir – Menandatangani daftar hadir resmi pada akhir kegiatan pembelajaran setiap hari kerja.",
        "Tanggung Jawab Guru Piket – Guru piket wajib mengisi buku piket harian, menyambut siswa di gerbang, dan bertanggung jawab penuh menjaga ketertiban selama jam pembelajaran berlangsung."
    ],
    "tata_tertib_siswa": [
        "Kehadiran Tepat Waktu – Peserta didik datang pukul 07.00 WIT sebelum pembelajaran berlangsung.",
        "Membudayakan 5S – Menerapkan salam, senyum, sapa, sopan, dan santun kepada guru, tenaga kependidikan, serta sesama teman.",
        "Kewajiban Upacara Bendera – Wajib mengikuti upacara bendera setiap hari Senin dengan mengenakan seragam lengkap (topi dan dasi).",
        "Budaya Lingkungan Bersih – Membudayakan lingkungan bersih, aktif memungut sampah, dan membuangnya pada tempat sampah yang tersedia.",
        "Tugas Piket Kelas – Peserta didik yang bertugas piket wajib hadir lebih awal untuk menyapu, membersihkan ruang kelas, lingkungan kelas, dan fasilitas MCK.",
        "Waktu Pembelajaran – Peserta didik masuk kelas mulai jam 07.30 WIT dan berakhir hingga jam 14.00 WIT sesuai jadwal rombel.",
        "Adab Berdoa – Membudayakan berdoa bersama dengan khusyuk sebelum memulai dan sesudah mengakhiri pembelajaran.",
        "Berbaris Tertib – Sebelum memasuki ruang kelas, peserta didik berbaris rapi di depan kelas dipimpin ketua kelas dan bersalaman dengan guru.",
        "Keamanan Lingkungan – Dilarang keluar pagar atau meninggalkan lingkungan sekolah tanpa izin guru piket atau wali kelas selama jam sekolah.",
        "Menjaga Fasilitas Sekolah – Menjaga ketertiban, kebersihan, serta merawat sarana dan prasarana sekolah dengan rasa tanggung jawab."
    ],
    "piket_guru": {
        "Senin": ["Elias Tabuni, S.Pd", "Flavianus Rainaldus, S.Ag"],
        "Selasa": ["Esther Tina Maria Panjaitan, S.Pd", "Cicik Mursidah, S.Pd"],
        "Rabu": ["Warno, S.Pd.SD", "Yuli Syetia Sari, S.Pd"],
        "Kamis": ["Rini Handayani, S.Pd", "Ferdinand, S.Pd"],
        "Jumat": ["Zainal Habiib Al Arif, S.Pd", "Umi Wildana Zulfa"]
    },
    "seragam_guru": [
        {
            "siklus": "Minggu Ke-1",
            "senin_selasa": "Seragam Keki (Khaki)",
            "rabu": "Putih - Hitam",
            "kamis": "Batik Papua Warna Hijau",
            "jumat": "Kaos Merah Maroon"
        },
        {
            "siklus": "Minggu Ke-2",
            "senin_selasa": "Seragam Keki (Khaki)",
            "rabu": "Putih - Hitam",
            "kamis": "Batik Papua Merah",
            "jumat": "Kaos Hitam"
        },
        {
            "siklus": "Minggu Ke-3",
            "senin_selasa": "Seragam Keki (Khaki)",
            "rabu": "Putih - Hitam",
            "kamis": "Batik Papua Cenderawasih",
            "jumat": "Kaos Biru Lengan Panjang"
        },
        {
            "siklus": "Minggu Ke-4",
            "senin_selasa": "Seragam Keki (Khaki)",
            "rabu": "Putih - Hitam",
            "kamis": "Batik Jawa Lengan Panjang",
            "jumat": "Kaos Merah Lengan Panjang"
        },
        {
            "siklus": "Minggu Ke-5",
            "senin_selasa": "Seragam Keki (Khaki)",
            "rabu": "Putih - Hitam",
            "kamis": "Batik Papua Bebas",
            "jumat": "Kaos Kuning Lengan Panjang"
        }
    ],
    "pramuka_pembina": {
        "jadwal": "Dilaksanakan 2 (dua) kali setiap bulan pada hari Jumat pukul 15.00 – 17.00 WIT di lingkungan sekolah.",
        "siaga": [
            "Yuli Syetia Sari, S.Pd",
            "Ferdinand, S.Pd",
            "Rita Paulina Wabiser, S.Pd",
            "Elias Tabuni, S.Pd",
            "Esther Tina Maria Panjaitan, S.Pd",
            "Flavianus Rainaldus, S.Ag"
        ],
        "penggalang": [
            "Warno, S.Pd.SD",
            "Cicik Mursidah, S.Pd",
            "Rini Handayani, S.Pd",
            "Zainal Habiib Al Arif, S.Pd",
            "Umi Wildana Zulfa"
        ]
    }
}

# Update data_sekolah.json
with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['sop_data'] = sop_data_default

with open('data_sekolah.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data_sekolah.json updated successfully with sop_data!")

# Update js/data_sekolah.js
js_content = f"// Data Sekolah SDN Inpres Arso VIII - Generated\nwindow.SDN_DATABASE = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
with open('js/data_sekolah.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("js/data_sekolah.js updated successfully with window.SDN_DATABASE!")
