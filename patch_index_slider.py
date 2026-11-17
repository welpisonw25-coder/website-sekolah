# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

track_start = html.find('<div class="showcase-slider-track" id="showcaseSliderTrack">')
section_end = html.find('</div>\n        </div>\n    </section>', track_start)
if section_end == -1:
    section_end = html.find('</div>\r\n        </div>\r\n    </section>', track_start)
if section_end == -1:
    # Look for </section>
    sec = html.find('</section>', track_start)
    section_end = html.rfind('</div>', track_start, sec)
    section_end = html.rfind('</div>', track_start, section_end) + len('</div>')

print("Slice end found at:", section_end)

new_track_and_dots = '''<div class="showcase-slider-track" id="showcaseSliderTrack">
                    <!-- SLIDE 1: TEKNOLOGI & SIMULASI ANBK DENGAN STARLINK -->
                    <div class="showcase-slide active" data-index="0">
                        <div class="showcase-slide-image-wrapper">
                            <img src="images/kegiatan-anbk-komputer.jpg" alt="Pemanfaatan Jaringan Starlink untuk Simulasi ANBK & Pembelajaran Komputer" class="showcase-slide-img" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/kegiatan-anbk-komputer.jpg', 'Simulasi ANBK & Pembelajaran Komputer Berbasis Internet Starlink'); }" title="Klik untuk memperbesar foto berita" decoding="async">
                        </div>
                        <div class="school-photo-caption">
                            <div>
                                <span class="showcase-category-pill" style="background: #0284c7; color: white;">🛰️ TEKNOLOGI & SIMULASI ANBK</span>
                                <h3 class="showcase-slide-title">Pemanfaatan Jaringan Starlink untuk Simulasi ANBK & Pembelajaran Komputer</h3>
                                <p class="showcase-slide-desc">Siswa kelas tinggi SDN Inpres Arso VIII aktif mengikuti simulasi ANBK dan pembelajaran digital berbasis internet satelit kecepatan tinggi di laboratorium TIK.</p>
                            </div>
                            <div class="showcase-btn-group">
                                <button type="button" class="btn btn-showcase-zoom" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/kegiatan-anbk-komputer.jpg', 'Simulasi ANBK & Pembelajaran Komputer Berbasis Internet Starlink'); }">🔍 Perbesar Foto</button>
                                <a href="berita.html" class="btn btn-showcase-action">Baca Berita Lengkap →</a>
                            </div>
                        </div>
                    </div>

                    <!-- SLIDE 2: SENAM KEBUGARAN JASMANI -->
                    <div class="showcase-slide" data-index="1">
                        <div class="showcase-slide-image-wrapper">
                            <img src="images/kegiatan-senam-bersama.jpg" alt="Semarak Senam Kebugaran Jasmani dan Olahraga Bersama Seluruh Siswa & Guru" class="showcase-slide-img" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/kegiatan-senam-bersama.jpg', 'Senam Pagi Kebugaran Jasmani Bersama Siswa & Dewan Guru'); }" title="Klik untuk memperbesar foto berita" decoding="async" loading="lazy">
                        </div>
                        <div class="school-photo-caption">
                            <div>
                                <span class="showcase-category-pill" style="background: #16a34a; color: white;">🏃 KESEHATAN & SENAM BERSAMA</span>
                                <h3 class="showcase-slide-title">Semarak Senam Kebugaran Jasmani dan Olahraga Bersama Siswa & Guru</h3>
                                <p class="showcase-slide-desc">Menjaga kebugaran jasmani dan membina kekompakan warga sekolah, seluruh siswa Kelas I–VI bersama guru rutin melaksanakan senam pagi bersama di halaman sekolah.</p>
                            </div>
                            <div class="showcase-btn-group">
                                <button type="button" class="btn btn-showcase-zoom" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/kegiatan-senam-bersama.jpg', 'Senam Pagi Kebugaran Jasmani Bersama Siswa & Dewan Guru'); }">🔍 Perbesar Foto</button>
                                <a href="berita.html" class="btn btn-showcase-action">Baca Berita Lengkap →</a>
                            </div>
                        </div>
                    </div>

                    <!-- SLIDE 3: PRAMUKA & SENI BUDAYA NUSANTARA -->
                    <div class="showcase-slide" data-index="2">
                        <div class="showcase-slide-image-wrapper">
                            <img src="images/kegiatan-pramuka-budaya.jpg" alt="Prestasi dan Semangat Siswa Gugus Depan 08-013 Pramuka SDN Inpres Arso VIII" class="showcase-slide-img" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/kegiatan-pramuka-budaya.jpg', 'Pramuka Gudep 08-013 SDN Inpres Arso VIII Berbusana Adat Papua & Nusantara'); }" title="Klik untuk memperbesar foto berita" decoding="async" loading="lazy">
                        </div>
                        <div class="school-photo-caption">
                            <div>
                                <span class="showcase-category-pill" style="background: #d97706; color: white;">🏕️ PRAMUKA & SENI BUDAYA</span>
                                <h3 class="showcase-slide-title">Prestasi dan Semangat Siswa Gudep 08-013 Pramuka Berbusana Adat Papua</h3>
                                <p class="showcase-slide-desc">Mengenakan busana adat khas Papua dan pakaian adat Nusantara, anggota Pramuka SDN Inpres Arso VIII tampil memukau dalam kegiatan perkemahan serta pentas seni daerah.</p>
                            </div>
                            <div class="showcase-btn-group">
                                <button type="button" class="btn btn-showcase-zoom" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/kegiatan-pramuka-budaya.jpg', 'Pramuka Gudep 08-013 SDN Inpres Arso VIII Berbusana Adat Papua & Nusantara'); }">🔍 Perbesar Foto</button>
                                <a href="berita.html" class="btn btn-showcase-action">Baca Berita Lengkap →</a>
                            </div>
                        </div>
                    </div>

                    <!-- SLIDE 4: PEMBINAAN ROHANI & KERUKUNAN LINTAS AGAMA -->
                    <div class="showcase-slide" data-index="3">
                        <div class="showcase-slide-image-wrapper">
                            <img src="images/kegiatan-keagamaan-rohani.jpg" alt="Pembinaan Rohani dan Peringatan Hari Besar Keagamaan Siswa" class="showcase-slide-img" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/kegiatan-keagamaan-rohani.jpg', 'Pembinaan Rohani dan Kerukunan Siswa Lintas Agama'); }" title="Klik untuk memperbesar foto berita" decoding="async" loading="lazy">
                        </div>
                        <div class="school-photo-caption">
                            <div>
                                <span class="showcase-category-pill" style="background: #8b5cf6; color: white;">🕊️ KARAKTER & BUDI PEKERTI</span>
                                <h3 class="showcase-slide-title">Pembinaan Rohani dan Kerukunan Siswa Lintas Agama</h3>
                                <p class="showcase-slide-desc">Menjunjung tinggi toleransi dan keberagaman di Tanah Papua, sekolah membina keimanan siswa melalui bimbingan keagamaan Islam, Kristen Protestan, dan Katolik secara intensif.</p>
                            </div>
                            <div class="showcase-btn-group">
                                <button type="button" class="btn btn-showcase-zoom" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/kegiatan-keagamaan-rohani.jpg', 'Pembinaan Rohani dan Kerukunan Siswa Lintas Agama'); }">🔍 Perbesar Foto</button>
                                <a href="berita.html" class="btn btn-showcase-action">Baca Berita Lengkap →</a>
                            </div>
                        </div>
                    </div>

                    <!-- SLIDE 5: RAPAT KOORDINASI & MUTU BELAJAR -->
                    <div class="showcase-slide" data-index="4">
                        <div class="showcase-slide-image-wrapper">
                            <img src="images/gerbang-sekolah.jpg" alt="Rapat Koordinasi Dewan Guru & Kepala Sekolah Tingkatkan Kualitas Belajar" class="showcase-slide-img" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/gerbang-sekolah.jpg', 'Rapat Koordinasi Dewan Guru SDN Inpres Arso VIII'); }" title="Klik untuk memperbesar foto berita" decoding="async" loading="lazy">
                        </div>
                        <div class="school-photo-caption">
                            <div>
                                <span class="showcase-category-pill" style="background: #ea580c; color: white;">📚 MUTU PENDIDIKAN</span>
                                <h3 class="showcase-slide-title">Rapat Koordinasi Dewan Guru & Kepala Sekolah Tingkatkan Kualitas Belajar</h3>
                                <p class="showcase-slide-desc">Peningkatan mutu pembelajaran berbasis Kurikulum Merdeka terus dimatangkan melalui musyawarah rutin dewan guru bersama Kepala Sekolah.</p>
                            </div>
                            <div class="showcase-btn-group">
                                <button type="button" class="btn btn-showcase-zoom" onclick="if(window.openLightboxWith){ window.openLightboxWith('images/gerbang-sekolah.jpg', 'Rapat Koordinasi Dewan Guru SDN Inpres Arso VIII'); }">🔍 Perbesar Foto</button>
                                <a href="berita.html" class="btn btn-showcase-action">Baca Berita Lengkap →</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Indikator Titik (Dots Navigation 5 Berita) -->
                <div class="showcase-dots-bar" id="showcaseDotsBar">
                    <button type="button" class="showcase-dot active" data-index="0" aria-label="Slide 1: Simulasi ANBK & Starlink"></button>
                    <button type="button" class="showcase-dot" data-index="1" aria-label="Slide 2: Senam Kebugaran Jasmani"></button>
                    <button type="button" class="showcase-dot" data-index="2" aria-label="Slide 3: Pramuka Gudep 08-013"></button>
                    <button type="button" class="showcase-dot" data-index="3" aria-label="Slide 4: Pembinaan Rohani"></button>
                    <button type="button" class="showcase-dot" data-index="4" aria-label="Slide 5: Rapat Koordinasi Dewan Guru"></button>
                </div>'''

# Let's inspect exact target in index.html
dots_end = html.find('</div>\n            </div>\n        </div>\n    </section>', track_start)
if dots_end == -1:
    dots_end = html.find('</div>\r\n            </div>\r\n        </div>\r\n    </section>', track_start)

print("Exact dots_end:", dots_end)
old_slice = html[track_start:dots_end]
print("Old slice length:", len(old_slice))

html = html[:track_start] + new_track_and_dots + html[dots_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully replaced static slider in index.html!")
