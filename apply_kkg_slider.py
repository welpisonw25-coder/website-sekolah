with open('scratch/generated_kkg_slider.html', 'r', encoding='utf-8') as f:
    slider_html = f.read()

# 1. Update pengembangan-guru.html
with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    p_html = f.read()

target_marker = '<div id="kkgDokumentasiGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">\n                    <!-- Diisi otomatis oleh JavaScript -->\n                </div>'

if target_marker in p_html:
    p_html = p_html.replace(target_marker, slider_html + '\n                <div id="kkgDokumentasiGrid" style="display: none;"></div>')
    with open('pengembangan-guru.html', 'w', encoding='utf-8') as f:
        f.write(p_html)
    print("Successfully replaced kkgDokumentasiGrid in pengembangan-guru.html!")
else:
    print("target_marker not found exactly, attempting fuzzy replacement...")
    start_p = p_html.find('id="kkgDokumentasiGrid"')
    if start_p != -1:
        div_start = p_html.rfind('<div', 0, start_p)
        div_end = p_html.find('</div>', start_p) + 6
        p_html = p_html[:div_start] + slider_html + '\n                <div id="kkgDokumentasiGrid" style="display: none;"></div>' + p_html[div_end:]
        with open('pengembangan-guru.html', 'w', encoding='utf-8') as f:
            f.write(p_html)
        print("Fuzzy replaced kkgDokumentasiGrid in pengembangan-guru.html!")

# 2. Update js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# Add initKKGShowcaseSlider(); in DOMContentLoaded
if "initFeaturedShowcaseSlider();" in main_js and "initKKGShowcaseSlider();" not in main_js:
    main_js = main_js.replace(
        "    initFeaturedShowcaseSlider();\n",
        "    initFeaturedShowcaseSlider();\n    initKKGShowcaseSlider();\n"
    )

# Replace the grid rendering in loadDynamicKKG with slider rendering
old_kkg_render = """    // Render galeri dokumentasi KKG jika ada container
    const gridContainer = document.getElementById('kkgDokumentasiGrid');
    if (gridContainer) {
        gridContainer.innerHTML = '';
        const itemsWithPhoto = jadwalList.filter(item => item.foto && item.foto.length > 0);
        if (itemsWithPhoto.length > 0) {
            itemsWithPhoto.forEach(j => {
                const card = document.createElement('div');
                card.style.cssText = 'background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.05);';
                card.innerHTML = `
                    <div style="height: 180px; overflow: hidden; position: relative;">
                        <img src="${j.foto}" alt="${escapeHTML(j.agenda)}" style="width: 100%; height: 100%; object-fit: cover; cursor: pointer;" onclick="if(window.openLightboxWith) window.openLightboxWith('${j.foto}', '${escapeHTML(j.agenda)}')">
                    </div>
                    <div style="padding: 16px;">
                        <span style="font-size: 11px; font-weight: 700; color: #0284c7;">${escapeHTML(j.tanggal || j.bulan || '')}</span>
                        <h4 style="font-size: 14px; font-weight: 700; color: #0f172a; margin: 4px 0 6px;">${escapeHTML(j.agenda)}</h4>
                        <p style="font-size: 12px; color: #64748b; margin: 0;">📍 Tuan Rumah: <strong>${escapeHTML(j.tuan_rumah || '')}</strong></p>
                    </div>
                `;
                gridContainer.appendChild(card);
            });
        }
    }"""

new_kkg_render = """    // Render galeri dokumentasi KKG sebagai Showcase Slider Carousel Otomatis
    const sliderWrapper = document.getElementById('kkgShowcaseSliderWrapper');
    const track = document.getElementById('kkgShowcaseSliderTrack');
    const dotsBar = document.getElementById('kkgShowcaseDotsBar');
    if (sliderWrapper && track && dotsBar) {
        const itemsWithPhoto = jadwalList.filter(item => item.foto && item.foto.length > 0);
        if (itemsWithPhoto.length > 0) {
            const categoryColors = ["#0284c7", "#10b981", "#8b5cf6", "#f59e0b", "#06b6d4", "#ec4899", "#14b8a6"];
            track.innerHTML = itemsWithPhoto.map((itm, i) => {
                const activeCls = i === 0 ? ' active' : '';
                const color = categoryColors[i % categoryColors.length];
                const kelompokBadge = (itm.kelompok || 'KEGIATAN GUGUS 1').toUpperCase();
                const tgl = itm.tanggal || '';
                const agenda = itm.agenda || `Pertemuan KKG #${i+1}`;
                const tuanRumah = itm.tuan_rumah || 'SDN Inpres Arso VIII';
                const foto = itm.foto || 'images/kegiatan-rapat-dewan-guru.jpg';
                const status = itm.status || 'Terlaksana';
                return `
                    <div class="showcase-slide${activeCls}" data-index="${i}">
                        <div class="showcase-slide-image-wrapper">
                            <img src="${foto}" alt="${escapeHTML(agenda)}" class="showcase-slide-img" onclick="if(window.openLightboxWith){ window.openLightboxWith(this.src, '${escapeHTML(agenda)} - Tuan Rumah: ${escapeHTML(tuanRumah)} (${escapeHTML(tgl)})'); }" title="Klik untuk memperbesar foto dokumentasi" decoding="async" loading="lazy">
                            <div class="school-photo-caption">
                                <div>
                                    <span class="showcase-category-pill" style="background: ${color}; color: #ffffff;">${escapeHTML(kelompokBadge)} • ${escapeHTML(tgl)}</span>
                                    <h3 class="showcase-slide-title">${escapeHTML(agenda)}</h3>
                                    <p class="showcase-slide-desc">📍 Tuan Rumah: <strong>${escapeHTML(tuanRumah)}</strong> • Status: <strong>${escapeHTML(status)}</strong> • Kegiatan Resmi Gugus 1 Arso Barat.</p>
                                </div>
                                <div class="showcase-btn-group">
                                    <button type="button" class="btn-showcase-zoom" onclick="if(window.openLightboxWith){ window.openLightboxWith('${foto}', '${escapeHTML(agenda)} - Tuan Rumah: ${escapeHTML(tuanRumah)} (${escapeHTML(tgl)})'); }">
                                        🔍 Perbesar Foto
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');

            dotsBar.innerHTML = itemsWithPhoto.map((_, i) => {
                const activeCls = i === 0 ? ' active' : '';
                return `<button type="button" class="showcase-dot${activeCls}" data-index="${i}" aria-label="Slide ${i+1}"></button>`;
            }).join('');

            if (typeof initKKGShowcaseSlider === 'function') {
                initKKGShowcaseSlider();
            }
        }
    }"""

