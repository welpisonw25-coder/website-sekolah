# -*- coding: utf-8 -*-
import json
import urllib.request
import time

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# 1. Pastikan setiap berita memiliki status: published jika belum ada
for b in db.get('berita', []):
    if 'status' not in b:
        b['status'] = 'published'

# 2. Pastikan setiap pengumuman memiliki status: published jika belum ada
for p in db.get('pengumuman', []):
    if 'status' not in p:
        p['status'] = 'published'

# 3. Pastikan setiap galeri memiliki status: published jika belum ada
for g in db.get('galeri', []):
    if 'status' not in g:
        g['status'] = 'published'

# 4. Tambah node profil
if 'profil' not in db:
    db['profil'] = {
        "visi": "Terwujudnya Peserta Didik yang Beriman, Bertakwa, Berakhlak Mulia, Cerdas, Terampil, Mandiri, dan Berwawasan Lingkungan.",
        "misi": [
            "Menanamkan nilai-nilai keagamaan dan budi pekerti luhur dalam kehidupan sehari-hari seluruh warga sekolah.",
            "Melaksanakan pembelajaran aktif, inovatif, kreatif, efektif, dan menyenangkan berbasis Kurikulum Merdeka.",
            "Meningkatkan kecakapan literasi, numerasi, dan penguasaan teknologi dasar (TIK) dengan fasilitas internet satelit Starlink.",
            "Mengembangkan bakat, minat, dan potensi peserta didik melalui kegiatan ekstrakurikuler kepramukaan, olahraga, dan seni budaya Papua.",
            "Menciptakan lingkungan sekolah yang bersih, asri, aman, nyaman, dan berbudaya lingkungan sehat."
        ],
        "tujuan": "Membentuk lulusan yang beriman dan bertakwa kepada Tuhan Yang Maha Esa, berkarakter Profil Pelajar Pancasila, memiliki dasar-dasar ilmu pengetahuan dan teknologi, serta berjiwa mandiri dan siap melanjutkan pendidikan ke jenjang SMP/sederajat.",
        "sejarah": "SD Negeri Inpres Arso VIII didirikan pada tahun 1984 untuk melayani kebutuhan pendidikan dasar anak-anak masyarakat transmigrasi dan masyarakat adat di wilayah Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua. Dalam perjalanannya, sekolah ini terus berbenah dan saat ini telah terakreditasi A (Unggul) dengan fasilitas laboratorium TIK berbasis satelit Starlink.",
        "identitas": {
            "npsn": "60301140",
            "nss": "101250302008",
            "nama_sekolah": "SD Negeri Inpres Arso VIII",
            "status": "Negeri",
            "bentuk_pendidikan": "Sekolah Dasar (SD)",
            "status_kepemilikan": "Pemerintah Daerah Kabupaten Keerom",
            "sk_pendirian": "01/SK/PDK/1984",
            "sk_izin_operasional": "421/045/DISDIK/2018",
            "akreditasi": "A (Unggul - BAN-S/M)",
            "alamat": "Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Provinsi Papua 99473",
            "luas_tanah": "5.400 m² (Bersertifikat Hak Milik Pemda)",
            "daya_listrik": "2.200 Watt + Genset Cadangan",
            "akses_internet": "Satelit Starlink Kecepatan Tinggi & Telkomsel Orbit"
        }
    }

# 5. Tambah node beranda
if 'beranda' not in db:
    db['beranda'] = {
        "tagline": "Sekolah Dasar Unggul Berkarakter, Cerdas, dan Berbasis Teknologi di Tanah Papua",
        "sub_tagline": "Membina Generasi Emas Kabupaten Keerom yang Berakhlak Mulia dan Berprestasi",
        "marquee": "Selamat datang di Website Resmi SD Negeri Inpres Arso VIII Kabupaten Keerom Papua. Penerimaan Peserta Didik Baru (PPDB) Tahun Ajaran 2026/2027 telah dibuka! Silakan daftar online melalui menu PPDB.",
        "headline_badge": "🏛️ SD NEGERI INPRES ARSO VIII — TERAKREDITASI A"
    }

