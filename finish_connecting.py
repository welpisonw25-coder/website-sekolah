# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# Replace initFeaturedShowcaseSlider
idx_start = main_js.find('function initFeaturedShowcaseSlider() {')
idx_end = main_js.find('/* -------------------------------------------------------------------\n   CEK MANDIRI STATUS KELULUSAN / PENERIMAAN PPDB OLEH ORANG TUA', idx_start)

assert idx_start != -1 and idx_end != -1, "Slider slice not found"

new_slider_code = """function initFeaturedShowcaseSlider() {
    const sliderWrapper = document.getElementById('showcaseSliderWrapper');
    if (!sliderWrapper) return;

    const slides = sliderWrapper.querySelectorAll('.showcase-slide');
    const dots = sliderWrapper.querySelectorAll('.showcase-dot');
    const prevBtn = document.getElementById('showcasePrevBtn');
    const nextBtn = document.getElementById('showcaseNextBtn');

    if (!slides.length) return;

    let currentIndex = 0;
    const AUTO_PLAY_DELAY = 5500; // Bergeser otomatis setiap 5.5 detik

    if (window._showcaseAutoPlayTimer) {
        clearInterval(window._showcaseAutoPlayTimer);
        window._showcaseAutoPlayTimer = null;
    }

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

    if (nextBtn && !nextBtn._sliderBound) {
        nextBtn._sliderBound = true;
        nextBtn.addEventListener('click', function (e) {
            e.preventDefault();
            nextSlide();
            startAutoPlay();
        });
    }

    if (prevBtn && !prevBtn._sliderBound) {
        prevBtn._sliderBound = true;
        prevBtn.addEventListener('click', function (e) {
            e.preventDefault();
            prevSlide();
            startAutoPlay();
        });
    }

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

    if (!sliderWrapper._hoverBound) {
        sliderWrapper._hoverBound = true;
        sliderWrapper.addEventListener('mouseenter', stopAutoPlay);
        sliderWrapper.addEventListener('mouseleave', startAutoPlay);

        let touchStartX = 0;
        let touchEndX = 0;

        sliderWrapper.addEventListener('touchstart', function (e) {
            touchStartX = e.changedTouches[0].screenX;
            stopAutoPlay();
        }, { passive: true });

        sliderWrapper.addEventListener('touchend', function (e) {
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
        }, { passive: true });
    }

    startAutoPlay();
}

"""

main_js = main_js[:idx_start] + new_slider_code + main_js[idx_end:]

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(main_js)

print("SUCCESS: main.js updated with slider logic!")

# Update js/admin.js: getPengumumanData, getSambutanData, getGaleriData, getGuruData, getSiswaData, getSarprasData, getKolaborasiData, getKKGData, getSOPData
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

# Update getPengumumanData
old_get_pengumuman = """function getPengumumanData() {
    const data = localStorage.getItem('sdn_pengumuman_data');
    return data ? JSON.parse(data) : defaultPengumuman;
}"""

new_get_pengumuman = """function getPengumumanData() {
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.pengumuman) && window.SDN_DATABASE.pengumuman.length > 0) {
        return window.SDN_DATABASE.pengumuman;
    }
    const data = localStorage.getItem('sdn_pengumuman_data');
    return data ? JSON.parse(data) : defaultPengumuman;
}"""

if old_get_pengumuman in admin_js:
    admin_js = admin_js.replace(old_get_pengumuman, new_get_pengumuman)
    print("SUCCESS: admin.js updated with getPengumumanData")

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(admin_js)
