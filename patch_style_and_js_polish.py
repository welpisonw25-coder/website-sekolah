import re

# ==========================================
# 1. PATCH CSS/STYLE.CSS
# ==========================================
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace Top Bar block
top_bar_css_regex = re.compile(r'\.top-bar\s*\{[\s\S]*?(?=\/\* ===================================================================\s+HEADER & NAVIGASI UTAMA)', re.MULTILINE)

new_top_bar_css = '''.top-bar {
    background: linear-gradient(90deg, #041c11 0%, #0d5c3a 50%, #041c11 100%);
    color: #f1f5f9;
    font-size: 13px;
    padding: 7px 0;
    border-bottom: 1px solid rgba(253, 224, 71, 0.25);
    position: relative;
    z-index: 1001;
}

.top-bar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: nowrap;
    gap: 12px;
}

.top-bar-left {
    display: flex;
    align-items: center;
    gap: 16px;
    font-size: 12.5px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.top-bar-right {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-shrink: 0;
}

.top-bar-item {
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.top-bar-clock {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(253, 224, 71, 0.35);
    color: #fde047;
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.3px;
    white-space: nowrap;
}

.top-bar-admin-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, rgba(253, 224, 71, 0.18) 0%, rgba(217, 119, 6, 0.35) 100%);
    border: 1px solid rgba(253, 224, 71, 0.5);
    color: #fde047 !important;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.25s ease;
    white-space: nowrap;
}

.top-bar-admin-btn:hover {
    background: #fde047;
    color: #041c11 !important;
    border-color: #fde047;
    box-shadow: 0 2px 10px rgba(253, 224, 71, 0.45);
    transform: translateY(-1px);
}

.admin-user-icon {
    display: inline-block;
    vertical-align: middle;
}

'''

assert top_bar_css_regex.search(css), 'top_bar_css_regex failed to match'
css = top_bar_css_regex.sub(new_top_bar_css, css, count=1)
print('[CSS] Top bar rules replaced successfully!')

# Replace Hero Section & Marquee block up to hero-glass-card
hero_css_regex = re.compile(r'\.hero-section\s*\{[\s\S]*?(?=\/\* KARTU KACA ELEGAN \(GLASSMORPHISM\))', re.MULTILINE)

new_hero_css = '''.hero-section {
    position: relative;
    background-color: #041c11;
    background-image: 
        /* Overlay gradien halus & lembut: bagian atas gapura jernih cerah, bagian bawah melindungi keterbacaan teks */
        linear-gradient(to bottom, 
            rgba(3, 18, 11, 0.18) 0%, 
            rgba(3, 18, 11, 0.02) 18%, 
            rgba(3, 18, 11, 0.10) 42%, 
            rgba(3, 20, 13, 0.72) 74%, 
            rgba(2, 14, 8, 0.96) 100%),
        url('../images/gerbang-utama.jpg');
    background-position: center top;
    background-size: cover;
    background-repeat: no-repeat;
    color: white;
    padding: 240px 0 95px;
    min-height: 760px;
    display: flex;
    align-items: flex-end;
    overflow: hidden;
}

.hero-container {
    position: relative;
    z-index: 5;
    width: 100%;
}

.hero-content-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    gap: 0;
}

/* ==========================================================================
   ANIMASI SAMBUTAN ELEGAN (3 TAHAP BERKESINAMBUNGAN)
   Tahap 1: SELAMAT DATANG (Putih, Bold, Slide-Up Lembut)
   Tahap 2: PORTAL RESMI • KAMPUNG DUKWIA, KEEROM, PAPUA (Emas/Kuning, Bold)
   Tahap 3: SDN INPRES ARSO VIII (Identitas Sekolah)
   ========================================================================== */
.hero-welcome-stage {
    width: 100%;
    max-width: 820px;
    height: 48px;
    position: relative;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    user-select: none;
}

.welcome-sequence-track {
    position: relative;
    width: 100%;
    height: 100%;
}

.welcome-phase {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    opacity: 0;
    visibility: hidden;
    transform: translate3d(0, 10px, 0);
    transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), transform 0.85s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.85s;
    pointer-events: none;
}

.welcome-phase.active {
    opacity: 1;
    visibility: visible;
    transform: translate3d(0, 0, 0);
    pointer-events: auto;
}

/* Tahap 1: Putih, Huruf Tebal, Elegan */
.welcome-text-white {
    color: #ffffff;
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 3px;
    text-transform: uppercase;
    text-shadow: 0 2px 14px rgba(0, 0, 0, 0.85), 0 0 24px rgba(255, 255, 255, 0.4);
    display: inline-block;
}

/* Tahap 2: Emas / Kuning, Huruf Tebal & Profesional */
.welcome-text-gold {
    color: #fde047;
    font-size: 16.5px;
    font-weight: 750;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    text-shadow: 0 2px 12px rgba(0, 0, 0, 0.85), 0 0 20px rgba(253, 224, 71, 0.4);
    background: rgba(4, 28, 17, 0.7);
    padding: 6px 20px;
    border-radius: 9999px;
    border: 1px solid rgba(253, 224, 71, 0.45);
    backdrop-filter: blur(8px);
    display: inline-block;
}

/* Tahap 3: Identitas SDN INPRES ARSO VIII */
.welcome-text-identity {
    color: #ffffff;
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-shadow: 0 2px 14px rgba(0, 0, 0, 0.85);
    background: linear-gradient(90deg, rgba(5, 42, 22, 0.88) 0%, rgba(13, 92, 58, 0.88) 50%, rgba(5, 42, 22, 0.88) 100%);
    padding: 5px 24px;
    border-radius: 9999px;
    border: 1px solid rgba(253, 224, 71, 0.5);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(8px);
    display: inline-block;
}

@media (prefers-reduced-motion: reduce) {
    .welcome-phase {
        transition: none !important;
        transform: none !important;
    }
}

'''

