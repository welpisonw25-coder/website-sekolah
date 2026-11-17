# -*- coding: utf-8 -*-

with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# 1. Update loadDynamicAnnouncements
idx_ann_start = main_js.find('function loadDynamicAnnouncements() {\n    try {\n        let items = null;')
idx_ann_end = main_js.find('/* -------------------------------------------------------------------\n   10. SINKRONISASI BERITA DINAMIS', idx_ann_start)

assert idx_ann_start != -1 and idx_ann_end != -1, "Announcements slice not found"

new_announcements_code = """function loadDynamicAnnouncements() {
    try {
        let items = null;
        // 1. Prioritas Utama: Google Cloud Firebase
        if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.pengumuman) && window.SDN_DATABASE.pengumuman.length > 0) {
            items = window.SDN_DATABASE.pengumuman;
        }
        // 2. Fallback: LocalStorage Cache
        if (!items) {
            try {
                const raw = localStorage.getItem('sdn_pengumuman_data');
                if (raw) {
                    const parsed = JSON.parse(raw);
                    if (Array.isArray(parsed) && parsed.length > 0) items = parsed;
                }
            } catch (e) {}
        }
        if (!items || items.length === 0) items = defaultPengumuman;

        // 1. RENDER DI HALAMAN BERANDA (index.html: #homePengumumanGrid) - HANYA 3 TERBARU
        const homePengumumanContainer = document.getElementById('homePengumumanGrid');
        if (homePengumumanContainer) {
            homePengumumanContainer.innerHTML = '';
            const topAnnouncements = items.slice(0, 3);
            const borderColors = ['#0284c7', '#16a34a', '#f59e0b', '#8b5cf6'];
            const badgeBgs = ['#dbeafe', '#dcfce7', '#fef3c7', '#ede9fe'];
            const badgeColors = ['#1e40af', '#166534', '#92400e', '#5b21b6'];

            topAnnouncements.forEach((item, idx) => {
                const bColor = borderColors[idx % borderColors.length];
                const bBg = badgeBgs[idx % badgeBgs.length];
                const tColor = badgeColors[idx % badgeColors.length];
                const card = document.createElement('div');
                card.style.cssText = `padding: 20px; background: #ffffff; border-radius: 10px; border: 1px solid var(--border-color); border-left: 4px solid ${bColor}; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 2px 6px rgba(0,0,0,0.03);`;
                
                const snippet = item.isi ? (item.isi.length > 150 ? item.isi.substring(0, 147) + '...' : item.isi) : '';
                card.innerHTML = `
                    <div>
                        <span style="font-size: 11px; background: ${bBg}; color: ${tColor}; padding: 3px 10px; border-radius: 999px; font-weight: 700; text-transform: uppercase;">${escapeHTML(item.kategori || 'PENGUMUMAN')}</span>
                        <h4 style="font-size: 16px; margin: 10px 0 8px; font-weight: 700; line-height: 1.4;">
                            <a href="pengumuman.html" style="color: var(--primary-dark); text-decoration: none;">${escapeHTML(item.judul)}</a>
                        </h4>
                        <p style="font-size: 13px; color: var(--dark-muted); margin: 0 0 12px; line-height: 1.6;">${escapeHTML(snippet)}</p>
                    </div>
                    <div style="font-size: 11.5px; color: #64748b; border-top: 1px dashed #e2e8f0; padding-top: 8px;">
                        📅 ${escapeHTML(item.tanggal || 'Terkini')} • Oleh: ${escapeHTML(item.pengirim || 'Kepala Sekolah')}
                    </div>
                `;
                homePengumumanContainer.appendChild(card);
            });
        }

        // 2. RENDER DI HALAMAN PENGUMUMAN (pengumuman.html: #pengumumanList)
        const pengumumanContainer = document.getElementById('pengumumanList') || document.querySelector('.section-pill + .section-title')?.parentElement?.nextElementSibling;
        if (pengumumanContainer && (window.location.pathname.includes('pengumuman.html') || document.getElementById('pengumumanList'))) {
            pengumumanContainer.innerHTML = '';
            items.forEach(item => {
                const card = document.createElement('div');
                card.className = 'card';
                card.style = 'padding: 24px; border-left: 5px solid var(--primary); margin-bottom: 20px;';
                card.innerHTML = `
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
                        <span class="badge-tag akreditasi">${escapeHTML(item.kategori || 'Pengumuman')}</span>
                        <span style="font-size: 12px; color: var(--dark-muted);">Diterbitkan: ${escapeHTML(item.tanggal || '')}</span>
                    </div>
                    <h3 style="font-size: 18px; color: var(--primary-dark); font-weight: 800; margin-bottom: 8px;">
                        ${escapeHTML(item.judul)}
                    </h3>
                    <p style="font-size: 14px; color: #475569; line-height: 1.7; margin-bottom: 12px;">
                        ${escapeHTML(item.isi)}
                    </p>
                    <div style="font-size: 12.5px; color: var(--dark-muted); font-style: italic;">
                        Tertanda: ${escapeHTML(item.pengirim || 'Kepala Sekolah - Adi Puspito, S.Pd')}
                    </div>
                `;
                pengumumanContainer.appendChild(card);
            });
        }
    } catch (e) {
        console.warn('Error loading dynamic announcements:', e);
    }
}

"""