if old_kkg_render in main_js:
    main_js = main_js.replace(old_kkg_render, new_kkg_render)
    print("Replaced old KKG grid render with new KKG slider render in js/main.js!")
else:
    print("Could not find exact old_kkg_render in js/main.js, let's search...")
    p_kkg_doc = main_js.find("// Render galeri dokumentasi KKG jika ada container")
    if p_kkg_doc != -1:
        p_kkg_doc_end = main_js.find("function loadDynamicSOP() {", p_kkg_doc)
        main_js = main_js[:p_kkg_doc] + new_kkg_render + "\n}\n\n" + main_js[p_kkg_doc_end:]
        print("Replaced KKG render (block search) in js/main.js!")

# Add initKKGShowcaseSlider function right after initFeaturedShowcaseSlider
slider_fn_marker = "function initFeaturedShowcaseSlider() {"
p_fn = main_js.find(slider_fn_marker)
if p_fn != -1 and "function initKKGShowcaseSlider()" not in main_js:
    kkg_slider_fn = """
/* ==========================================================================
   KKG & KKKS DOKUMENTASI SHOWCASE SLIDER (AUTO-SLIDE / CAROUSEL)
   ========================================================================== */
function initKKGShowcaseSlider() {
    const sliderWrapper = document.getElementById('kkgShowcaseSliderWrapper');
    if (!sliderWrapper) return;

    const prevBtn = document.getElementById('kkgShowcasePrevBtn');
    const nextBtn = document.getElementById('kkgShowcaseNextBtn');

    if (window._kkgAutoPlayTimer) {
        clearInterval(window._kkgAutoPlayTimer);
        window._kkgAutoPlayTimer = null;
    }

    const slides = sliderWrapper.querySelectorAll('.showcase-slide');
    const dots = sliderWrapper.querySelectorAll('.showcase-dot');
    if (!slides.length) return;

    let currentIndex = 0;
    slides.forEach((slide, idx) => {
        if (slide.classList.contains('active')) currentIndex = idx;
    });

    const AUTO_PLAY_DELAY = 4500; // Berputar otomatis setiap 4.5 detik seperti Kabar Terkini

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
        window._kkgAutoPlayTimer = setInterval(nextSlide, AUTO_PLAY_DELAY);
    }

    function stopAutoPlay() {
        if (window._kkgAutoPlayTimer) {
            clearInterval(window._kkgAutoPlayTimer);
            window._kkgAutoPlayTimer = null;
        }
    }

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

    dots.forEach((dot, idx) => {
        dot.onclick = function (e) {
            e.preventDefault();
            goToSlide(idx);
            startAutoPlay();
        };
    });

    sliderWrapper.onmouseenter = stopAutoPlay;
    sliderWrapper.onmouseleave = startAutoPlay;

    // Dukungan Touch Swipe untuk Layar HP / Tablet
    let touchStartX = 0;
    let touchEndX = 0;
    sliderWrapper.addEventListener('touchstart', function (e) {
        if (e.changedTouches && e.changedTouches.length > 0) {
            touchStartX = e.changedTouches[0].screenX;
        }
        stopAutoPlay();
    }, { passive: true });

    sliderWrapper.addEventListener('touchend', function (e) {
        if (e.changedTouches && e.changedTouches.length > 0) {
            touchEndX = e.changedTouches[0].screenX;
            const diff = touchEndX - touchStartX;
            if (Math.abs(diff) > 40) {
                if (diff < 0) {
                    nextSlide(); // Geser ke kiri -> lanjut
                } else {
                    prevSlide(); // Geser ke kanan -> mundur
                }
            }
        }
        startAutoPlay();
    }, { passive: true });

    goToSlide(currentIndex);
    startAutoPlay();
}
window.initKKGShowcaseSlider = initKKGShowcaseSlider;
"""
    main_js = main_js[:p_fn] + kkg_slider_fn + "\n" + main_js[p_fn:]
    print("Added initKKGShowcaseSlider to js/main.js successfully!")

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(main_js)

print("Finished updating pengembangan-guru.html and js/main.js!")
