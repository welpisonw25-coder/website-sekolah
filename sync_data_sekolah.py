import json

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print("Keys in data_sekolah.json:", list(db.keys()))

# Check profil
if 'profil' in db:
    print("Profil found in db:", db['profil'].get('visi')[:50])
else:
    print("Profil NOT in db, adding default profil...")

db['profil'] = {
    "visi": "MEWUJUDKAN PESERTA DIDIK YANG BERPRESTASI DALAM BIDANG KEIMANAN (BERTAQWA), BERKARAKTER, MAMPU BERKOLABORASI, SEHAT JASMANI, UNGGUL DALAM ILMU PENGETAHUAN DAN TEKNOLOGI (IPTEK), SERTA MENCINTAI LINGKUNGAN.",
    "misi": [
        "Mengembangkan potensi peserta didik agar bertaqwa kepada Tuhan Yang Maha Esa.",
        "Menyelenggarakan pendidikan yang demokratis, menjunjung tinggi hak asasi, nilai keagamaan, dan nilai kultural bangsa.",
        "Menyelenggarakan pendidikan yang beraspirasi dari seluruh warga sekolah dan masyarakat sekitar.",
        "Melaksanakan evaluasi pendidikan dalam penjaminan mutu yang bertanggung jawab dan transparan.",
        "Menjalin hubungan erat dengan komite sekolah, tokoh masyarakat, dan berperan aktif dalam pelaksanaan pendidikan."
    ],
    "tujuan": [
        "Siswa beriman dan berakhlak mulia kepada Tuhan Yang Maha Esa.",
        "Siswa senantiasa sehat jasmani dan rohani.",
        "Siswa memiliki dasar-dasar pengetahuan dan ketrampilan untuk melanjutkan pendidikan ke jenjang yang lebih tinggi (SMP).",
        "Siswa mengenal dan mencintai bangsa, masyarakat, dan ragam budaya Nusantara, khususnya budaya lokal Papua.",
        "Siswa kreatif, terampil, bekerja keras, serta mampu mengembangkan diri secara terus-menerus."
    ],
    "sejarah": "SD Negeri Inpres Arso VIII didirikan sebagai bagian dari program pemerataan akses pendidikan nasional di kawasan pemukiman transmigrasi dan masyarakat lokal Arso, Kabupaten Keerom. Beralamat di Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, sekolah ini menjadi sentra pendidikan bagi warga sekitar yang majemuk.\n\nDengan luas area mencapai 10.000 m² milik pemerintah, sekolah ini memiliki potensi lingkungan yang sangat luas, sejuk, dan asri. Meskipun kondisi sarana prasarana fisik bangunan seperti ruang kelas, ruang TIK, dan ruang kantor saat ini berstatus rusak sedang dan masih memerlukan perhatian serta renovasi berkala dari pemerintah daerah, semangat 12 tenaga pendidik dan 157 siswa tetap menyala tinggi.\n\nKehadiran jaringan satelit berkecepatan tinggi Starlink menjadi lompatan bersejarah bagi SDN Inpres Arso VIII, membuktikan bahwa keterbatasan geografis bukan halangan bagi anak-anak di tanah Keerom Papua untuk bersaing menguasai ilmu pengetahuan dan teknologi modern.",
    "identitas": {
        "npsn": "60301140",
        "nss": "101250302008",
        "akreditasi": "A (Unggul - BAN-SM 2023)",
        "status_kepemilikan": "Pemerintah Daerah",
        "sk_pendirian": "01/SK/PDK/1984",
        "sk_izin_operasional": "0005/OPS.SD/DPM-PTSP/VII/2026",
        "luas_tanah": "10.000 m²",
        "daya_listrik": "2.200 Watt",
        "alamat": "Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua 99473"
    }
}

# Simplify admin_users to single admin
db['admin_users'] = [
    {
        "id": "USR-ADMIN",
        "username": "admin",
        "nama": "Administrator Utama SDN Inpres Arso VIII",
        "role": "Administrator Utama",
        "level": "superadmin",
        "status": "Aktif"
    }
]

with open('data_sekolah.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print("data_sekolah.json updated successfully with clean profil and single admin user!")