assert hero_css_regex.search(css), 'hero_css_regex failed to match'
css = hero_css_regex.sub(new_hero_css, css, count=1)
print('[CSS] Hero section and welcome stage rules replaced successfully!')

# Append responsive rules at the end of style.css to guarantee priority on HP/Mobile/Desktop
responsive_polish_css = '''
/* ==========================================================================
   PENYEMPURNAAN TAMPILAN RESPONSIVE (HP, TABLET, LAPTOP, DESKTOP)
   ========================================================================== */
@media (max-width: 992px) {
    .hero-section {
        padding: 210px 0 80px;
        min-height: 700px;
    }
    .welcome-text-white {
        font-size: 23px;
        letter-spacing: 2px;
    }
    .welcome-text-gold {
        font-size: 15px;
    }
    .welcome-text-identity {
        font-size: 19px;
    }
}

@media (max-width: 768px) {
    /* Header Top Bar pada Layar Smartphone */
    .top-bar {
        padding: 6px 0;
    }
    .top-bar .container {
        justify-content: space-between;
        gap: 6px;
    }
    .top-bar-left {
        font-size: 11px;
        max-width: 52%;
    }
    .top-bar-contact-hide {
        display: none !important;
    }
    .top-bar-right {
        gap: 6px;
    }
    .top-bar-clock {
        font-size: 11px;
        padding: 3px 8px;
    }
    .top-bar-admin-btn {
        font-size: 11px;
        padding: 3px 9px;
    }

    /* Hero Section pada HP: Seluruh Gapura Tampil Utuh di Atas, Portal di Bawahnya */
    .hero-section {
        background-size: 100% auto !important;
        background-position: center top !important;
        background-repeat: no-repeat !important;
        padding-top: calc(100vw * (1024 / 1536) + 15px) !important;
        padding-bottom: 50px !important;
        min-height: auto !important;
    }

    .hero-welcome-stage {
        height: 42px;
        margin-bottom: 10px;
    }
    .welcome-text-white {
        font-size: 18px;
        letter-spacing: 1.5px;
    }
    .welcome-text-gold {
        font-size: 12px;
        padding: 4px 14px;
        letter-spacing: 0.5px;
    }
    .welcome-text-identity {
        font-size: 15px;
        padding: 4px 14px;
    }

    .hero-glass-card {
        padding: 20px 16px !important;
        border-radius: 18px !important;
        margin-top: 5px !important;
        max-width: 100% !important;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.6) !important;
    }
    .hero-title {
        font-size: 24px !important;
    }
    .hero-tagline {
        font-size: 13.5px !important;
    }
    .hero-subtitle {
        font-size: 12px !important;
        line-height: 1.5 !important;
    }
}

@media (max-width: 480px) {
    .hero-section {
        padding-top: calc(100vw * (1024 / 1536) + 10px) !important;
        padding-bottom: 40px !important;
    }
    .welcome-text-white {
        font-size: 16px;
        letter-spacing: 1.2px;
    }
    .welcome-text-gold {
        font-size: 11px;
        padding: 3px 10px;
    }
    .welcome-text-identity {
        font-size: 13.5px;
        padding: 3px 12px;
    }
    .top-bar-left {
        max-width: 48%;
    }
}
'''

