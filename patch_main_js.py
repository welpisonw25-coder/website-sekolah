# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# 1. Update renderShowcaseSlides
start_render = main_js.find('function renderShowcaseSlides(newsData)')
end_render = main_js.find('/* -------------------------------------------------------------------\n   10B. SINKRONISASI SAMBUTAN KEPALA SEKOLAH', start_render)
assert start_render != -1 and end_render != -1, "renderShowcaseSlides bounds not found"

new_render = '''function renderShowcaseSlides(newsData) {
    const track = document.getElementById('showcaseSliderTrack');
    const dotsBar = document.getElementById('showcaseDotsBar');
    if (!track || !dotsBar) return;

    // Pastikan data berita valid; jika kosong gunakan fallback default berita kegiatan
    const dynamicNews = (Array.isArray(newsData) && newsData.length > 0) 
        ? newsData.slice(0, 6) 
        : (Array.isArray(defaultMainNewsList) ? defaultMainNewsList.slice(0, 6) : []);
    if (!dynamicNews || dynamicNews.length === 0) return;

    const categoryColors = ['#0284c7', '#16a34a', '#8b5cf6', '#d97706', '#ea580c', '#0d9488'];
    const categoryIcons = ['🛰️', '🏃', '🕊️', '🏕️', '📚', '⭐'];

    let slidesHtml = '';
    let dotsHtml = '';

    dynamicNews.forEach((item, idx) => {
        const isActive = (idx === 0) ? ' active' : '';
        const color = categoryColors[idx % categoryColors.length];
        const icon = categoryIcons[idx % categoryIcons.length];
        const photo = item.foto || 'images/kegiatan-anbk-komputer.jpg';
        const snippet = item.snippet || item.isi || '';
        const cleanSnippet = snippet.replace(/<[^>]*>?/gm, '').slice(0, 160) + '...';
        const categoryName = item.kategori || 'Kabar Terkini';
        const safeTitle = escapeHTML(item.judul || 'Kabar Sekolah');

        slidesHtml += `
            <div class="showcase-slide${isActive}" data-index="${idx}">
                <div class="showcase-slide-image-wrapper">
                    <img src="${photo}" alt="${safeTitle}" class="showcase-slide-img" onclick="if(window.openLightboxWith){ window.openLightboxWith('${photo.replace(/'/g, "\\'")}', '${safeTitle}'); }" title="Klik untuk memperbesar foto berita" decoding="async" loading="${idx === 0 ? 'eager' : 'lazy'}">
                </div>
                <div class="school-photo-caption">
                    <div>
                        <span class="showcase-category-pill" style="background: ${color}; color: white;">${icon} ${escapeHTML(categoryName)}</span>
                        <h3 class="showcase-slide-title">${safeTitle}</h3>
                        <p class="showcase-slide-desc">${escapeHTML(cleanSnippet)}</p>
                    </div>
                    <div class="showcase-btn-group">
                        <button type="button" class="btn btn-showcase-zoom" onclick="if(window.openLightboxWith){ window.openLightboxWith('${photo.replace(/'/g, "\\'")}', '${safeTitle}'); }">🔍 Perbesar Foto</button>
                        <a href="berita.html" class="btn btn-showcase-action">Baca Berita Lengkap →</a>
                    </div>
                </div>
            </div>
        `;

        dotsHtml += `
            <button type="button" class="showcase-dot${isActive}" data-index="${idx}" aria-label="Slide ${idx + 1}: ${safeTitle}"></button>
        `;
    });

    track.innerHTML = slidesHtml;
    dotsBar.innerHTML = dotsHtml;

    // Inisialisasi ulang event listener & jalankan auto-play slider
    initFeaturedShowcaseSlider();
}

'''

main_js = main_js[:start_render] + new_render + main_js[end_render:]

