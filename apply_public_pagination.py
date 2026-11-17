import re

print("=== 1. Updating berita.html ===")
with open("berita.html", "r", encoding="utf-8") as f:
    berita_html = f.read()

target_berita_grid = '<div class="news-grid" id="beritaListGrid">'
filter_berita_block = """            <!-- PENCARIAN & FILTER KATEGORI BERITA RESMI -->
            <div class="table-filter-bar" style="background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 24px;">
                <div class="table-filter-search" style="min-width: 260px;">
                    <span style="font-size: 16px;">🔍</span>
                    <input type="text" id="publicBeritaSearchInput" placeholder="Ketik untuk mencari berita, topik, atau kata kunci..." oninput="window.filterPublicNews()">
                </div>
                <div class="table-filter-actions">
                    <span style="font-size: 12.5px; color: #64748b; font-weight: 600;">Kategori:</span>
                    <select id="publicBeritaCategorySelect" class="table-filter-select" onchange="window.filterPublicNews()">
                        <option value="ALL">Semua Kategori</option>
                        <option value="Kegiatan">Kegiatan & Berita</option>
                        <option value="Akademik">Akademik & ANBK</option>
                        <option value="Kesiswaan">Kesiswaan & Pramuka</option>
                        <option value="Prestasi">Prestasi & Seni</option>
                    </select>
                </div>
            </div>

            <div class="news-grid" id="beritaListGrid">"""

pagination_berita_block = """            </div>

            <!-- PAGINASI BERITA PUBLIK (ARSIP AMAN TANPA HAPUS) -->
            <div id="publicBeritaPagination" class="pagination-container" style="margin-top: 30px;"></div>"""

if target_berita_grid in berita_html and "publicBeritaSearchInput" not in berita_html:
    berita_html = berita_html.replace(target_berita_grid, filter_berita_block)
    # find closing div of news-grid
    pos_grid = berita_html.find('id="beritaListGrid"')
    pos_grid_close = berita_html.find('</div>\n\n        </div>\n    </section>', pos_grid)
    if pos_grid_close != -1:
        berita_html = berita_html[:pos_grid_close] + pagination_berita_block + berita_html[pos_grid_close+6:]
    with open("berita.html", "w", encoding="utf-8") as f:
        f.write(berita_html)
    print("✔ berita.html updated with filter & pagination container!")
else:
    print("berita.html already updated or target not found.")

print("\n=== 2. Updating galeri.html ===")
with open("galeri.html", "r", encoding="utf-8") as f:
    galeri_html = f.read()

target_galeri_grid = '<div class="gallery-grid">'
filter_galeri_block = """            <!-- PENCARIAN & FILTER KATEGORI GALERI FOTO -->
            <div class="table-filter-bar" style="background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 24px;">
                <div class="table-filter-search" style="min-width: 260px;">
                    <span style="font-size: 16px;">🔍</span>
                    <input type="text" id="publicGaleriSearchInput" placeholder="Ketik kata kunci untuk mencari foto kegiatan..." oninput="window.filterPublicGallery()">
                </div>
                <div class="table-filter-actions">
                    <span style="font-size: 12.5px; color: #64748b; font-weight: 600;">Kategori:</span>
                    <select id="publicGaleriCategorySelect" class="table-filter-select" onchange="window.filterPublicGallery()">
                        <option value="ALL">Semua Foto Dokumentasi</option>
                        <option value="KEGIATAN">Kegiatan Sekolah</option>
                        <option value="AKADEMIK">Akademik & ANBK</option>
                        <option value="PRAMUKA">Pramuka & Budaya</option>
                        <option value="OLAHRAGA">Olahraga & Kesehatan</option>
                        <option value="KEROHANIAN">Kerohanian & Karakter</option>
                        <option value="FASILITAS">Fasilitas & Dewan Guru</option>
                    </select>
                </div>
            </div>

            <div class="gallery-grid">"""

pagination_galeri_block = """            </div>

            <!-- PAGINASI GALERI PUBLIK (ARSIP AMAN TANPA HAPUS) -->
            <div id="publicGaleriPagination" class="pagination-container" style="margin-top: 30px;"></div>"""