main_js = main_js[:idx_ann_start] + new_announcements_code + main_js[idx_ann_end:]

# 2. Update loadDynamicNews
idx_news_start = main_js.find('function loadDynamicNews() {\n    let newsData = null;')
idx_news_end = main_js.find('/* -------------------------------------------------------------------\n   10B. SINKRONISASI SAMBUTAN', idx_news_start)

assert idx_news_start != -1 and idx_news_end != -1, "News slice not found"

new_news_code = """function loadDynamicNews() {
    let newsData = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.berita) && window.SDN_DATABASE.berita.length > 0) {
        newsData = window.SDN_DATABASE.berita;
    }
    // 2. Fallback: LocalStorage Cache (saat offline / fetch awal)
    if (!newsData) {
        try {
            const stored = localStorage.getItem('sdn_berita_data');
            if (stored && !stored.includes('unsplash')) {
                const parsed = JSON.parse(stored);
                if (Array.isArray(parsed) && parsed.length > 0) {
                    newsData = parsed;
                }
            }
        } catch (e) {}
    }

    if (!newsData) newsData = defaultMainNewsList;
    window._allPublicNews = newsData;

    // 1. RENDER SLIDER SOROTAN KEGIATAN & KABAR TERKINI DI BERANDA (index.html: #showcaseSliderTrack)
    renderShowcaseSlides(newsData);

    // 2. RENDER GRID BERITA TERBARU DI BERANDA (index.html: #homeNewsGrid) - 3 TERBARU
    const homeGrid = document.getElementById('homeNewsGrid');
    if (homeGrid) {
        homeGrid.innerHTML = '';
        const homeItems = newsData.slice(0, 3);
        homeItems.forEach(item => {
            const card = document.createElement('div');
            card.className = 'news-card';
            const imgThumb = item.foto || 'images/gerbang-sekolah.jpg';
            card.innerHTML = `
                <div class="news-img-holder">
                    <img src="${imgThumb}" alt="${escapeHTML(item.judul)}" class="news-img" decoding="async" loading="lazy">
                    <span class="news-tag">${escapeHTML(item.kategori || 'Kegiatan')}</span>
                </div>
                <div class="news-body">
                    <div class="news-date">📅 ${escapeHTML(item.tanggal)} | ${escapeHTML(item.penulis || 'Humas SDN Inpres Arso 8')}</div>
                    <h3 class="news-title">
                        <a href="berita.html">${escapeHTML(item.judul)}</a>
                    </h3>
                    <p class="news-snippet">${escapeHTML(item.snippet || '')}</p>
                    <a href="berita.html" class="news-link">Baca Selengkapnya →</a>
                </div>
            `;
            homeGrid.appendChild(card);
        });
    }

    // 3. RENDER DI HALAMAN BERITA (berita.html: #beritaListGrid) DENGAN PAGINASI & FILTER
    const beritaGrid = document.getElementById('beritaListGrid') || (document.title.includes('Berita') ? document.querySelector('.news-grid') : null);
    if (beritaGrid) {
        window.filterPublicNews(1);
    }
}

// FUNGSI RENDER DINAMIS CAROUSEL SOROTAN KEGIATAN & KABAR TERKINI
function renderShowcaseSlides(newsData) {
    const track = document.getElementById('showcaseSliderTrack');
    const dotsBar = document.getElementById('showcaseDotsBar');
    if (!track || !dotsBar) return;

    // Pertahankan HTML Slide 0 (Gapura) dan Slide 1 (Dewan Guru)
    if (!window._baseSlide0Html) {
        const s0 = track.querySelector('.showcase-slide[data-index="0"]');
        if (s0) window._baseSlide0Html = s0.outerHTML;
    }
    if (!window._baseSlide1Html) {
        const s1 = track.querySelector('.showcase-slide[data-index="1"]');
        if (s1) window._baseSlide1Html = s1.outerHTML;
    }

    let slidesHtml = (window._baseSlide0Html || '') + (window._baseSlide1Html || '');
    let dotsHtml = `
        <button type="button" class="showcase-dot active" data-index="0" aria-label="Slide 1: Gapura Kehormatan"></button>
        <button type="button" class="showcase-dot" data-index="1" aria-label="Slide 2: Keluarga Besar Dewan Guru"></button>
    `;

    const dynamicNews = (newsData || []).slice(0, 4);
    const categoryColors = ['#0284c7', '#16a34a', '#d97706', '#8b5cf6'];
    const categoryIcons = ['📰', '⭐', '🏕️', '🕊️'];

    dynamicNews.forEach((item, idx) => {
        const slideIdx = idx + 2;
        const color = categoryColors[idx % categoryColors.length];
        const icon = categoryIcons[idx % categoryIcons.length];
        const photo = item.foto || 'images/gerbang-sekolah.jpg';
        const snippet = item.snippet || item.isi || '';
        const cleanSnippet = snippet.length > 180 ? snippet.substring(0, 177) + '...' : snippet;

        slidesHtml += `
            <div class="showcase-slide" data-index="${slideIdx}">
                <div class="showcase-slide-image-wrapper">
                    <img src="${photo}" alt="${escapeHTML(item.judul)}" class="showcase-slide-img" onclick="if(window.openLightboxWith){ window.openLightboxWith('${photo}', '${escapeHTML(item.judul)}'); }" title="Klik untuk memperbesar foto berita" decoding="async" loading="lazy">
                </div>
                <div class="school-photo-caption">
                    <div>
                        <span class="showcase-category-pill" style="background: ${color}; color: white;">${icon} ${escapeHTML(item.kategori || 'KABAR TERKINI')}</span>
                        <h3 class="showcase-slide-title">${escapeHTML(item.judul)}</h3>
                        <p class="showcase-slide-desc">${escapeHTML(cleanSnippet)}</p>
                    </div>
                    <div class="showcase-btn-group">
                        <button type="button" class="btn btn-showcase-zoom" onclick="if(window.openLightboxWith){ window.openLightboxWith('${photo}', '${escapeHTML(item.judul)}'); }">🔍 Perbesar Foto</button>
                        <a href="berita.html" class="btn btn-showcase-action">Baca Berita Lengkap →</a>
                    </div>
                </div>
            </div>
        `;

        dotsHtml += `
            <button type="button" class="showcase-dot" data-index="${slideIdx}" aria-label="Slide ${slideIdx + 1}: ${escapeHTML(item.judul)}"></button>
        `;
    });

    track.innerHTML = slidesHtml;
    dotsBar.innerHTML = dotsHtml;

    const allSlides = track.querySelectorAll('.showcase-slide');
    if (allSlides.length > 0) allSlides[0].classList.add('active');

    // Inisialisasi ulang event listener slider
    initFeaturedShowcaseSlider();
}

"""

main_js = main_js[:idx_news_start] + new_news_code + main_js[idx_news_end:]

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(main_js)

print("SUCCESS: js/main.js updated with announcements and showcase slides!")
