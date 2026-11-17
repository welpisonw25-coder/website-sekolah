import re

def test_slider_integrity():
    with open('kolaborasi.html', 'r', encoding='utf-8') as f:
        k_html = f.read()

    with open('css/style.css', 'r', encoding='utf-8') as f:
        css = f.read()

    with open('js/main.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # 1. HTML checks
    assert 'id="mitraSliderWrapper"' in k_html, "Missing #mitraSliderWrapper"
    assert 'id="mitraPrevBtn"' in k_html, "Missing #mitraPrevBtn"
    assert 'id="mitraNextBtn"' in k_html, "Missing #mitraNextBtn"
    assert 'id="mitraTabsNav"' in k_html, "Missing #mitraTabsNav"
    assert 'id="mitraSliderViewport"' in k_html, "Missing #mitraSliderViewport"
    assert 'id="mitraDotsBar"' in k_html, "Missing #mitraDotsBar"
    assert 'id="mitraSlideCounter"' in k_html, "Missing #mitraSlideCounter"
    
    slides = re.findall(r'class="mitra-slide(?:\s|")[^"]*"', k_html)
    assert len(slides) == 6, f"Expected 6 slides, found {len(slides)}"
    
    tabs = re.findall(r'class="mitra-tab-btn(?:\s|")[^"]*"', k_html)
    assert len(tabs) == 6, f"Expected 6 tabs, found {len(tabs)}"
    
    dots = re.findall(r'class="mitra-dot(?:\s|")[^"]*"', k_html)
    assert len(dots) == 6, f"Expected 6 dots, found {len(dots)}"

    # Check photos
    assert 'images/kegiatan-rapat-dewan-guru.jpg' in k_html
    assert 'images/kegiatan-belajar-kelas.jpg' in k_html
    assert 'images/kegiatan-evaluasi-guru.jpg' in k_html
    assert 'images/kegiatan-kebersamaan-guru.jpg' in k_html
    assert 'images/kegiatan-senam-bersama.jpg' in k_html
    assert 'images/kegiatan-pramuka-budaya.jpg' in k_html

    # Check zoom lightbox integration
    zoom_buttons = re.findall(r'class="mitra-photo-zoom-btn"', k_html)
    assert len(zoom_buttons) == 6, f"Expected 6 zoom buttons, found {len(zoom_buttons)}"

    # 2. CSS checks
    assert '.mitra-slider-container' in css
    assert '.mitra-tabs-nav' in css
    assert '.mitra-tab-btn' in css
    assert '.mitra-slide' in css
    assert '.mitra-dot' in css
    assert '.mitra-nav-btn' in css

    # 3. JS checks
    assert 'window.initMitraSlider' in js
    assert 'window.filterPublicMitra' in js
    assert 'function loadDynamicKolaborasi' in js
    assert 'initMitraSlider();' in js

    print("ALL 15 MITRA SLIDER INTEGRITY CHECKS PASSED 100% PERFECTLY!")

if __name__ == '__main__':
    test_slider_integrity()
