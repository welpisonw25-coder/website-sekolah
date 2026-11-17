with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# 1. Add initMitraSlider(); in DOMContentLoaded (after loadDynamicKolaborasi();)
if "loadDynamicKolaborasi();" in main_js and "initMitraSlider();" not in main_js:
    main_js = main_js.replace(
        "    loadDynamicKolaborasi();\n",
        "    loadDynamicKolaborasi();\n    if (typeof initMitraSlider === 'function') initMitraSlider();\n"
    )

# 2. Find and replace loadDynamicKolaborasi()
old_func_start = "/* ==========================================================================\n   DYNAMIC KOLABORASI & KEMITRAAN LOADER (DENGAN PERBESAR FOTO / LIGHTBOX ZOOM)\n   ========================================================================== */"
old_func_end_marker = "/* ==========================================================================\n   DYNAMIC PENGEMBANGAN GURU (K3S & KKG) LOADER"

p1 = main_js.find(old_func_start)
p2 = main_js.find(old_func_end_marker)

if p1 != -1 and p2 != -1:
    print("Found old loadDynamicKolaborasi block!")
    
    new_code = '''/* ==========================================================================
   DYNAMIC KOLABORASI & KEMITRAAN LOADER (SLIDER CAROUSEL & LIGHTBOX ZOOM)
   ========================================================================== */
function loadDynamicKolaborasi() {
    const container = document.getElementById('kolaborasiListContainer');
    if (!container) return;

    let items = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.kolaborasi) && window.SDN_DATABASE.kolaborasi.length > 0) {
        items = window.SDN_DATABASE.kolaborasi;
    }
    // 2. Fallback: LocalStorage Cache
    if (!items) {
        try {
            const raw = localStorage.getItem('sdn_kolaborasi_data');
            if (raw) {
                const parsed = JSON.parse(raw);
                if (Array.isArray(parsed) && parsed.length > 0) {
                    items = parsed;
                }
            }
        } catch (e) {
            console.warn('Gagal membaca data kolaborasi dari localStorage:', e);
        }
    }

    if (!items || items.length === 0) {
        if (typeof window.initMitraSlider === 'function') {
            window.initMitraSlider();
        }
        return;
    }

    const borderColors = ['#0284c7', '#10b981', '#f59e0b', '#8b5cf6', '#ef4444', '#14b8a6'];
    const badgeColors = [
        { bg: '#e0f2fe', color: '#0369a1' },
        { bg: '#d1fae5', color: '#065f46' },
        { bg: '#fef3c7', color: '#92400e' },
        { bg: '#ede9fe', color: '#5b21b6' },
        { bg: '#fee2e2', color: '#991b1b' },
        { bg: '#ccfbf1', color: '#115e59' }
    ];

    const shortTabNames = [
        "1. Guru-Guru",
        "2. Guru-Siswa",
        "3. Komite",
        "4. Paguyuban",
        "5. Puskesmas",
        "6. Kampung Adat"
    ];

    let tabsHtml = '';
    let slidesHtml = '';
    let dotsHtml = '';

    items.forEach((item, index) => {
        const color = borderColors[index % borderColors.length];
        const badge = badgeColors[index % badgeColors.length];
        const icon = item.icon || '🤝';
        const judul = item.judul || ('Pilar Kemitraan ' + (index + 1));
        const kategori = item.kategori || 'KEMITRAAN SEKOLAH';
        const ringkasan = item.ringkasan || '';
        const pic = item.penanggung_jawab || 'Dewan Guru & Kepala Sekolah';
        const periode = item.periode || 'Berkala & Rutin';
        const status = item.status || 'Aktif Berjalan Rutin';
        const foto = item.foto || '';
        const keteranganFoto = item.keterangan_foto || 'Dokumentasi kegiatan resmi kemitraan SDN Inpres Arso VIII.';
        const tabTitle = shortTabNames[index] || (`${index + 1}. ` + judul.split(' ')[0]);
        const activeClass = index === 0 ? ' active' : '';

        let uraianList = [];
        if (Array.isArray(item.uraian_kerja)) {
            uraianList = item.uraian_kerja;
        } else if (typeof item.uraian_kerja === 'string') {
            uraianList = item.uraian_kerja.split('\\n').map(s => s.trim().replace(/^[-*•\\d.]+\\s*/, '')).filter(s => s.length > 0);
        }
        const listHtml = uraianList.map(u => '<li>' + escapeHTML(u) + '</li>').join('');

        tabsHtml += `
            <button type="button" class="mitra-tab-btn${activeClass}" data-index="${index}" onclick="window.goToMitraSlide(${index})">
                <span>${icon}</span> <span>${escapeHTML(tabTitle)}</span>
            </button>
        `;

        dotsHtml += `
            <button type="button" class="mitra-dot${activeClass}" data-index="${index}" onclick="window.goToMitraSlide(${index})" aria-label="Slide ${index + 1}"></button>
        `;

        slidesHtml += `
            <div class="mitra-slide${activeClass}" data-index="${index}" style="border-left: 6px solid ${color};">
                <div class="mitra-slide-grid">
                    <div class="mitra-media-col">
                        <div class="mitra-photo-card">
                            <div class="mitra-photo-wrapper">
                                <img src="${foto}" alt="${escapeHTML(judul)}" class="mitra-photo-img" onclick="if(window.openLightboxWith) window.openLightboxWith(this.src, '${escapeHTML(judul)} - ${escapeHTML(keteranganFoto)}')" title="Klik untuk memperbesar foto (Tampilan Penuh)" decoding="async" loading="lazy">
                                <span class="mitra-photo-badge">📸 Dokumentasi Kegiatan</span>
                                <button type="button" class="mitra-photo-zoom-btn" onclick="if(window.openLightboxWith) window.openLightboxWith('${foto}', '${escapeHTML(judul)} - ${escapeHTML(keteranganFoto)}')">🔍 Perbesar Foto</button>
                            </div>
                            <div class="mitra-caption-box">
                                <span style="font-size: 15px;">📌</span>
                                <span style="font-size: 12.5px; color: #475569; line-height: 1.5;">${escapeHTML(keteranganFoto)}</span>
                            </div>
                        </div>
                        <div style="margin-top: 14px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
                            <span style="background: #dcfce7; color: #166534; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 999px;">${escapeHTML(status)}</span>
                            <span style="font-size: 12px; color: #64748b;">Pilar Ke-${index + 1} dari ${items.length}</span>
                        </div>
                    </div>
                    <div class="mitra-details-col">
                        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                            <span style="font-size: 32px; background: #f8fafc; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 12px; border: 1px solid #e2e8f0; flex-shrink: 0;">${icon}</span>
                            <div>
                                <span class="badge-tag" style="background: ${badge.bg}; color: ${badge.color}; font-size: 11px; margin-bottom: 4px; display: inline-block;">${escapeHTML(kategori)}</span>
                                <h3 style="font-size: 19px; font-weight: 800; color: #0f172a; margin: 0; line-height: 1.3;">${escapeHTML(judul)}</h3>
                            </div>
                        </div>
                        <p style="font-size: 14px; color: #475569; line-height: 1.6; margin-bottom: 16px;">${escapeHTML(ringkasan)}</p>
                        <div class="mitra-checklist-box">
                            <h4 style="font-size: 13.5px; font-weight: 800; color: ${color}; margin: 0 0 10px 0; display: flex; align-items: center; gap: 6px;">
                                <span>📋</span> <span>Uraian Kerja & Program Nyata:</span>
                            </h4>
                            <ul class="mitra-checklist-list">
                                ${listHtml}
                            </ul>
                        </div>
                        <div class="mitra-meta-footer">
                            <span>👤 Penanggung Jawab: <strong style="color: #0f172a;">${escapeHTML(pic)}</strong></span>
                            <span>⏱️ Periode: <strong>${escapeHTML(periode)}</strong></span>
                        </div>
                    </div>
                </div>
            </div>
        `;
    });

    container.innerHTML = `
        <div class="mitra-slider-container" id="mitraSliderWrapper">
            <div class="mitra-slider-topbar">
                <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                    <span style="background: #0284c7; color: #ffffff; font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 999px; letter-spacing: 0.5px;">🤝 SHOWCASE PROGRAM KEMITRAAN</span>
                    <span id="mitraSlideCounter" style="font-size: 13px; font-weight: 700; color: #475569;">Pilar 1 dari ${items.length}</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <button type="button" class="mitra-nav-btn" id="mitraPrevBtn" title="Pilar Sebelumnya" aria-label="Sebelumnya">❮</button>
                    <button type="button" class="mitra-nav-btn" id="mitraNextBtn" title="Pilar Berikutnya" aria-label="Berikutnya">❯</button>
                </div>
            </div>
            <div class="mitra-tabs-nav" id="mitraTabsNav">
                ${tabsHtml}
            </div>
            <div class="mitra-slider-viewport" id="mitraSliderViewport">
                ${slidesHtml}
            </div>
            <div class="mitra-dots-bar" id="mitraDotsBar">
                ${dotsHtml}
            </div>
        </div>
    `;

    if (typeof window.initMitraSlider === 'function') {
        window.initMitraSlider();
    }
}

/* ==========================================================================
   INTERACTIVE MITRA & KOLABORASI SLIDER (CAROUSEL & SEARCH FILTER)
   ========================================================================== */
window.initMitraSlider = function() {
    const wrapper = document.getElementById('mitraSliderWrapper');
    if (!wrapper) return;

    const slides = wrapper.querySelectorAll('.mitra-slide');
    const tabs = wrapper.querySelectorAll('.mitra-tab-btn');
    const dots = wrapper.querySelectorAll('.mitra-dot');
    const counter = document.getElementById('mitraSlideCounter');
    const prevBtn = document.getElementById('mitraPrevBtn');
    const nextBtn = document.getElementById('mitraNextBtn');
    const viewport = document.getElementById('mitraSliderViewport');

    if (!slides.length) return;

    let currentIndex = 0;
    slides.forEach((s, idx) => {
        if (s.classList.contains('active')) currentIndex = idx;
    });

    const AUTO_DELAY = 5500; // Berputar otomatis setiap 5.5 detik

    if (window._mitraAutoTimer) {
        clearInterval(window._mitraAutoTimer);
        window._mitraAutoTimer = null;
    }

    function goTo(idx) {
        if (idx < 0) {
            currentIndex = slides.length - 1;
        } else if (idx >= slides.length) {
            currentIndex = 0;
        } else {
            currentIndex = idx;
        }

        slides.forEach((s, i) => {
            if (i === currentIndex) {
                s.classList.add('active');
            } else {
                s.classList.remove('active');
            }
        });

        tabs.forEach((t, i) => {
            if (i === currentIndex) {
                t.classList.add('active');
                try {
                    t.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
                } catch(e) {}
            } else {
                t.classList.remove('active');
            }
        });

        dots.forEach((d, i) => {
            if (i === currentIndex) {
                d.classList.add('active');
            } else {
                d.classList.remove('active');
            }
        });

        if (counter) {
            counter.textContent = `Pilar ${currentIndex + 1} dari ${slides.length}`;
        }
    }

    window.goToMitraSlide = function(idx) {
        goTo(idx);
        startAuto();
    };

    function next() {
        goTo(currentIndex + 1);
    }

    function prev() {
        goTo(currentIndex - 1);
    }

    function startAuto() {
        stopAuto();
        const searchInput = document.getElementById('publicMitraSearchInput');
        if (searchInput && searchInput.value.trim().length > 0) return;
        window._mitraAutoTimer = setInterval(next, AUTO_DELAY);
    }

    function stopAuto() {
        if (window._mitraAutoTimer) {
            clearInterval(window._mitraAutoTimer);
            window._mitraAutoTimer = null;
        }
    }

    if (prevBtn) {
        prevBtn.onclick = function(e) {
            e.preventDefault();
            prev();
            startAuto();
        };
    }

    if (nextBtn) {
        nextBtn.onclick = function(e) {
            e.preventDefault();
            next();
            startAuto();
        };
    }

    wrapper.onmouseenter = stopAuto;
    wrapper.onmouseleave = startAuto;

    // Dukungan Touch Swipe untuk Layar HP & Tablet
    if (viewport) {
        let touchStartX = 0;
        let touchEndX = 0;
        viewport.addEventListener('touchstart', function(e) {
            if (e.changedTouches && e.changedTouches.length > 0) {
                touchStartX = e.changedTouches[0].screenX;
            }
            stopAuto();
        }, { passive: true });

        viewport.addEventListener('touchend', function(e) {
            if (e.changedTouches && e.changedTouches.length > 0) {
                touchEndX = e.changedTouches[0].screenX;
                const diff = touchEndX - touchStartX;
                if (Math.abs(diff) > 40) {
                    if (diff < 0) {
                        next();
                    } else {
                        prev();
                    }
                }
            }
            startAuto();
        }, { passive: true });
    }

    goTo(currentIndex);
    startAuto();
};

/* ==========================================================================
   FILTER PENCARIAN REALTIME MITRA & KOLABORASI
   ========================================================================== */
window.filterPublicMitra = function() {
    const searchInput = document.getElementById('publicMitraSearchInput');
    const query = (searchInput ? searchInput.value : '').trim().toLowerCase();
    const wrapper = document.getElementById('mitraSliderWrapper');
    if (!wrapper) return;

    const slides = wrapper.querySelectorAll('.mitra-slide');
    const tabs = wrapper.querySelectorAll('.mitra-tab-btn');
    const dots = wrapper.querySelectorAll('.mitra-dot');
    const counter = document.getElementById('mitraSlideCounter');

    if (!query) {
        tabs.forEach(t => {
            t.style.display = '';
            t.style.borderColor = '';
        });
        dots.forEach(d => d.style.display = '');
        if (typeof window.goToMitraSlide === 'function') {
            window.goToMitraSlide(0);
        }
        return;
    }

    let firstMatch = -1;
    let matchCount = 0;

    slides.forEach((slide, idx) => {
        const text = (slide.textContent || '').toLowerCase();
        const matches = text.includes(query);
        const tab = tabs[idx];
        const dot = dots[idx];

        if (matches) {
            matchCount++;
            if (firstMatch === -1) firstMatch = idx;
            if (tab) {
                tab.style.display = '';
                tab.style.borderColor = '#10b981';
            }
            if (dot) dot.style.display = '';
        } else {
            if (tab) tab.style.display = 'none';
            if (dot) dot.style.display = 'none';
        }
    });

    if (firstMatch !== -1) {
        slides.forEach((s, i) => {
            if (i === firstMatch) s.classList.add('active');
            else s.classList.remove('active');
        });
        tabs.forEach((t, i) => {
            if (i === firstMatch) t.classList.add('active');
            else t.classList.remove('active');
        });
        if (counter) {
            counter.textContent = `Ditemukan ${matchCount} dari ${slides.length} pilar kemitraan`;
        }
    } else {
        if (counter) {
            counter.textContent = `Tidak ada pilar yang sesuai dengan "${escapeHTML(query)}"`;
        }
    }
};

'''
    main_js = main_js[:p1] + new_code + main_js[p2:]
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(main_js)
    print("Successfully replaced loadDynamicKolaborasi in js/main.js!")
else:
    print("Could not find boundary markers in js/main.js!")
