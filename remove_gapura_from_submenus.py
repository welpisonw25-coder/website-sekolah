import re

# 1. Update profil.html
with open('profil.html', 'r', encoding='utf-8') as f:
    profil_html = f.read()

old_profil_snippet = '''            <!-- DOKUMENTASI RESMI GAPURA UTAMA & KELUARGA BESAR DEWAN GURU -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-bottom: 35px;">
                <!-- FOTO 1: GAPURA KEHORMATAN UTAMA -->
                <div class="school-photo-showcase" style="margin-bottom: 0;">
                    <img src="images/gapura-kehormatan.jpg" alt="Gapura Kehormatan Resmi SD Negeri Inpres Arso VIII" decoding="async" loading="lazy" style="cursor: pointer;" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/gapura-kehormatan.jpg', 'Gapura Kehormatan Resmi SDN Inpres Arso VIII'); }" title="Klik untuk memperbesar foto">
                    <div class="school-photo-caption">
                        <div>
                            <span style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: #0f172a; padding: 4px 14px; border-radius: 9999px; font-size: 11px; font-weight: 900; text-transform: uppercase;">🏛️ PINTU GERBANG UTAMA</span>
                            <h3 style="font-size: 17px; font-weight: 800; margin: 6px 0 2px; color: white;">Gapura Kehormatan SDN Inpres Arso VIII</h3>
                            <p style="font-size: 12.5px; color: #cbd5e1; margin: 0;">Pintu masuk utama resmi di Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, Keerom, Papua.</p>
                        </div>
                    </div>
                </div>

                <!-- FOTO 2: DEWAN GURU & GTK DI DEPAN GAPURA -->
                <div class="school-photo-showcase" style="margin-bottom: 0;">
                    <img src="images/gerbang-sekolah.jpg" alt="Dewan Guru & Tenaga Kependidikan SDN Inpres Arso VIII" decoding="async" loading="lazy" style="cursor: pointer;" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/gerbang-sekolah.jpg', 'Keluarga Besar Dewan Guru & Tenaga Kependidikan SDN Inpres Arso VIII'); }" title="Klik untuk memperbesar foto">
                    <div class="school-photo-caption">
                        <div>
                            <span style="background: var(--secondary); color: white; padding: 4px 14px; border-radius: 9999px; font-size: 11px; font-weight: 800; text-transform: uppercase;">⭐ KELUARGA BESAR SEKOLAH</span>
                            <h3 style="font-size: 17px; font-weight: 800; margin: 6px 0 2px; color: white;">Dewan Guru & Tenaga Kependidikan</h3>
                            <p style="font-size: 12.5px; color: #cbd5e1; margin: 0;">Kepala Sekolah Bapak Adi Puspito, S.Pd bersama 11 tenaga pendidik berdedikasi tinggi di Keerom.</p>
                        </div>
                    </div>
                </div>
            </div>'''

new_profil_snippet = '''            <!-- DOKUMENTASI RESMI KELUARGA BESAR DEWAN GURU -->
            <div style="margin-bottom: 35px;">
                <!-- DOKUMENTASI DEWAN GURU & GTK -->
                <div class="school-photo-showcase" style="margin-bottom: 0;">
                    <img src="images/gerbang-sekolah.jpg" alt="Dewan Guru & Tenaga Kependidikan SDN Inpres Arso VIII" decoding="async" loading="lazy" style="cursor: pointer;" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/gerbang-sekolah.jpg', 'Keluarga Besar Dewan Guru & Tenaga Kependidikan SDN Inpres Arso VIII'); }" title="Klik untuk memperbesar foto">
                    <div class="school-photo-caption">
                        <div>
                            <span style="background: var(--secondary); color: white; padding: 4px 14px; border-radius: 9999px; font-size: 11px; font-weight: 800; text-transform: uppercase;">⭐ KELUARGA BESAR SEKOLAH</span>
                            <h3 style="font-size: 18px; font-weight: 800; margin: 6px 0 2px; color: white;">Dewan Guru & Tenaga Kependidikan SDN Inpres Arso VIII</h3>
                            <p style="font-size: 13px; color: #cbd5e1; margin: 0;">Kepala Sekolah Bapak Adi Puspito, S.Pd bersama 11 tenaga pendidik berdedikasi tinggi di Kampung Dukwia, Distrik Arso Barat, Keerom, Papua.</p>
                        </div>
                    </div>
                </div>
            </div>'''

assert old_profil_snippet in profil_html, 'old_profil_snippet not found in profil.html'
profil_html = profil_html.replace(old_profil_snippet, new_profil_snippet, 1)

with open('profil.html', 'w', encoding='utf-8') as f:
    f.write(profil_html)
print('[OK] profil.html updated (standalone gapura photo removed)')

# 2. Update galeri.html
with open('galeri.html', 'r', encoding='utf-8') as f:
    galeri_html = f.read()

old_galeri_item = '''                <div class="gallery-item">
                    <img src="images/gapura-kehormatan.jpg" alt="Gapura Kehormatan SDN Inpres Arso VIII - Pintu Masuk Resmi" decoding="async" loading="lazy">
                    <div class="gallery-overlay">
                        <div class="gallery-cat">GAPURA & IDENTITAS RESMI</div>
                        <div class="gallery-title">Gapura Kehormatan SDN Inpres Arso VIII (Pintu Masuk Utama)</div>
                    </div>
                </div>\n\n'''

assert old_galeri_item in galeri_html, 'old_galeri_item not found in galeri.html'
galeri_html = galeri_html.replace(old_galeri_item, '', 1)

with open('galeri.html', 'w', encoding='utf-8') as f:
    f.write(galeri_html)
print('[OK] galeri.html updated (standalone gapura item removed)')

# 3. Update js/admin.js
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

old_admin_gapura = '''const defaultGaleri = [
    {
        id: "gapura_kehormatan",
        judul: "Gapura Kehormatan SDN Inpres Arso VIII (Pintu Masuk Utama)",
        kategori: "Gapura & Identitas",
        src: "images/gapura-kehormatan.jpg"
    },'''

new_admin_gapura = '''const defaultGaleri = ['''

assert old_admin_gapura in admin_js, 'old_admin_gapura not found in js/admin.js'
admin_js = admin_js.replace(old_admin_gapura, new_admin_gapura, 1)

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(admin_js)
print('[OK] js/admin.js updated (gapura_kehormatan removed from defaultGaleri)')

print('\nALL GAPURA SUBMENU REMOVAL COMPLETED!')
