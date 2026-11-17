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

def create_presentation_docx(filename):
    doc = Document()
    
    # 0.7 inch margins
    for s in doc.sections:
        s.top_margin = Inches(0.7)
        s.bottom_margin = Inches(0.7)
        s.left_margin = Inches(0.7)
        s.right_margin = Inches(0.7)

    # Styles
    doc.styles['Normal'].font.name = 'Calibri'
    doc.styles['Normal'].font.size = Pt(11)
    doc.styles['Normal'].font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Header / Title Box
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_t = title_p.add_run("PANDUAN & NASKAH LENGKAP PRESENTASI RESMI\nWEBSITE SD NEGERI INPRES ARSO VIII")
    run_t.font.name = 'Arial'
    run_t.font.size = Pt(17)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(0x0f, 0x17, 0x2a)

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run("Disusun untuk Presenter / Pembawa Materi di Depan Kepala Sekolah, Dewan Guru, & Operator\nKampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua | Domain: https://sdninpresarso8.sch.id")
    run_sub.font.size = Pt(9.5)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(0x03, 0x69, 0xa1)

    doc.add_paragraph("―" * 58).alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Quick Info Box
    table = doc.add_table(rows=4, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_data = [
        ("Alamat Website Publik", "https://sdninpresarso8.sch.id (Alternatif: https://sdninpresarso8.surge.sh)"),
        ("Pintu Masuk Admin CMS", "https://sdninpresarso8.sch.id/admin.html (atau klik ikon 👤 di pojok kanan atas)"),
        ("Kredensial Login Resmi", "Nama Pengguna: admin   |   Kata Sandi: sdnarso8juara"),
        ("Alokasi Waktu Ideal", "20 – 30 Menit (Fleksibel disesuaikan dengan sesi tanya jawab)")
    ]
    for idx, (label, val) in enumerate(info_data):
        row = table.rows[idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(4.7)
        c0.text, c1.text = label, val
        c0.paragraphs[0].runs[0].font.bold = True
        set_cell_background(c0, "F1F5F9")
        set_cell_background(c1, "F8FAFC")

    doc.add_paragraph()

    # TAHAP 1
    h = doc.add_paragraph()
    r = h.add_run("TAHAP 1: PEMBUKAAN & LATAR BELAKANG (Durasi: ± 3 Menit)")
    r.font.bold = True
    r.font.size = Pt(12.5)
    r.font.color.rgb = RGBColor(0x16, 0x65, 0x34) # Green 800

    quote1 = doc.add_paragraph()
    quote1.paragraph_format.left_indent = Inches(0.3)
    q_r = quote1.add_run(
        '“Selamat pagi / siang, Bapak Kepala Sekolah yang saya hormati, Bapak/Ibu dewan guru sekalian, serta rekan Operator Sekolah yang kami banggakan.\n\n'
        'Puji dan syukur kita panjatkan ke hadirat Tuhan Yang Maha Esa. Hari ini merupakan momen yang sangat membanggakan bagi SD Negeri Inpres Arso VIII. '
        'Sekolah kita yang berdiri kokoh di Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, kini telah resmi memiliki Portal Website Sekolah Berbasis Cloud Modern '
        'dengan domain resmi berstandar nasional Indonesia: sdninpresarso8.sch.id.\n\n'
        'Website ini dibangun bukan sekadar pajangan, melainkan sebagai pusat transparansi informasi, media publikasi prestasi anak-anak didik kita, sarana PPDB online, '
        'serta bukti nyata bahwa sekolah kita di perbatasan Papua mampu berdiri sejajar dengan sekolah-sekolah unggulan di kota besar.\n\n'
        'Mari kita saksikan bersama tampilan dan kemudahan cara mengelolanya.”'
    )
    q_r.font.italic = True
    q_r.font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)

    # TAHAP 2
    doc.add_paragraph()
    h = doc.add_paragraph()
    r = h.add_run("TAHAP 2: MENGENAL TAMPILAN & FITUR UTAMA (Durasi: ± 7 Menit)")
    r.font.bold = True
    r.font.size = Pt(12.5)
    r.font.color.rgb = RGBColor(0x03, 0x69, 0xa1)

    pts2 = [
        ("Header Atas & Gapura Kehormatan", "Tunjukkan Logo Kabupaten Keerom di kiri atas, Jam Digital Presisi di kanan atas, dan tombol Login Admin berbentuk ikon user elegan. Perlihatkan foto Gapura Kehormatan yang utuh dan animasi sambutan bertahap (Selamat Datang -> Portal Resmi Kampung Dukwia -> SDN Inpres Arso VIII)."),
        ("Slider Sorotan Info Kabar Terkini", "Tunjukkan berita sekolah yang bergulir otomatis setiap 4.5 detik. Tekankan: 'Bapak/Ibu, slider ini pintar, otomatis membatasi maksimal 6 berita terbaru sehingga titik navigasi di HP siapapun tidak akan bertumpuk atau berantakan.'"),
        ("Profil Sekolah & Struktur Organisasi", "Buka menu Profil: perlihatkan sejarah sekolah, visi-misi unggul IPTEK & berakhlak mulia, serta bagan struktur organisasi interaktif."),
        ("Dewan Guru & Sarana Prasarana", "Tunjukkan profil 12 pendidik lengkap dengan NIP dan mata pelajaran. Tunjukkan pula inventaris 6 ruang kelas, perpustakaan, toilet sanitasi, dan koneksi internet satelit Starlink & Telkomsel Orbit."),
        ("K3S & KKG Gugus 1 Arso Barat", "Klik menu 'Pengembangan Guru': tunjukkan dokumentasi foto pertemuan bergilir KKG dan tabel agenda resmi Gugus 1 Arso Barat."),
        ("Mitra, Galeri & PPDB Online", "Perlihatkan 6 pilar kolaborasi serta formulir pendaftaran PPDB online yang memudahkan orang tua mendaftar langsung lewat HP.")
    ]
    for title, desc in pts2:
        p = doc.add_paragraph()
        p.add_run(f"• {title}: ").bold = True
        p.add_run(desc)

    # TAHAP 3
    doc.add_paragraph()
    h = doc.add_paragraph()
    r = h.add_run("TAHAP 3: DEMO LANGSUNG CARA PENGELOLAAN OLEH OPERATOR (CMS ADMIN) (Durasi: ± 10 Menit)")
    r.font.bold = True
    r.font.size = Pt(12.5)
    r.font.color.rgb = RGBColor(0x16, 0x65, 0x34)

    quote2 = doc.add_paragraph()
    quote2.paragraph_format.left_indent = Inches(0.3)
    q_r2 = quote2.add_run(
        '“Bapak Kepala Sekolah dan rekan Operator, sistem pengelola website ini dirancang sangat ramah pengguna (user-friendly). '
        'Operator atau guru tidak perlu menguasai bahasa pemrograman yang rumit. '
        'Semuanya semudah mengisi formulir biasa di HP atau laptop, lalu sekali klik simpan, otomatis langsung tayang.”'
    )
    q_r2.font.italic = True
    q_r2.font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)

    steps = [
        ("1. Cara Masuk ke Halaman Pengelola", "Klik ikon manusia 👤 di pojok kanan atas beranda (atau buka admin.html). Masukkan username 'admin' dan password 'sdnarso8juara', lalu klik Masuk. Tunjukkan Dashboard dengan ringkasan jumlah berita, galeri, pengumuman, dan data PPDB."),
        ("2. Simulasi Menerbitkan Berita Baru (1 Menit)", "Klik tab 'Kelola Berita'. Isi Judul (misal: 'Pemeriksaan Kesehatan Berkala Bersama Puskesmas'), pilih Kategori, tanggal, ketik isi ringkas, dan pilih foto. Klik tombol 'Terbitkan Berita'. Buka tab baru di Beranda: buktikan bahwa berita tersebut detik itu juga langsung tayang di baris terdepan!"),
        ("3. Mengelola Pengumuman Sekolah", "Klik tab 'Kelola Pengumuman'. Masukkan pengumuman libur semester atau jadwal pembagian rapor. Klik Simpan, pengumuman langsung terbaca di website publik."),
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
    r = h.add_run("TAHAP 4: JAMINAN KEAMANAN & KETAHANAN JANGKA PANJANG (Durasi: ± 3 Menit)")
    r.font.bold = True
    r.font.size = Pt(12.5)
    r.font.color.rgb = RGBColor(0x03, 0x69, 0xa1)

    pts4 = [
        ("Kunci Otentikasi Ganda", "Halaman admin terkunci rapat. Pengunjung biasa yang mencoba mengetik admin.html tanpa login akan otomatis ditolak dan dikembalikan ke halaman login."),
        ("Penyaring Teks Aman (Anti-XSS & Anti-Spam)", "Seluruh formulir kontak dan pendaftaran PPDB dilengkapi penyaring teks berbahaya dan verifikasi captcha manusia, memastikan website tidak dapat disusupi robot spam atau skrip berbahaya."),
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
    r = h.add_run("TAHAP 5: KATA PENUTUP & PENGANTAR SERAH TERIMA (Durasi: ± 4 Menit)")
    r.font.bold = True
    r.font.size = Pt(12.5)
    r.font.color.rgb = RGBColor(0x16, 0x65, 0x34)

    quote3 = doc.add_paragraph()
    quote3.paragraph_format.left_indent = Inches(0.3)
    q_r3 = quote3.add_run(
        '“Bapak Kepala Sekolah yang kami hormati, serta dewan guru dan operator yang kami banggakan.\n\n'
        'Demikianlah pemaparan mengenai sistem website resmi SD Negeri Inpres Arso VIII. '
        'Sebagai bukti penyerahan tanggung jawab teknis dan hak kelola penuh, selanjutnya kita akan menandatangani Lembar Berita Acara Serah Terima Simbolis '
        'beserta penyerahan berkas master paket website untuk arsip resmi sekolah.\n\n'
        'Semoga website ini menjadi jembatan kemajuan dan kebanggaan bagi seluruh masyarakat Kampung Dukwia dan Kabupaten Keerom.\n'
        'Terima kasih. Tabea, Salam Sejahtera, Wassalamu’alaikum Warahmatullahi Wabarakatuh.”'
    )
    q_r3.font.italic = True
    q_r3.font.color.rgb = RGBColor(0x1e, 0x29, 0x3b)

    # Tips Menjadikan Logo seperti Aplikasi di HP
    doc.add_paragraph()
    h_app = doc.add_paragraph()
    r_app = h_app.add_run("TIPS PRAKTIS: MENJADIKAN WEBSITE SEPERTI APLIKASI DI HP GURU & WALI MURID")
    r_app.font.bold = True
    r_app.font.size = Pt(11)
    r_app.font.color.rgb = RGBColor(0x02, 0x84, 0xc7)

    p_app = doc.add_paragraph()
    p_app.add_run(
        "Ajak audiens mempraktekkan langsung di HP masing-masing:\n"
        "1. Buka Google Chrome di HP, ketik: sdninpresarso8.sch.id\n"
        "2. Klik titik tiga (⋮) di pojok kanan atas Chrome -> pilih 'Tambahkan ke Layar Utama' (Add to Home screen).\n"
        "3. Klik Tambahkan. Seketika Logo Resmi SDN Inpres Arso VIII akan muncul di layar HP mereka layaknya aplikasi Android/iPhone resmi!"
    )

    doc.save(filename)
    print(f"Presentation document saved: {filename}")


def create_berita_acara_docx(filename):
    doc = Document()
    
    # 0.6 inch margins to ensure it fits perfectly on 1 standard A4 page!
    for s in doc.sections:
        s.top_margin = Inches(0.5)
        s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.7)
        s.right_margin = Inches(0.7)

    # Styles
    doc.styles['Normal'].font.name = 'Arial'
    doc.styles['Normal'].font.size = Pt(10)
    doc.styles['Normal'].font.color.rgb = RGBColor(0, 0, 0)

    # KOP SURAT RESMI
    p_kop1 = doc.add_paragraph()
    p_kop1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kop1.paragraph_format.space_after = Pt(1)
    r1 = p_kop1.add_run("PEMERINTAH KABUPATEN KEEROM\nDINAS PENDIDIKAN DAN KEBUDAYAAN\n")
    r1.font.size = Pt(12)
    r1.font.bold = True

    p_kop2 = doc.add_paragraph()
    p_kop2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kop2.paragraph_format.space_after = Pt(2)
    r2 = p_kop2.add_run("SD NEGERI INPRES ARSO VIII")
    r2.font.size = Pt(14)
    r2.font.bold = True

    p_kop3 = doc.add_paragraph()
    p_kop3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_kop3.paragraph_format.space_after = Pt(4)
    r3 = p_kop3.add_run("Alamat: Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua - Kode Pos 99368\nNPSN: 60300958 | NSS: 101250302008 | Akreditasi: A (Amat Baik)\nLaman Resmi: https://sdninpresarso8.sch.id | Pos-el: info@sdninpresarso8.sch.id")
    r3.font.size = Pt(8.5)
    r3.font.italic = True

    # Garis Pembatas Kop Surat
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_after = Pt(10)
    p_line.add_run("━" * 68).font.bold = True

    # JUDUL SURAT
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(2)
    r_t = p_title.add_run("BERITA ACARA SERAH TERIMA PENGELOLAAN SISTEM WEBSITE RESMI")
    r_t.font.size = Pt(11.5)
    r_t.font.bold = True
    r_t.font.underline = True

    p_nomor = doc.add_paragraph()
    p_nomor.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_nomor.paragraph_format.space_after = Pt(10)
    r_n = p_nomor.add_run("Nomor : 421.2 / 088 / SDN-A.VIII / XI / 2026")
    r_n.font.size = Pt(10)
    r_n.font.bold = True

    # Pembuka
    p_intro = doc.add_paragraph()
    p_intro.paragraph_format.space_after = Pt(6)
    p_intro.add_run("Pada hari ini, ")
    p_intro.add_run("Senin").bold = True
    p_intro.add_run(" tanggal ")
    p_intro.add_run("Enam Belas").bold = True
    p_intro.add_run(" bulan ")
    p_intro.add_run("November").bold = True
    p_intro.add_run(" tahun ")
    p_intro.add_run("Dua Ribu Dua Puluh Enam (16-11-2026)").bold = True
    p_intro.add_run(", bertempat di SD Negeri Inpres Arso VIII, telah dilakukan serah terima sistem website resmi sekolah oleh dan antara pihak-pihak:")

    # Identitas Pihak (Tabel Ringkas)
    t_pihak = doc.add_table(rows=2, cols=3)
    t_pihak.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Pihak 1
    t_pihak.rows[0].cells[0].width = Inches(0.4)
    t_pihak.rows[0].cells[1].width = Inches(1.8)
    t_pihak.rows[0].cells[2].width = Inches(4.5)
    t_pihak.rows[0].cells[0].paragraphs[0].text = "1."
    t_pihak.rows[0].cells[1].paragraphs[0].text = "Nama / Pihak\nJabatan"
    t_pihak.rows[0].cells[2].paragraphs[0].text = ": PENGEMBANG / DIGITALISATOR SISTEM\n: Pihak Pertama (Yang Menyerahkan)"
    
    # Pihak 2
    t_pihak.rows[1].cells[0].width = Inches(0.4)
    t_pihak.rows[1].cells[1].width = Inches(1.8)
    t_pihak.rows[1].cells[2].width = Inches(4.5)
    t_pihak.rows[1].cells[0].paragraphs[0].text = "2."
    t_pihak.rows[1].cells[1].paragraphs[0].text = "Nama\nNIP / Pangkat\nJabatan"
    t_pihak.rows[1].cells[2].paragraphs[0].text = ": ADI PUSPITO, S.Pd\n: 196805291993121002 / Pembina Utama Muda, IV/c\n: Kepala Sekolah SD Negeri Inpres Arso VIII\n  selaku Pihak Kedua (Yang Menerima)"

    doc.add_paragraph().paragraph_format.space_after = Pt(2)

    # Isi Serah Terima
    p_isi = doc.add_paragraph()
    p_isi.paragraph_format.space_after = Pt(4)
    p_isi.add_run("PIHAK PERTAMA menyerahkan kepada PIHAK KEDUA, dan PIHAK KEDUA menyatakan telah menerima dengan baik, lengkap, dan berfungsi sempurna pengelolaan Website Resmi SD Negeri Inpres Arso VIII yang meliputi:")

    items = [
        "Hak Akses Kelola Penuh (Super Administrator) pada Content Management System (CMS) beralamat di: https://sdninpresarso8.sch.id/admin.html dengan username: 'admin'.",
        "Domain Resmi Nasional Khusus Sekolah: sdninpresarso8.sch.id dan cadangan cloud hosting berkinerja tinggi.",
        "Basis Data Sekolah Terintegrasi meliputi modul Berita, Galeri Foto, Profil Guru/Siswa, Pengumuman, Agenda K3S/KKG Gugus 1, serta Modul PPDB Online.",
        "Berkas Arsip Master Offline Lengkap (PAKET-WEBSITE-SDN-INPRES-ARSO-8-RESMI.zip) untuk dicadangkan pada media penyimpanan laptop/flashdisk sekolah."
    ]
    for idx, itm in enumerate(items):
        p_itm = doc.add_paragraph()
        p_itm.paragraph_format.left_indent = Inches(0.3)
        p_itm.paragraph_format.space_after = Pt(2)
        p_itm.add_run(f"{idx+1}. ").bold = True
        p_itm.add_run(itm)

    # Penutup
    p_close = doc.add_paragraph()
    p_close.paragraph_format.space_after = Pt(12)
    p_close.add_run("Demikian Berita Acara Serah Terima ini dibuat dengan sebenarnya dalam rangkap 2 (dua) bermaterai/berstempel sah, untuk dapat dipergunakan sebagaimana mestinya demi mendukung keterbukaan informasi dan digitalisasi pendidikan di Kabupaten Keerom.")

    # Kolom Tanda Tangan Formal
    t_sig = doc.add_table(rows=2, cols=2)
    t_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    c_p1 = t_sig.rows[0].cells[0]
    c_p2 = t_sig.rows[0].cells[1]
    c_p1.width, c_p2.width = Inches(3.4), Inches(3.4)

    p1_sig = c_p1.paragraphs[0]
    p1_sig.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1_sig.add_run("PIHAK PERTAMA\nYang Menyerahkan,\n\n\n\n\n")
    r_p1_name = p1_sig.add_run("( ___________________________ )\n")
    r_p1_name.bold = True
    p1_sig.add_run("Tim Pengembang / Presenter")

    p2_sig = c_p2.paragraphs[0]
    p2_sig.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2_sig.add_run("PIHAK KEDUA\nYang Menerima,\nKepala SDN Inpres Arso VIII\n\n\n\n")
    r_p2_name = p2_sig.add_run("ADI PUSPITO, S.Pd\n")
    r_p2_name.bold = True
    r_p2_name.underline = True
    p2_sig.add_run("NIP. 196805291993121002")

    # Baris Saksi
    c_s1 = t_sig.rows[1].cells[0]
    c_s2 = t_sig.rows[1].cells[1]
    c_s1.width, c_s2.width = Inches(3.4), Inches(3.4)

    s1_sig = c_s1.paragraphs[0]
    s1_sig.alignment = WD_ALIGN_PARAGRAPH.CENTER
    s1_sig.add_run("\nMengetahui / Saksi I,\nTenaga Operator Sekolah\n\n\n\n")
    s1_sig.add_run("( ___________________________ )\n").bold = True
    s1_sig.add_run("NIP/NRK. -")

    s2_sig = c_s2.paragraphs[0]
    s2_sig.alignment = WD_ALIGN_PARAGRAPH.CENTER
    s2_sig.add_run("\nMengetahui / Saksi II,\nPerwakilan Dewan Guru\n\n\n\n")
    s2_sig.add_run("( ___________________________ )\n").bold = True
    s2_sig.add_run("NIP. -")

    doc.save(filename)
    print(f"Berita Acara document saved: {filename}")

if __name__ == "__main__":
    ws_doc1 = r"c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\1_MATERI_PRESENTASI_WEBSITE_SDN_INPRES_ARSO_8.docx"
    ws_doc2 = r"c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8\2_BERITA_ACARA_SERAH_TERIMA_WEBSITE_SDN_INPRES_ARSO_8.docx"
    
    create_presentation_docx(ws_doc1)
    create_berita_acara_docx(ws_doc2)

    dl_doc1 = r"c:\Users\acer\Downloads\1_MATERI_PRESENTASI_WEBSITE_SDN_INPRES_ARSO_8.docx"
    dl_doc2 = r"c:\Users\acer\Downloads\2_BERITA_ACARA_SERAH_TERIMA_WEBSITE_SDN_INPRES_ARSO_8.docx"
    
    shutil.copyfile(ws_doc1, dl_doc1)
    shutil.copyfile(ws_doc2, dl_doc2)
    print("Both DOCX files created and copied to Downloads!")
