import json

with open('data_sekolah.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

jadwal = db.get('kkg', {}).get('jadwal_pertemuan', [])
items_with_photo = [j for j in jadwal if j.get('foto') and len(j.get('foto').strip()) > 0]
print(f"Items with photo: {len(items_with_photo)}")

category_colors = [
    "#0284c7", # biru
    "#10b981", # hijau
    "#8b5cf6", # ungu
    "#f59e0b", # emas
    "#06b6d4", # cyan
    "#ec4899", # pink
    "#14b8a6"  # teal
]

def generate_kkg_slider_html(items):
    out = []
    out.append('<!-- SHOWCASE CAROUSEL OTOMATIS DOKUMENTASI K3S & KKG -->')
    out.append('<div class="showcase-slider-wrapper" id="kkgShowcaseSliderWrapper" style="margin-bottom: 20px;">')
    out.append('    <!-- Tag Sorotan KKG Otomatis -->')
    out.append('    <div class="showcase-live-badge">')
    out.append('        <span class="showcase-pulse-dot"></span>')
    out.append('        <span>DOKUMENTASI RESMI K3S & KKG GUGUS 1</span>')
    out.append('    </div>')
    out.append('')
    out.append('    <!-- Tombol Navigasi Kiri & Kanan -->')
    out.append('    <button type="button" class="showcase-arrow-btn showcase-prev-btn" id="kkgShowcasePrevBtn" aria-label="Slide Sebelumnya" title="Lihat kegiatan sebelumnya">‹</button>')
    out.append('    <button type="button" class="showcase-arrow-btn showcase-next-btn" id="kkgShowcaseNextBtn" aria-label="Slide Selanjutnya" title="Lihat kegiatan berikutnya">›</button>')
    out.append('')
    out.append('    <!-- Track Slide Kegiatan KKG -->')
    out.append('    <div class="showcase-slider-track" id="kkgShowcaseSliderTrack">')
    
    for i, itm in enumerate(items):
        active_cls = " active" if i == 0 else ""
        color = category_colors[i % len(category_colors)]
        kelompok_badge = (itm.get('kelompok') or 'KEGIATAN GUGUS 1').upper()
        tgl = itm.get('tanggal') or ''
        agenda = itm.get('agenda') or f'Pertemuan KKG #{i+1}'
        tuan_rumah = itm.get('tuan_rumah') or 'SDN Inpres Arso VIII'
        foto = itm.get('foto') or 'images/kegiatan-rapat-dewan-guru.jpg'
        status = itm.get('status') or 'Terlaksana'
        
        out.append(f'        <!-- SLIDE {i+1}: {agenda[:40]} -->')
        out.append(f'        <div class="showcase-slide{active_cls}" data-index="{i}">')
        out.append('            <div class="showcase-slide-image-wrapper">')
        out.append(f'                <img src="{foto}" alt="{agenda}" class="showcase-slide-img" onclick="if(window.openLightboxWith){{ window.openLightboxWith(this.src, \'{agenda} - Tuan Rumah: {tuan_rumah} ({tgl})\'); }}" title="Klik untuk memperbesar foto dokumentasi" decoding="async" loading="lazy">')
        out.append('                <div class="school-photo-caption">')
        out.append('                    <div>')
        out.append(f'                        <span class="showcase-category-pill" style="background: {color}; color: #ffffff;">{kelompok_badge} • {tgl}</span>')
        out.append(f'                        <h3 class="showcase-slide-title">{agenda}</h3>')
        out.append(f'                        <p class="showcase-slide-desc">📍 Tuan Rumah: <strong>{tuan_rumah}</strong> • Status: <strong>{status}</strong> • Kegiatan Resmi Gugus 1 Arso Barat.</p>')
        out.append('                    </div>')
        out.append('                    <div class="showcase-btn-group">')
        out.append(f'                        <button type="button" class="btn-showcase-zoom" onclick="if(window.openLightboxWith){{ window.openLightboxWith(\'{foto}\', \'{agenda} - Tuan Rumah: {tuan_rumah} ({tgl})\'); }}">')
        out.append('                            🔍 Perbesar Foto')
        out.append('                        </button>')
        out.append('                    </div>')
        out.append('                </div>')
        out.append('            </div>')
        out.append('        </div>')
        
    out.append('    </div>')
    out.append('')
    out.append('    <!-- Indikator Titik (Dots) Navigasi Bawah -->')
    out.append('    <div class="showcase-dots-bar" id="kkgShowcaseDotsBar">')
    for i in range(len(items)):
        active_cls = " active" if i == 0 else ""
        out.append(f'        <button type="button" class="showcase-dot{active_cls}" data-index="{i}" aria-label="Slide {i+1}"></button>')
    out.append('    </div>')
    out.append('</div>')
    
    return '\n'.join(out)

generated_html = generate_kkg_slider_html(items_with_photo)
with open('scratch/generated_kkg_slider.html', 'w', encoding='utf-8') as f:
    f.write(generated_html)
print(f"Generated KKG slider HTML! Total length: {len(generated_html)} chars.")