# 2. Update initFeaturedShowcaseSlider
start_slider = main_js.find('function initFeaturedShowcaseSlider()')
end_slider = main_js.find('/* -------------------------------------------------------------------\n   CEK MANDIRI STATUS KELULUSAN', start_slider)
assert start_slider != -1 and end_slider != -1, "initFeaturedShowcaseSlider bounds not found"

new_slider = '''function initFeaturedShowcaseSlider() {
    const sliderWrapper = document.getElementById('showcaseSliderWrapper');
    if (!sliderWrapper) return;

    const prevBtn = document.getElementById('showcasePrevBtn');
    const nextBtn = document.getElementById('showcaseNextBtn');

    // Hentikan timer sebelumnya agar tidak terjadi duplikasi interval
    if (window._showcaseAutoPlayTimer) {
        clearInterval(window._showcaseAutoPlayTimer);
        window._showcaseAutoPlayTimer = null;
    }

    const slides = sliderWrapper.querySelectorAll('.showcase-slide');
    const dots = sliderWrapper.querySelectorAll('.showcase-dot');
    if (!slides.length) return;

    let currentIndex = 0;
    slides.forEach((slide, idx) => {
        if (slide.classList.contains('active')) currentIndex = idx;
    });

    const AUTO_PLAY_DELAY = 4500; // Berputar otomatis setiap 4.5 detik

    function goToSlide(index) {
        if (index < 0) {
            currentIndex = slides.length - 1;
        } else if (index >= slides.length) {
            currentIndex = 0;
        } else {
            currentIndex = index;
        }

        slides.forEach((slide, idx) => {
            if (idx === currentIndex) {
                slide.classList.add('active');
            } else {
                slide.classList.remove('active');
            }
        });

        dots.forEach((dot, idx) => {
            if (idx === currentIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }

    function nextSlide() {
        goToSlide(currentIndex + 1);
    }

    function prevSlide() {
        goToSlide(currentIndex - 1);
    }

    function startAutoPlay() {
        stopAutoPlay();
        window._showcaseAutoPlayTimer = setInterval(nextSlide, AUTO_PLAY_DELAY);
    }

    function stopAutoPlay() {
        if (window._showcaseAutoPlayTimer) {
            clearInterval(window._showcaseAutoPlayTimer);
            window._showcaseAutoPlayTimer = null;
        }
    }

    // Bind tombol panah kiri & kanan dengan handler segar
    if (nextBtn) {
        nextBtn.onclick = function (e) {
            e.preventDefault();
            nextSlide();
            startAutoPlay();
        };
    }

    if (prevBtn) {
        prevBtn.onclick = function (e) {
            e.preventDefault();
            prevSlide();
            startAutoPlay();
        };
    }

    // Bind indikator dots
    dots.forEach(function (dot) {
        dot.onclick = function (e) {
            e.preventDefault();
            const idx = parseInt(dot.getAttribute('data-index'), 10);
            if (!isNaN(idx)) {
                goToSlide(idx);
                startAutoPlay();
            }
        };
    });

    // Jeda saat cursor mouse berada di atas slider, lanjutkan saat keluar
    sliderWrapper.onmouseenter = stopAutoPlay;
    sliderWrapper.onmouseleave = startAutoPlay;

    // Touch swipe mobile
    let touchStartX = 0;
    let touchEndX = 0;
    sliderWrapper.ontouchstart = function (e) {
        touchStartX = e.changedTouches[0].screenX;
        stopAutoPlay();
    };
    sliderWrapper.ontouchend = function (e) {
        touchEndX = e.changedTouches[0].screenX;
        const diffX = touchEndX - touchStartX;
        if (Math.abs(diffX) > 40) {
            if (diffX < 0) {
                nextSlide();
            } else {
                prevSlide();
            }
        }
        startAutoPlay();
    };

    // Jalankan rotasi otomatis langsung
    startAutoPlay();
}

'''

main_js = main_js[:start_slider] + new_slider + main_js[end_slider:]

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(main_js)

print("Successfully updated js/main.js!")
