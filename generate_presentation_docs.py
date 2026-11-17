import os
import shutil
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def create_docx(filename):
    doc = Document()
    
    # Page setup
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Styles
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Calibri'
    font.size = Pt(11)
    font.color.rgb = RGBColor(0x33, 0x41, 0x55) # Slate 700

    # Header / Title Box
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t = title_p.add_run("PANDUAN LENGKAP & NASKAH PRESENTASI RESMI\nSERAH TERIMA WEBSITE SD NEGERI INPRES ARSO VIII")
    run_t.font.name = 'Arial'
    run_t.font.size = Pt(18)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a) # Dark Slate

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run("Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Provinsi Papua\nDomain Resmi: https://sdninpresarso8.sch.id | NPSN: 60300958")
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(0x03, 0x69, 0xa1)

    doc.add_paragraph("―" * 55).alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Quick Info Box (Table)
    table = doc.add_table(rows=5, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Nama Sistem", "Portal Web Resmi & CMS SD Negeri Inpres Arso VIII"),
        ("Alamat Website Publik", "https://sdninpresarso8.sch.id (Alternatif: https://sdninpresarso8.surge.sh)"),
        ("Pintu Masuk Admin CMS", "https://sdninpresarso8.sch.id/admin.html"),
        ("Kredensial Login", "Username: admin   |   Password: sdnarso8juara"),
        ("Paket Master Offline", "PAKET-WEBSITE-SDN-INPRES-ARSO-8-RESMI.zip (Flashdisk Sekolah)")
    ]
    for idx, (label, val) in enumerate(info_data):
        row = table.rows[idx]
        cell_lbl = row.cells[0]
        cell_val = row.cells[1]
        cell_lbl.width = Inches(2.2)
        cell_val.width = Inches(4.5)
        cell_lbl.text = label
        cell_val.text = val
        cell_lbl.paragraphs[0].runs[0].font.bold = True
        set_cell_background(cell_lbl, "F1F5F9")
        set_cell_background(cell_val, "F8FAFC")

    doc.add_paragraph()

    # Petunjuk Praktis Presenter
    h1 = doc.add_paragraph()
    r = h1.add_run("PETUNJUK PRAKTIS UNTUK PEMBAWA MATERI (PRESENTER)")
    r.font.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x16, 0x65, 0x34) # Green 800

    p_p = doc.add_paragraph()
    p_p.add_run("• Alokasi Waktu Ideal: ").bold = True
    p_p.add_run("20 hingga 30 menit (fleksibel disesuaikan dengan sesi tanya jawab).\n")
    p_p.add_run("• Target Peserta: ").bold = True
    p_p.add_run("Bapak Kepala Sekolah (Adi Puspito, S.Pd), Seluruh Dewan Guru & Tenaga Kependidikan, serta Tenaga Operator Sekolah.\n")
    p_p.add_run("• Perlengkapan: ").bold = True
    p_p.add_run("Laptop terhubung layar proyektor, koneksi internet (atau file offline jika tanpa internet), dan Flashdisk berisi paket file master.")

    # TAHAP 1
    doc.add_paragraph()
    h = doc.add_paragraph()
    r = h.add_run("TAHAP 1: PEMBUKAAN & LATAR BELAKANG (± 3 MENIT)")
    r.font.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x03, 0x69, 0xa1)

    quote1 = doc.add_paragraph()
    quote1.paragraph_format.left_indent = Inches(0.4)
    q_r = quote1.add_run(
        '“Selamat pagi / siang, Bapak Kepala Sekolah yang saya hormati, Bapak/Ibu dewan guru sekalian, serta rekan Operator Sekolah yang kami banggakan.\n\n'
        'Puji dan syukur kita panjatkan ke hadirat Tuhan Yang Maha Esa. Hari ini adalah hari yang sangat bersejarah bagi keluarga besar SD Negeri Inpres Arso VIII. '
        'Sekolah kita yang berdiri di Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, kini telah resmi memiliki Portal Website Resmi Sekolah Berbasis Cloud Modern '
        'dengan domain terverifikasi Indonesia: sdninpresarso8.sch.id.\n\n'
        'Website ini hadir bukan sekadar pajangan formalitas, melainkan sebagai pusat transparansi informasi, wadah publikasi prestasi anak-anak kita, sarana pendaftaran siswa baru secara online, '
        'serta bukti nyata bahwa sekolah kita di perbatasan Papua mampu berdiri sejajar dengan sekolah-sekolah unggulan di kota besar.\n\n'
        'Mari bersama-sama kita saksikan tampilan dan kemudahan cara mengelolanya.”'
    )
    q_r.font.italic = True
    q_r.font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)

    # TAHAP 2
    doc.add_paragraph()
    h = doc.add_paragraph()
    r = h.add_run("TAHAP 2: TUR TAMPILAN & MENU WEBSITE PUBLIK (± 7 MENIT)")
    r.font.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x03, 0x69, 0xa1)

    doc.add_paragraph("Buka halaman beranda website di proyektor (https://sdninpresarso8.sch.id) dan jelaskan bagian berikut:").runs[0].font.italic = True

    pts2 = [
        ("Header Atas & Foto Gapura Kehormatan", "Tunjukkan Logo Kabupaten Keerom di sebelah kiri, Jam Digital Presisi di sebelah kanan, dan tombol Login Admin berbentuk ikon user. Tunjukkan foto Gapura Kehormatan sekolah yang tampak megah dan utuh, diikuti animasi sambutan bertahap (Selamat Datang -> Portal Resmi -> SDN Inpres Arso VIII)."),
        ("Slider Sorotan Info Kabar Terkini", "Tunjukkan bagaimana berita dan foto kegiatan sekolah bergulir otomatis setiap 4.5 detik. Tekankan bahwa slider ini pintar dan otomatis dibatasi maksimal 6 berita terbaru, sehingga titik-titik di bawahnya tidak akan pernah kepenuhan atau merusak tampilan di HP guru dan orang tua murid."),
        ("Menu Profil & Struktur Organisasi", "Buka menu Profil Sekolah. Perlihatkan sejarah, visi-misi sekolah berakhlak mulia dan unggul IPTEK, dasar hukum pendirian, serta Bagan Struktur Organisasi interaktif."),
        ("Menu Dewan Guru & Siswa", "Tunjukkan 12 profil pendidik lengkap dengan NIP, jabatan, foto resmi, dan mata pelajaran yang diampu. Tunjukkan pula statistik siswa 109 murid dan rekam prestasi akademik/non-akademik."),
        ("Sarana Prasarana & Internet Satelit Starlink", "Tunjukkan inventaris 6 ruang kelas, perpustakaan, fasilitas sanitasi, serta ketersediaan internet satelit Starlink dan Telkomsel Orbit yang mendukung pelaksanaan ANBK di perbatasan."),
        ("K3S & KKG Gugus 1 Arso Barat", "Klik menu 'Pengembangan Guru'. Tunjukkan bahwa SDN Inpres Arso VIII merupakan pusat kegiatan Gugus 1 Arso Barat. Perlihatkan slider dokumentasi pertemuan KKG bergilir dan tabel agenda lengkap."),
        ("Mitra Kolaborasi, Pengumuman & PPDB Online", "Tunjukkan 6 pilar kemitraan (Guru, Siswa, Orang Tua, Puskesmas/TNI/Polri). Tunjukkan formulir PPDB online yang memudahkan orang tua mendaftarkan calon siswa baru langsung lewat HP.")
    ]
    for title, desc in pts2:
        p = doc.add_paragraph()
        r1 = p.add_run(f"• {title}: ")
        r1.bold = True
        p.add_run(desc)

    # TAHAP 3
    doc.add_paragraph()
    h = doc.add_paragraph()
    r = h.add_run("TAHAP 3: DEMONSTRASI LANGSUNG PENGELOLAAN OLEH OPERATOR (CMS ADMIN) (± 10 MENIT)")
    r.font.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x03, 0x69, 0xa1)

    quote2 = doc.add_paragraph()
    quote2.paragraph_format.left_indent = Inches(0.4)
    q_r2 = quote2.add_run(
        '“Bapak Kepala Sekolah dan rekan Operator, sistem pengelola website ini dirancang sangat ramah pengguna (user-friendly). '
        'Operator atau dewan guru tidak perlu menguasai ilmu pemrograman atau kode yang rumit. '
        'Semuanya semudah mengisi formulir biasa di HP atau laptop, lalu sekali klik simpan, otomatis langsung tayang.”'
    )
    q_r2.font.italic = True
    q_r2.font.color.rgb = RGBColor(0x1e, 29, 59)

    doc.add_paragraph("Langkah-langkah yang dipraktekkan di depan audiens:").runs[0].font.bold = True

    steps = [
        ("1. Cara Masuk ke Halaman Pengelola", "Klik ikon manusia 👤 di pojok kanan atas beranda (atau buka admin.html). Masukkan username 'admin' dan password 'sdnarso8juara', lalu klik Masuk. Tunjukkan Dashboard dengan ringkasan jumlah berita, galeri, pengumuman, dan data PPDB."),
        ("2. Simulasi Menerbitkan Berita Baru (1 Menit)", "Klik tab 'Kelola Berita'. Isi Judul (misal: 'Kegiatan Senam Pagi Bersama Guru dan Murid'), pilih Kategori, tanggal, ketik isi ringkas, dan pilih foto kegiatan. Klik tombol 'Terbitkan Berita'. Buka tab baru di Beranda: buktikan bahwa berita tersebut detik itu juga langsung tayang di paling depan!"),
        ("3. Mengelola Pengumuman Sekolah", "Klik tab 'Kelola Pengumuman'. Masukkan pengumuman libur semester atau jadwal pembagian rapor. Klik Simpan, dan pengumuman seketika muncul untuk dibaca orang tua murid."),
        ("4. Memeriksa Pendaftar Siswa Baru (PPDB)", "Klik tab 'Kelola PPDB'. Tunjukkan tabel pendaftar calon siswa baru lengkap dengan nama anak, NIK, nama wali, alamat, dan nomor kontak WhatsApp. Tunjukkan tombol cetak/ekspor data pendaftar."),
        ("5. Keamanan & Cadangkan Data Sekolah (1 Kali Klik)", "Buka tab 'Pengaturan Sistem'. Tunjukkan bahwa operator bisa mengganti kata sandi kapan saja. Tunjukkan tombol 'Cadangkan Database (.JSON)'. Tekankan bahwa cukup menekan tombol ini sebulan sekali, seluruh data sekolah aman tersimpan di flashdisk dan tidak akan pernah hilang meski komputer rusak.")
    ]
    for s_title, s_desc in steps:
        p = doc.add_paragraph()
        p.add_run(f"{s_title}: ").bold = True
        p.add_run(s_desc)

    # TAHAP 4
    doc.add_paragraph()
    h = doc.add_paragraph()
    r = h.add_run("TAHAP 4: JAMINAN KEAMANAN & KETAHANAN JANGKA PANJANG (± 3 MENIT)")
    r.font.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x03, 0x69, 0xa1)

    pts4 = [
        ("Kunci Otentikasi Ganda", "Halaman admin terkunci rapat. Pengunjung biasa yang mencoba mengetik admin.html tanpa login akan otomatis ditolak dan dikembalikan ke halaman login."),
        ("Penyaring Teks Aman (Anti-XSS & Anti-Spam)", "Seluruh formulir kontak dan pendaftaran PPDB dilengkapi penyaring teks berbahaya dan verifikasi captcha manusia, memastikan website tidak dapat dibobol robot spam atau disusupi skrip perusak."),
        ("Sistem Tiga Lapis Pengaman Data (Multi-Tier Resilience)", "Data sekolah tersimpan di Google Cloud Database Realtime, disinkronkan ke memori penyimpanan lokal browser (LocalStorage), dan memiliki berkas cadangan data_sekolah.json."),
        ("Dapat Digunakan Sepenuhnya Secara Offline", "Jika sewaktu-waktu jaringan internet mati total di Arso VIII, sekolah tetap bisa membuka website secara offline lewat file master di komputer sekolah.")
    ]
    for title, desc in pts4:
        p = doc.add_paragraph()
        p.add_run(f"✔ {title}: ").bold = True
        p.add_run(desc)

    # TAHAP 5
    doc.add_paragraph()
    h = doc.add_paragraph()
    r = h.add_run("TAHAP 5: SERAH TERIMA SIMBOLIS & PENUTUP (± 4 MENIT)")
    r.font.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x03, 0x69, 0xa1)

    quote3 = doc.add_paragraph()
    quote3.paragraph_format.left_indent = Inches(0.4)
    q_r3 = quote3.add_run(
        '“Bapak Kepala Sekolah yang kami hormati, serta seluruh dewan guru dan operator yang kami banggakan.\n\n'
        'Dengan rasa bangga dan ketulusan hati, hari ini saya menyerahkan secara resmi:\n'
        '1. Hak Akses Kelola Penuh Portal Website Resmi SD Negeri Inpres Arso VIII.\n'
        '2. Berkas Paket Master Offline Lengkap (PAKET-WEBSITE-SDN-INPRES-ARSO-8-RESMI.zip) untuk arsip komputer sekolah.\n'
        '3. Buku Petunjuk Teknis Panduan Pengelolaan Sekolah.\n\n'
        'Besar harapan kita semua, website ini akan terus hidup, diperbarui, dan menjadi sarana kemajuan bagi anak-anak generasi penerus bangsa di Arso VIII tercinta.\n\n'
        'Terima kasih atas kepercayaan dan kerjasamanya. Tabea, Salam Sejahtera, Wassalamu’alaikum Warahmatullahi Wabarakatuh.”'
    )
    q_r3.font.italic = True
    q_r3.font.color.rgb = RGBColor(0x1e, 29, 59)

    # Trik Tambahan
    doc.add_paragraph()
    h = doc.add_paragraph()
    r = h.add_run("TIPS TAMBAHAN: MEMBUAT PINTASAN APLIKASI DI HP GURU & WALI MURID")
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0x02, 0x84, 0xc7)

    p_app = doc.add_paragraph()
    p_app.add_run(
        "Ajak audiens membuka Chrome di HP masing-masing:\n"
        "1. Ketik: sdninpresarso8.sch.id\n"
        "2. Klik titik tiga (⋮) di pojok kanan atas Chrome -> pilih 'Tambahkan ke Layar Utama' (Add to Home screen).\n"
        "3. Klik Tambahkan. Seketika Logo Sekolah SDN Inpres Arso VIII akan muncul di layar HP mereka layaknya aplikasi resmi!"
    )

    # Tanda Tangan Serah Terima
    doc.add_paragraph()
    doc.add_paragraph("―" * 55).alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("BERITA ACARA SERAH TERIMA SIMBOLIS").runs[0].font.bold = True
    doc.add_paragraph(f"Pada hari ini, Senin tanggal 16 November 2026, telah diserahterimakan pengelolaan Website Resmi SD Negeri Inpres Arso VIII:")

    sig_table = doc.add_table(rows=3, cols=2)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    sig_table.rows[0].cells[0].paragraphs[0].text = "Yang Menyerahkan (Presenter / Pengembang):"
    sig_table.rows[0].cells[1].paragraphs[0].text = "Yang Menerima (Kepala Sekolah):"
    sig_table.rows[1].cells[0].paragraphs[0].text = "\n\n\n_________________________\n( ......................................... )"
    sig_table.rows[1].cells[1].paragraphs[0].text = "\n\n\n_________________________\n( ADI PUSPITO, S.Pd )\nNIP. 196805291993121002"
    sig_table.rows[2].cells[0].paragraphs[0].text = "Mengetahui / Saksi:\nOperator Sekolah\n\n\n_________________________\n( ......................................... )"
    sig_table.rows[2].cells[1].paragraphs[0].text = "Mengetahui / Saksi:\nPerwakilan Dewan Guru\n\n\n_________________________\n( ......................................... )"

    doc.save(filename)
    print(f"Document saved successfully at: {filename}")

if __name__ == "__main__":
    out_docx_ws = r"c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\BAHAN_PRESENTASI_DAN_PANDUAN_SERAH_TERIMA_SDN_ARSO_8.docx"
    create_docx(out_docx_ws)
    out_docx_dl = r"c:\Users\acer\Downloads\BAHAN_PRESENTASI_DAN_PANDUAN_SERAH_TERIMA_SDN_ARSO_8.docx"
    shutil.copyfile(out_docx_ws, out_docx_dl)
    print("Copied to Downloads folder!")
