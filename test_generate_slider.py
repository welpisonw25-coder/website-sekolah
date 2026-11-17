import json

with open('scratch/extracted_kolaborasi.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

border_colors = ['#0284c7', '#10b981', '#f59e0b', '#8b5cf6', '#ef4444', '#14b8a6']
badge_colors = [
    {'bg': '#e0f2fe', 'color': '#0369a1'},
    {'bg': '#d1fae5', 'color': '#065f46'},
    {'bg': '#fef3c7', 'color': '#92400e'},
    {'bg': '#ede9fe', 'color': '#5b21b6'},
    {'bg': '#fee2e2', 'color': '#991b1b'},
    {'bg': '#ccfbf1', 'color': '#115e59'}
]

short_tab_names = [
    "1. Guru-Guru",
    "2. Guru-Siswa",
    "3. Komite",
    "4. Paguyuban",
    "5. Puskesmas",
    "6. Kampung Adat"
]

def generate_slider_html(items):
    out = []
    out.append('<!-- INTERACTIVE SLIDER KEMITRAAN & KOLABORASI -->')
    out.append('<div class="mitra-slider-container" id="mitraSliderWrapper">')
    
    # Topbar controls
    out.append('    <div class="mitra-slider-topbar">')
    out.append('        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">')
    out.append('            <span style="background: #0284c7; color: #ffffff; font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 999px; letter-spacing: 0.5px;">🤝 SHOWCASE PROGRAM KEMITRAAN</span>')
    out.append('            <span id="mitraSlideCounter" style="font-size: 13px; font-weight: 700; color: #475569;">Pilar 1 dari 6</span>')
    out.append('        </div>')
    out.append('        <div style="display: flex; align-items: center; gap: 8px;">')
    out.append('            <button type="button" class="mitra-nav-btn" id="mitraPrevBtn" title="Pilar Sebelumnya" aria-label="Sebelumnya">❮</button>')
    out.append('            <button type="button" class="mitra-nav-btn" id="mitraNextBtn" title="Pilar Berikutnya" aria-label="Berikutnya">❯</button>')
    out.append('        </div>')
    out.append('    </div>')
    
    # Quick-jump tabs bar
    out.append('    <div class="mitra-tabs-nav" id="mitraTabsNav">')
    for i, itm in enumerate(items):
        active_cls = ' active' if i == 0 else ''
        out.append(f'        <button type="button" class="mitra-tab-btn{active_cls}" data-index="{i}" onclick="window.goToMitraSlide({i})">')
        out.append(f'            <span>{itm["icon"]}</span> <span>{short_tab_names[i]}</span>')
        out.append('        </button>')
    out.append('    </div>')
    
    # Slider viewport
    out.append('    <div class="mitra-slider-viewport" id="mitraSliderViewport">')
    
    for i, itm in enumerate(items):
        color = border_colors[i % len(border_colors)]
        badge = badge_colors[i % len(badge_colors)]
        active_cls = ' active' if i == 0 else ''
        
        out.append(f'        <!-- SLIDE {i+1}: {itm["title"]} -->')
        out.append(f'        <div class="mitra-slide{active_cls}" data-index="{i}" style="border-left: 6px solid {color};">')
        out.append('            <div class="mitra-slide-grid">')
        
        # Left column: Media & Photo
        out.append('                <div class="mitra-media-col">')
        out.append('                    <div class="mitra-photo-card">')
        out.append('                        <div class="mitra-photo-wrapper">')
        out.append(f'                            <img src="{itm["foto"]}" alt="{itm["title"]}" class="mitra-photo-img" onclick="if(window.openLightboxWith) window.openLightboxWith(this.src, \'{itm["title"]} - {itm["keterangan_foto"]}\')" title="Klik untuk memperbesar foto (Tampilan Penuh)" decoding="async" loading="lazy">')
        out.append('                            <span class="mitra-photo-badge">📸 Dokumentasi Kegiatan</span>')
        out.append(f'                            <button type="button" class="mitra-photo-zoom-btn" onclick="if(window.openLightboxWith) window.openLightboxWith(\'{itm["foto"]}\', \'{itm["title"]} - {itm["keterangan_foto"]}\')">🔍 Perbesar Foto</button>')
        out.append('                        </div>')
        out.append('                        <div class="mitra-caption-box">')
        out.append('                            <span style="font-size: 15px;">📌</span>')
        out.append(f'                            <span style="font-size: 12.5px; color: #475569; line-height: 1.5;">{itm["keterangan_foto"]}</span>')
        out.append('                        </div>')
        out.append('                    </div>')
        out.append('                    <div style="margin-top: 14px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">')
        out.append(f'                        <span style="background: #dcfce7; color: #166534; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 999px;">{itm["status"]}</span>')
        out.append(f'                        <span style="font-size: 12px; color: #64748b;">Pilar Ke-{i+1} dari 6</span>')
        out.append('                    </div>')
        out.append('                </div>')
        
        # Right column: Details & Checklist
        out.append('                <div class="mitra-details-col">')
        out.append('                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">')
        out.append(f'                        <span style="font-size: 32px; background: #f8fafc; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 12px; border: 1px solid #e2e8f0; flex-shrink: 0;">{itm["icon"]}</span>')
        out.append('                        <div>')
        out.append(f'                            <span class="badge-tag" style="background: {badge["bg"]}; color: {badge["color"]}; font-size: 11px; margin-bottom: 4px; display: inline-block;">{itm["badge"]}</span>')
        out.append(f'                            <h3 style="font-size: 19px; font-weight: 800; color: #0f172a; margin: 0; line-height: 1.3;">{itm["title"]}</h3>')
        out.append('                        </div>')
        out.append('                    </div>')
        out.append(f'                    <p style="font-size: 14px; color: #475569; line-height: 1.6; margin-bottom: 16px;">{itm["desc"]}</p>')
        out.append('                    <div class="mitra-checklist-box">')
        out.append(f'                        <h4 style="font-size: 13.5px; font-weight: 800; color: {color}; margin: 0 0 10px 0; display: flex; align-items: center; gap: 6px;">')
        out.append('                            <span>📋</span> <span>Uraian Kerja & Program Nyata:</span>')
        out.append('                        </h4>')
        out.append('                        <ul class="mitra-checklist-list">')
        for pt in itm["uraian_kerja"]:
            out.append(f'                            <li>{pt}</li>')
        out.append('                        </ul>')
        out.append('                    </div>')
        out.append('                    <div class="mitra-meta-footer">')
        out.append(f'                        <span>👤 Penanggung Jawab: <strong style="color: #0f172a;">{itm["pic"]}</strong></span>')
        out.append(f'                        <span>⏱️ Periode: <strong>{itm["periode"]}</strong></span>')
        out.append('                    </div>')
        out.append('                </div>')
        
        out.append('            </div>')
        out.append('        </div>')
        
    out.append('    </div>')
    
    # Bottom Dots Bar
    out.append('    <div class="mitra-dots-bar" id="mitraDotsBar">')
    for i in range(len(items)):
        active_cls = ' active' if i == 0 else ''
        out.append(f'        <button type="button" class="mitra-dot{active_cls}" data-index="{i}" onclick="window.goToMitraSlide({i})" aria-label="Slide {i+1}"></button>')
    out.append('    </div>')
    out.append('</div>')
    
    return '\n'.join(out)

generated = generate_slider_html(items)
with open('scratch/generated_slider.html', 'w', encoding='utf-8') as f:
    f.write(generated)
print(f"Generated slider HTML! Total length: {len(generated)} chars.")