# 6. Tambah node kontak
if 'kontak' not in db:
    db['kontak'] = {
        "alamat": "Jalan Sulawesi, RW 03 / RT 05, Kampung Dukwia, Distrik Arso Barat, Kab. Keerom, Papua 99473",
        "telepon": "0812-4821-9125",
        "whatsapp": "6281248219125",
        "email": "sdninpresarso8@gmail.com",
        "jam_kerja": "Senin – Jumat: 07.15 – 12.30 WIT (Sabtu: Kegiatan Ekstrakurikuler & Pramuka)",
        "maps_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3985.748123456789!2d140.703999!3d-2.822991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMsKwNDknMjIuOCJTIDE0MMKwNDInMTQuNCJF!5e0!3m2!1sid!2sid!4v1",
        "koordinat": "Lat -2.822991º, Long 140.703999º",
        "facebook": "https://facebook.com",
        "youtube": "https://youtube.com"
    }

# 7. Tambah node pesan_kontak jika belum ada
if 'pesan_kontak' not in db:
    db['pesan_kontak'] = [
        {
            "id": "MSG-001",
            "nama": "Markus Wenda",
            "telepon": "0813-4455-6677",
            "subjek": "Informasi Siswa Pindahan",
            "pesan": "Selamat siang Kepala Sekolah, kami berencana memindahkan anak kami ke kelas 4 di SDN Inpres Arso VIII karena kepindahan tugas orang tua ke Keerom. Mohon info kelengkapan berkasnya. Terima kasih.",
            "tanggal": "14 November 2026 10:15 WIT",
            "status": "Ditanggapi"
        }
    ]

# 8. Tambah node admin_users (multi-role)
if 'admin_users' not in db:
    db['admin_users'] = [
        {
            "id": "USR-001",
            "username": "kepsek",
            "nama": "Adi Puspito, S.Pd",
            "role": "Kepala Sekolah",
            "level": "superadmin",
            "email": "adipuspito@gmail.com",
            "status": "Aktif",
            "akses": ["semua_menu", "publikasi", "kelola_akun", "hapus_data"]
        },
        {
            "id": "USR-002",
            "username": "operator",
            "nama": "Warno, S.Pd",
            "role": "Operator Dapodik & Sekolah",
            "level": "operator",
            "email": "operator.arso8@gmail.com",
            "status": "Aktif",
            "akses": ["siswa", "ppdb", "sarpras", "berita", "pengumuman", "galeri", "kontak"]
        },
        {
            "id": "USR-003",
            "username": "guru",
            "nama": "Ferdinandus Belau, S.Pd",
            "role": "Dewan Guru / Editor Konten",
            "level": "guru",
            "email": "guru.arso8@gmail.com",
            "status": "Aktif",
            "akses": ["berita", "pengumuman", "kkg", "sop", "galeri"]
        }
    ]

# 9. Tambah node admin_logs (catatan riwayat aktivitas)
if 'admin_logs' not in db:
    db['admin_logs'] = [
        {
            "id": "LOG-001",
            "waktu": "15 Nov 2026, 17:15 WIT",
            "user": "Kepala Sekolah (Adi Puspito, S.Pd)",
            "role": "Super Admin",
            "aksi": "Penyempurnaan Arsitektur CMS",
            "keterangan": "Menghubungkan seluruh menu website ke Google Cloud Database"
        },
        {
            "id": "LOG-002",
            "waktu": "15 Nov 2026, 16:40 WIT",
            "user": "Operator Sekolah (Warno, S.Pd)",
            "role": "Operator",
            "aksi": "Sinkronisasi Papan Pengumuman & Berita Terkini",
            "keterangan": "Menghubungkan slider kabar terkini dan papan pengumuman beranda"
        }
    ]

# Simpan ke data_sekolah.json lokal
with open('data_sekolah.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
print("Updated local data_sekolah.json successfully!")

# Sinkronkan ke Firebase menggunakan PATCH
cloud_url = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json'
req = urllib.request.Request(cloud_url, data=json.dumps(db).encode('utf-8'), headers={'Content-Type': 'application/json'}, method='PATCH')
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print("Firebase response code:", resp.status)
        print("Successfully synced complete schema to Google Cloud Firebase!")
except Exception as e:
    print("Error syncing to Firebase:", e)