if target_galeri_grid in galeri_html and "publicGaleriSearchInput" not in galeri_html:
    galeri_html = galeri_html.replace(target_galeri_grid, filter_galeri_block)
    pos_gal = galeri_html.find('class="gallery-grid"')
    pos_gal_close = galeri_html.find('</div>\n\n        </div>\n    </section>', pos_gal)
    if pos_gal_close != -1:
        galeri_html = galeri_html[:pos_gal_close] + pagination_galeri_block + galeri_html[pos_gal_close+6:]
    with open("galeri.html", "w", encoding="utf-8") as f:
        f.write(galeri_html)
    print("✔ galeri.html updated with filter & pagination container!")
else:
    print("galeri.html already updated or target not found.")

print("\n=== 3. Updating pengembangan-guru.html ===")
with open("pengembangan-guru.html", "r", encoding="utf-8") as f:
    kkg_html = f.read()

target_kkg_table = '<div class="data-table-wrapper"'
filter_kkg_block = """                <!-- PENCARIAN & FILTER JADWAL KKG -->
                <div class="table-filter-bar" style="background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 16px;">
                    <div class="table-filter-search" style="min-width: 280px;">
                        <span style="font-size: 16px;">🔍</span>
                        <input type="text" id="publicKKGSearchInput" placeholder="Ketik pencarian: materi, pemateri (Turut, S.Pd), atau sekolah..." oninput="window.filterPublicKKG()">
                    </div>
                    <div class="table-filter-actions">
                        <select id="publicKKGFilterKelompok" class="table-filter-select" onchange="window.filterPublicKKG()">
                            <option value="ALL">Semua Sasaran Kelompok</option>
                            <option value="Kelas Awal">Kelas 1, 2, 3 & Agama (Kelas Awal)</option>
                            <option value="Kelas Tinggi">Kelas 4, 5, 6, PJOK, Seni, Inggris (Kelas Tinggi)</option>
                        </select>
                        <select id="publicKKGFilterStatus" class="table-filter-select" onchange="window.filterPublicKKG()">
                            <option value="ALL">Semua Status</option>
                            <option value="Terlaksana">Terlaksana</option>
                            <option value="Dijadwalkan">Dijadwalkan</option>
                        </select>
                    </div>
                </div>

                <div class="data-table-wrapper" """

pagination_kkg_block = """</table>
                </div>

                <!-- PAGINASI JADWAL KKG PUBLIK (ARSIP AMAN TANPA HAPUS) -->
                <div id="publicKKGPagination" class="pagination-container" style="margin-top: 18px;"></div>"""

if target_kkg_table in kkg_html and "publicKKGSearchInput" not in kkg_html:
    kkg_html = kkg_html.replace(target_kkg_table, filter_kkg_block)
    pos_table_end = kkg_html.find('</table>\n                </div>')
    if pos_table_end != -1:
        kkg_html = kkg_html[:pos_table_end] + pagination_kkg_block + kkg_html[pos_table_end+23:]
    with open("pengembangan-guru.html", "w", encoding="utf-8") as f:
        f.write(kkg_html)
    print("✔ pengembangan-guru.html updated with filter & pagination container!")
else:
    print("pengembangan-guru.html already updated or target not found.")

print("\n=== 4. Updating kolaborasi.html ===")
with open("kolaborasi.html", "r", encoding="utf-8") as f:
    kolab_html = f.read()

target_kolab = '<div id="kolaborasiListContainer"'
filter_kolab_block = """            <!-- PENCARIAN MITRA KOLABORASI -->
            <div class="table-filter-bar" style="background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 24px;">
                <div class="table-filter-search">
                    <span style="font-size: 16px;">🔍</span>
                    <input type="text" id="publicMitraSearchInput" placeholder="Cari nama instansi mitra, pilar kerjasama, atau program kemitraan..." oninput="window.filterPublicMitra()">
                </div>
            </div>

            <div id="kolaborasiListContainer" """

if target_kolab in kolab_html and "publicMitraSearchInput" not in kolab_html:
    kolab_html = kolab_html.replace(target_kolab, filter_kolab_block)
    with open("kolaborasi.html", "w", encoding="utf-8") as f:
        f.write(kolab_html)
    print("✔ kolaborasi.html updated with search filter bar!")
else:
    print("kolaborasi.html already updated or target not found.")