css += responsive_polish_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('SUCCESS: css/style.css updated successfully!')

# ==========================================
# 2. PATCH JS/MAIN.JS
# ==========================================
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace initHeroInteractions function body
init_hero_regex = re.compile(r'function initHeroInteractions\(\)\s*\{[\s\S]*?(?=\/\* -------------------------------------------------------------------\s+6\. SIMULASI PENDAFTARAN PPDB ONLINE|\/\* -------------------------------------------------------------------\s+5C\. RENDER INFORMASI PPDB)', re.MULTILINE)

new_init_hero_js = '''function initHeroInteractions() {
    // Animasi Sambutan Baru: 3 Tahap Berkesinambungan (Selamat Datang -> Portal Resmi -> Identitas Sekolah)
    const phases = [
        document.getElementById('welcomePhase1'),
        document.getElementById('welcomePhase2'),
        document.getElementById('welcomePhase3')
    ].filter(Boolean);

    if (phases.length > 0) {
        let currentIdx = 0;
        const PHASE_DURATION = 4200; // 4.2 detik jeda waktu baca nyaman per tahap

        function switchPhase(nextIdx) {
            phases.forEach((p, idx) => {
                if (idx === nextIdx) {
                    p.classList.add('active');
                } else {
                    p.classList.remove('active');
                }
            });
            currentIdx = nextIdx;
        }

        // Jalankan siklus otomatis berkesinambungan
        setInterval(() => {
            const nextIdx = (currentIdx + 1) % phases.length;
            switchPhase(nextIdx);
        }, PHASE_DURATION);
    }

    // Lightbox zoom untuk foto gapura utama
    const btnZoomHero = document.getElementById('btnZoomHeroPhoto');
    const btnZoomShowcase = document.getElementById('btnZoomShowcase');
    const showcaseImg = document.getElementById('showcaseImage');

    function openModalWith(src, alt) {
        if (typeof window.openLightboxWith === 'function') {
            window.openLightboxWith(src, alt);
        } else {
            const modal = document.querySelector('.lightbox-modal');
            const modalImg = document.querySelector('.lightbox-content img');
            if (modal && modalImg) {
                modalImg.src = src;
                modalImg.alt = alt || 'Dokumentasi SDN Inpres Arso VIII';
                modal.classList.add('active');
            }
        }
    }

    if (btnZoomHero) {
        btnZoomHero.addEventListener('click', function (e) {
            e.preventDefault();
            openModalWith('images/gerbang-utama.jpg', 'Foto Resmi Gapura Utama SDN INPRES ARSO VIII');
        });
    }

    if (btnZoomShowcase) {
        btnZoomShowcase.addEventListener('click', function (e) {
            e.preventDefault();
            openModalWith('images/gerbang-sekolah.jpg', 'Foto Resmi Gapura Kehormatan & Dewan Guru SDN Inpres Arso VIII');
        });
    }

    if (showcaseImg) {
        showcaseImg.addEventListener('click', function () {
            openModalWith(this.src, this.alt);
        });
    }
}

'''

assert init_hero_regex.search(js), 'init_hero_regex failed to match'
js = init_hero_regex.sub(new_init_hero_js, js, count=1)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('SUCCESS: js/main.js updated successfully!')
