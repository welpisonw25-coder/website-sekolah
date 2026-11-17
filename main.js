// PENGALIHAN OTOMATIS: Semua kunjungan ke domain hosting sementara (surge.sh) dialihkan ke domain resmi (sch.id)
if (typeof window !== 'undefined' && window.location.hostname === 'sdninpresarso8.surge.sh') {
    window.location.replace('https://sdninpresarso8.sch.id' + window.location.pathname + window.location.search + window.location.hash);
}

// PEMBERSIHAN OTOMATIS: Pastikan tidak ada data browser lama yang masih menahan URL Unsplash
try {
    ['sdn_berita_data', 'sdn_galeri_data'].forEach(function(k) {
        var v = localStorage.getItem(k);
        if (v && v.indexOf('unsplash') !== -1) {
            localStorage.removeItem(k);
        }
    });
} catch (e) {}

function escapeHTML(str) {
    if (!str) return '';
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

/**
 * ===================================================================
 * JAVASCRIPT UTAMA - SDN INPRES ARSO VIII (KAB. KEEROM, PAPUA)
 * Berfungsi mandiri (offline & online), responsif, dan interaktif
 * ===================================================================
 */

// HELPER PENYIMPANAN LOCALSTORAGE AMAN (Mencegah QuotaExceededError galeri memblokir berita/pengumuman)
function safeSetStorage(key, val) {
    if (!val) return;
    try {
        localStorage.setItem(key, typeof val === 'string' ? val : JSON.stringify(val));
    } catch (e) {
        // Abaikan batasan quota LocalStorage untuk payload foto besar
    }
}

// PEMBARUAN DATA OTOMATIS & REALTIME DARI GOOGLE CLOUD DATABASE KE SELURUH HP & LAPTOP
window.refreshDataFromCloud = function() {
    if (typeof fetch !== 'function') return;
    const cloudUrl = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json?t=' + Date.now();
    fetch(cloudUrl, { cache: 'no-store' })
        .then(res => {
            if (res.ok) return res.json();
            throw new Error('Cloud fetch failed');
        })
        .then(db => {
            if (db && typeof db === 'object') {
                window.SDN_DATABASE = Object.assign(window.SDN_DATABASE || {}, db);
                window._cloudDataLoaded = true;

                // Sinkronkan ke LocalStorage secara mandiri agar quota galeri tidak pernah memblokir berita/pengumuman
                safeSetStorage('sdn_sambutan_data', db.sambutan);
                safeSetStorage('sdn_berita_data', db.berita);
                safeSetStorage('sdn_pengumuman_data', db.pengumuman);
                safeSetStorage('sdn_guru_data', db.guru);
                safeSetStorage('sdn_sarpras_data', db.sarpras);
                safeSetStorage('sdn_kolaborasi_data', db.kolaborasi);
                safeSetStorage('sdn_kkg_data', db.kkg);
                safeSetStorage('sdn_sop_data', db.sop_data);
                safeSetStorage('sdn_agenda_data', db.agenda);
                safeSetStorage('sdn_ppdb_config', db.ppdb_config);
                if (db.siswa) {
                    safeSetStorage('sdn_siswa_counts', db.siswa);
                    safeSetStorage('sdn_siswa_kelas', db.siswa);
                }
                if (db.galeri) safeSetStorage('sdn_galeri_data', db.galeri);

                // Render ulang seluruh konten dengan data terbaru dari Google Cloud
                loadDynamicAnnouncements();
                loadDynamicAgenda();
                loadDynamicNews();
                loadDynamicSambutan();
                loadDynamicGallery();
                loadDynamicTeachers();
                loadDynamicStudentData();
                loadDynamicSapras();
                loadDynamicKolaborasi();
    if (typeof initMitraSlider === 'function') initMitraSlider();
                loadDynamicKKG();
                loadDynamicSOP();
                loadDynamicProfil();
                loadDynamicKontak();
                loadDynamicBeranda();
                renderPPDBPublicInfo();
            }
        })
        .catch(() => {
            // Fallback ke file data_sekolah.json lokal jika offline / jaringan terputus
            fetch('data_sekolah.json?t=' + Date.now(), { cache: 'no-store' })
                .then(res => res.json())
                .then(db => {
                    if (db && typeof db === 'object') {
                        window.SDN_DATABASE = Object.assign(window.SDN_DATABASE || {}, db);
                        loadDynamicAnnouncements();
                        loadDynamicAgenda();
                        loadDynamicNews();
                        loadDynamicSambutan();
                        loadDynamicGallery();
                        loadDynamicTeachers();
                        loadDynamicStudentData();
                        loadDynamicSapras();
                        loadDynamicKolaborasi();
    if (typeof initMitraSlider === 'function') initMitraSlider();
                        loadDynamicKKG();
                        loadDynamicSOP();
                        renderPPDBPublicInfo();
                    }
                }).catch(() => {});
        });
};

document.addEventListener('DOMContentLoaded', function () {
    initMobileNav();
    initLiveWITClock();
    initScrollToTop();
    initTeacherFilter();
    initSaprasFilter();
    initGalleryLightbox();
    loadDynamicGallery();
    initHeroInteractions();
    initFeaturedShowcaseSlider();
    initKKGShowcaseSlider();
    initPPDBForm();
    initPPDBHumanCaptcha();
    initContactHumanCaptcha();
    renderPPDBPublicInfo();
    initContactForm();
    highlightActiveNavLink();
    loadDynamicAnnouncements();
    loadDynamicAgenda();
    loadDynamicNews();
    loadDynamicSambutan();
    loadDynamicTeachers();
    loadDynamicStudentData();
    loadDynamicSapras();
    loadDynamicKolaborasi();
    if (typeof initMitraSlider === 'function') initMitraSlider();
    loadDynamicKKG();
    loadDynamicSOP();
    loadDynamicProfil();
    loadDynamicKontak();
    loadDynamicBeranda();

    // Eksekusi pembaruan realtime dari Google Cloud Database (Realtime di semua HP & Laptop)
    window.refreshDataFromCloud();

    // Pembaruan seketika antar-tab jika admin mengedit di tab sebelah
    window.addEventListener('storage', function(e) {
        if (!e.key || e.key.startsWith('sdn_')) {
            window.refreshDataFromCloud();
        }
    });

    // Auto-refresh saat pengguna kembali aktif ke jendela/tab website di HP / Laptop
    let _lastTabFocusTime = 0;
    window.addEventListener('focus', function() {
        if (Date.now() - _lastTabFocusTime > 10000) {
            _lastTabFocusTime = Date.now();
            window.refreshDataFromCloud();
        }
    });
});


/* -------------------------------------------------------------------
   1B. LIVE WIT CLOCK (WAKTU INDONESIA TIMUR - PAPUA)
   ------------------------------------------------------------------- */
function initLiveWITClock() {
    const clockElements = document.querySelectorAll('.live-wit-clock');
    if (!clockElements.length) return;

    function tick() {
        const now = new Date();
        const options = {
            timeZone: 'Asia/Jayapura',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
        };
        try {
            const timeStr = new Intl.DateTimeFormat('id-ID', options).format(now).replace(/\./g, ':');
            clockElements.forEach(el => {
                el.textContent = `${timeStr} WIT`;
            });
        } catch (e) {
            // Fallback for older browsers
            clockElements.forEach(el => {
                el.textContent = 'WIT (Papua)';
            });
        }
    }

    tick();
    setInterval(tick, 1000);
}

/* -------------------------------------------------------------------
   1. RESPONSIVE MOBILE NAVIGATION TOGGLE
   ------------------------------------------------------------------- */
function initMobileNav() {
    const toggleBtn = document.querySelector('.mobile-toggle');
    const mainNav = document.querySelector('nav.main-nav');

    if (toggleBtn && mainNav) {
        toggleBtn.addEventListener('click', function () {
            mainNav.classList.toggle('show');
            const isOpen = mainNav.classList.contains('show');
            toggleBtn.setAttribute('aria-expanded', isOpen);
            toggleBtn.innerHTML = isOpen ? '✕' : '☰';
        });

        // Dropdown toggle untuk layar kecil (HP)
        const dropdownItem = mainNav.querySelector('.nav-item-dropdown');
        const dropdownToggle = mainNav.querySelector('.nav-dropdown-toggle');
        if (dropdownItem && dropdownToggle) {
            dropdownToggle.addEventListener('click', function (e) {
                if (window.innerWidth <= 768) {
                    if (!dropdownItem.classList.contains('is-open')) {
                        e.preventDefault();
                        dropdownItem.classList.add('is-open');
                    }
                }
            });
        }

        // Close nav when clicking outside
        document.addEventListener('click', function (e) {
            if (!mainNav.contains(e.target) && !toggleBtn.contains(e.target) && mainNav.classList.contains('show')) {
                mainNav.classList.remove('show');
                if (dropdownItem) dropdownItem.classList.remove('is-open');
                toggleBtn.innerHTML = '☰';
            }
        });
    }
}

/* -------------------------------------------------------------------
   2. SCROLL TO TOP BUTTON
   ------------------------------------------------------------------- */
function initScrollToTop() {
    const scrollBtn = document.querySelector('.fab-scroll-top');
    if (!scrollBtn) return;

    window.addEventListener('scroll', function () {
        if (window.scrollY > 300) {
            scrollBtn.style.display = 'flex';
        } else {
            scrollBtn.style.display = 'none';
        }
    });

    scrollBtn.addEventListener('click', function (e) {
        e.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/* -------------------------------------------------------------------
   3. FILTER & PENCARIAN GURU / TENAGA PENDIDIK
   ------------------------------------------------------------------- */
function initTeacherFilter() {
    const searchInput = document.getElementById('teacherSearch');
    const filterButtons = document.querySelectorAll('.filter-teacher-btn');
    const teacherCards = document.querySelectorAll('.teacher-card');

    if (!teacherCards.length) return;

    let currentCategory = 'all';
    let searchQuery = '';

    function filterTeachers() {
        teacherCards.forEach(card => {
            const role = card.getAttribute('data-role') || '';
            const status = card.getAttribute('data-status') || '';
            const text = card.textContent.toLowerCase();

            const matchesCategory = (currentCategory === 'all') ||
                (currentCategory === 'wali' && role.includes('wali')) ||
                (currentCategory === 'agama' && role.includes('agama')) ||
                (currentCategory === 'mapel' && (role.includes('penjas') || role.includes('inggris'))) ||
                (currentCategory === 'pns' && status.includes('pns')) ||
                (currentCategory === 'p3k' && status.includes('p3k')) ||
                (currentCategory === 'honor' && status.includes('honor'));

            const matchesSearch = text.includes(searchQuery);

            if (matchesCategory && matchesSearch) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    if (searchInput) {
        searchInput.addEventListener('input', function (e) {
            searchQuery = e.target.value.toLowerCase().trim();
            filterTeachers();
        });
    }

    filterButtons.forEach(btn => {
        btn.addEventListener('click', function () {
            filterButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            currentCategory = this.getAttribute('data-filter');
            filterTeachers();
        });
    });
}

/* -------------------------------------------------------------------
   4. FILTER SARANA & PRASARANA
   ------------------------------------------------------------------- */
function initSaprasFilter() {
    const filterBtns = document.querySelectorAll('.filter-sapras-btn');
    const saprasRows = document.querySelectorAll('.sapras-row');

    if (!saprasRows.length || !filterBtns.length) return;

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            const filter = this.getAttribute('data-filter');

            saprasRows.forEach(row => {
                const condition = row.getAttribute('data-condition') || '';
                if (filter === 'all' || condition === filter) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    });
}

/* -------------------------------------------------------------------
   5. GLOBAL LIGHTBOX MODAL (UNTUK FOTO GERBANG & GALERI KEGIATAN)
   ------------------------------------------------------------------- */
window.closeActiveLightbox = function () {
    const modals = document.querySelectorAll('.lightbox-modal');
    modals.forEach(m => {
        m.classList.remove('active');
        m.style.display = 'none';
    });
    document.body.style.overflow = '';
};

window.openLightboxWith = function (src, alt) {
    if (!src) return;
    let modal = document.getElementById('globalLightbox') || document.querySelector('.lightbox-modal');
    
    // Jika elemen modal belum ada di halaman, buat secara otomatis dan pasang ke body
    if (!modal) {
        modal = document.createElement('div');
        modal.className = 'lightbox-modal';
        modal.id = 'globalLightbox';
        modal.style.cssText = 'display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.92); z-index: 999999; align-items: center; justify-content: center; padding: 20px; box-sizing: border-box; backdrop-filter: blur(4px);';
        modal.innerHTML = `
            <button type="button" class="lightbox-close" aria-label="Tutup Tampilan" title="Tutup Tampilan (Esc)" style="position: fixed; top: 20px; right: 24px; color: #ffffff; font-size: 26px; font-weight: 800; cursor: pointer; background: rgba(15, 23, 42, 0.85); border: 2px solid rgba(255, 255, 255, 0.7); border-radius: 50%; width: 48px; height: 48px; display: flex; align-items: center; justify-content: center; z-index: 1000000; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); transition: all 0.2s ease; outline: none;">✕</button>
            <div class="lightbox-content" style="max-width: 92vw; max-height: 88vh; border-radius: 12px; overflow: hidden; position: relative; background: #000000; box-shadow: 0 10px 40px rgba(0,0,0,0.8); display: flex; flex-direction: column; align-items: center;">
                <img src="${src}" alt="${escapeHTML(alt || 'Dokumentasi')}" style="max-width: 100%; max-height: 80vh; object-fit: contain; display: block;">
                <div id="lightboxCaptionBox" style="width: 100%; background: #0f172a; color: #f8fafc; font-size: 13.5px; padding: 12px 18px; text-align: center; border-top: 1px solid rgba(255,255,255,0.15); box-sizing: border-box;">
                    <span id="lightboxCaptionText">${escapeHTML(alt || 'Dokumentasi Resmi SDN Inpres Arso VIII')}</span>
                </div>
            </div>
            <div style="position: absolute; bottom: 12px; left: 0; width: 100%; text-align: center; pointer-events: none;">
                <span style="background: rgba(0,0,0,0.65); color: #cbd5e1; font-size: 12px; padding: 4px 14px; border-radius: 9999px;">✕ Klik tombol X di pojok atas atau tekan Esc untuk menutup</span>
            </div>
        `;
        document.body.appendChild(modal);

        // Bind handler penutup
        const closeBtn = modal.querySelector('.lightbox-close');
        if (closeBtn) closeBtn.onclick = function(e) { e.preventDefault(); e.stopPropagation(); window.closeActiveLightbox(); };
        modal.onclick = function(e) {
            if (e.target === modal || e.target.classList.contains('lightbox-content')) {
                window.closeActiveLightbox();
            }
        };
    }

    let modalImg = modal.querySelector('.lightbox-content img');
    let captionText = modal.querySelector('#lightboxCaptionText');
    if (modalImg) {
        modalImg.src = src;
        modalImg.alt = alt || 'Dokumentasi Resmi SDN Inpres Arso VIII';
    }
    if (captionText) {
        captionText.textContent = alt || 'Dokumentasi Resmi SDN Inpres Arso VIII';
    }

    modal.classList.add('active');
    modal.style.display = 'flex';

    // Perbarui isi modal sesuai bagan aktif saat ini (Gambar Kustom atau SVG Vektor Sinkron)
    const modalHolder = document.getElementById('baganModalContentHolder');
    if (modalHolder) {
        if (window._currentActiveBaganSrc && window._currentActiveBaganSrc.startsWith('data:')) {
            modalHolder.innerHTML = `<img src="${window._currentActiveBaganSrc}" alt="Bagan Struktur Organisasi SDN Inpres Arso VIII" style="display: block; width: 1060px; height: 710px; object-fit: contain; pointer-events: none;" draggable="false">`;
        } else {
            const liveSvg = document.getElementById('baganSvgContainer');
            if (liveSvg && liveSvg.querySelector('svg')) {
                modalHolder.innerHTML = liveSvg.innerHTML;
            } else {
                modalHolder.innerHTML = `<img src="images/bagan-struktur-organisasi.svg" alt="Bagan Struktur Organisasi SDN Inpres Arso VIII" style="display: block; width: 1060px; height: 710px; pointer-events: none;" draggable="false">`;
            }
        }
    }
    document.body.style.overflow = 'hidden';
};

// Global Esc key listener untuk menutup lightbox dan modal bagan kapan saja
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        window.closeActiveLightbox();
        if (typeof window.closeBaganModal === 'function') {
            window.closeBaganModal();
        }
    }
    // Keyboard shortcuts ketika modal bagan terbuka
    const baganModal = document.getElementById('baganInteractiveModal');
    if (baganModal && baganModal.classList.contains('active')) {
        if (e.key === '+' || e.key === '=') {
            const btn = document.getElementById('baganZoomInBtn');
            if (btn) btn.click();
        } else if (e.key === '-' || e.key === '_') {
            const btn = document.getElementById('baganZoomOutBtn');
            if (btn) btn.click();
        } else if (e.key === '0') {
            const btn = document.getElementById('baganZoomResetBtn');
            if (btn) btn.click();
        }
    }
});

/* -------------------------------------------------------------------
   5B. MODAL INTERAKTIF BAGAN STRUKTUR ORGANISASI (ZOOM & PAN HD)
   ------------------------------------------------------------------- */
let baganCurrentZoom = 1.0;
let baganIsDragging = false;
let baganStartX = 0;
let baganStartY = 0;
let baganScrollLeft = 0;
let baganScrollTop = 0;

window.closeBaganModal = function () {
    const modal = document.getElementById('baganInteractiveModal');
    if (modal) {
        modal.classList.remove('active');
        modal.style.display = 'none';
    }
    document.body.style.overflow = '';
};

window.openBaganModal = function () {
    let modal = document.getElementById('baganInteractiveModal');
    const BASE_W = 1060 + 32; // 1060 viewBox width + 32px padding
    const BASE_H = 710 + 32;  // 710 viewBox height + 32px padding

    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'baganInteractiveModal';
        modal.className = 'bagan-interactive-modal';
        modal.style.cssText = 'display: none; position: fixed; inset: 0; width: 100vw; height: 100vh; background: rgba(15, 23, 42, 0.96); z-index: 9999999; flex-direction: column; backdrop-filter: blur(8px);';
        modal.innerHTML = `
            <header style="display: flex; align-items: center; justify-content: space-between; padding: 10px 16px; background: #0f172a; border-bottom: 1px solid rgba(255,255,255,0.14); flex-wrap: wrap; gap: 10px; color: #ffffff; z-index: 2;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 22px;">🏛️</span>
                    <div>
                        <div style="font-size: 14px; font-weight: 800; color: #f8fafc; letter-spacing: 0.3px;">Struktur Organisasi SDN Inpres Arso VIII</div>
                        <div style="font-size: 11px; color: #94a3b8;">Tahun Ajaran 2026/2027 • Gunakan tombol zoom atau seret bagan untuk memperjelas kotak guru</div>
                    </div>
                </div>
                
                <div style="display: flex; align-items: center; gap: 6px; flex-wrap: wrap;">
                    <button type="button" id="baganZoomOutBtn" title="Perkecil (-20%)" style="background: rgba(255,255,255,0.12); color: #ffffff; border: 1px solid rgba(255,255,255,0.2); border-radius: 6px; padding: 6px 11px; font-size: 12px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 4px; transition: background 0.15s ease;">
                        <span>➖ Perkecil</span>
                    </button>
                    <span id="baganZoomBadge" style="background: rgba(30, 58, 138, 0.7); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 6px; padding: 6px 10px; font-size: 12px; font-weight: 800; min-width: 52px; text-align: center;">100%</span>
                    <button type="button" id="baganZoomInBtn" title="Perbesar (+20%)" style="background: rgba(255,255,255,0.12); color: #ffffff; border: 1px solid rgba(255,255,255,0.2); border-radius: 6px; padding: 6px 11px; font-size: 12px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 4px; transition: background 0.15s ease;">
                        <span>➕ Perbesar</span>
                    </button>
                    <button type="button" id="baganZoomResetBtn" title="Ukuran Asli Jelas (100%)" style="background: rgba(255,255,255,0.12); color: #ffffff; border: 1px solid rgba(255,255,255,0.2); border-radius: 6px; padding: 6px 11px; font-size: 12px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 4px; transition: background 0.15s ease;">
                        <span>↺ 100%</span>
                    </button>
                    <button type="button" id="baganZoomFitBtn" title="Pas di Layar" style="background: rgba(255,255,255,0.12); color: #ffffff; border: 1px solid rgba(255,255,255,0.2); border-radius: 6px; padding: 6px 11px; font-size: 12px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 4px; transition: background 0.15s ease;">
                        <span>⛶ Pas Layar</span>
                    </button>
                    <button type="button" onclick="window.closeBaganModal()" title="Tutup Tampilan Bagan (Esc)" style="background: #dc2626; color: #ffffff; border: none; border-radius: 6px; padding: 7px 15px; font-size: 12.5px; font-weight: 800; cursor: pointer; display: flex; align-items: center; gap: 6px; box-shadow: 0 2px 8px rgba(220,38,38,0.4); margin-left: 4px; transition: background 0.15s ease;">
                        <span>✕ Tutup</span>
                    </button>
                </div>
            </header>

            <div id="baganViewport" style="flex: 1; overflow: auto; -webkit-overflow-scrolling: touch; display: flex; padding: 20px; box-sizing: border-box; cursor: grab; position: relative;">
                <div id="baganCanvasWrapper" style="margin: auto; position: relative; transition: width 0.12s ease-out, height 0.12s ease-out;">
                    <div id="baganCanvasCard" style="background: #ffffff; border-radius: 12px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.55); padding: 16px; width: 1060px; height: 710px; box-sizing: content-box; transform-origin: 0 0; transition: transform 0.12s ease-out;">
                        <div id="baganModalContentHolder" style="width: 1060px; height: 710px;">
                            <img src="images/bagan-struktur-organisasi.svg" alt="Bagan Struktur Organisasi SDN Inpres Arso VIII" style="display: block; width: 1060px; height: 710px; pointer-events: none;" draggable="false">
                        </div>
                    </div>
                </div>
            </div>

            <footer style="padding: 8px 16px; background: #0b1120; border-top: 1px solid rgba(255,255,255,0.08); text-align: center; font-size: 11.5px; color: #94a3b8; pointer-events: none;">
                <span>💡 <strong>Navigasi:</strong> Klik & seret mouse untuk menggeser. Gunakan tombol zoom <strong>➕ / ➖</strong> atau tombol <strong>↺ 100%</strong> untuk memperjelas setiap kotak nama guru.</span>
            </footer>
        `;
        document.body.appendChild(modal);

        // Bind zoom handlers
        const viewport = modal.querySelector('#baganViewport');
        const wrapper = modal.querySelector('#baganCanvasWrapper');
        const card = modal.querySelector('#baganCanvasCard');
        const badge = modal.querySelector('#baganZoomBadge');

        const updateZoom = function (newZoom) {
            baganCurrentZoom = Math.min(Math.max(newZoom, 0.25), 2.5);
            card.style.transform = `scale(${baganCurrentZoom})`;
            wrapper.style.width = `${Math.round(BASE_W * baganCurrentZoom)}px`;
            wrapper.style.height = `${Math.round(BASE_H * baganCurrentZoom)}px`;
            badge.textContent = `${Math.round(baganCurrentZoom * 100)}%`;
        };

        modal.querySelector('#baganZoomInBtn').onclick = function () {
            updateZoom(baganCurrentZoom + 0.2);
        };
        modal.querySelector('#baganZoomOutBtn').onclick = function () {
            updateZoom(baganCurrentZoom - 0.2);
        };
        modal.querySelector('#baganZoomResetBtn').onclick = function () {
            updateZoom(1.0);
        };
        modal.querySelector('#baganZoomFitBtn').onclick = function () {
            if (viewport) {
                const availW = viewport.clientWidth - 40;
                const availH = viewport.clientHeight - 40;
                const fitScale = Math.min(Math.max(Math.min(availW / BASE_W, availH / BASE_H), 0.25), 1.2);
                updateZoom(fitScale);
            }
        };

        // Mouse drag to pan
        viewport.addEventListener('mousedown', function (e) {
            if (e.target.tagName === 'BUTTON') return;
            baganIsDragging = true;
            viewport.style.cursor = 'grabbing';
            viewport.style.userSelect = 'none';
            baganStartX = e.pageX - viewport.offsetLeft;
            baganStartY = e.pageY - viewport.offsetTop;
            baganScrollLeft = viewport.scrollLeft;
            baganScrollTop = viewport.scrollTop;
        });

        window.addEventListener('mousemove', function (e) {
            if (!baganIsDragging) return;
            e.preventDefault();
            const x = e.pageX - viewport.offsetLeft;
            const y = e.pageY - viewport.offsetTop;
            const walkX = (x - baganStartX);
            const walkY = (y - baganStartY);
            viewport.scrollLeft = baganScrollLeft - walkX;
            viewport.scrollTop = baganScrollTop - walkY;
        });

        window.addEventListener('mouseup', function () {
            baganIsDragging = false;
            if (viewport) {
                viewport.style.cursor = 'grab';
                viewport.style.userSelect = '';
            }
        });

        // Wheel zoom with Ctrl or trackpad pinch
        viewport.addEventListener('wheel', function (e) {
            if (e.ctrlKey || e.metaKey) {
                e.preventDefault();
                const delta = e.deltaY < 0 ? 0.1 : -0.1;
                updateZoom(baganCurrentZoom + delta);
            }
        }, { passive: false });
    }

    const viewport = modal.querySelector('#baganViewport');
    const wrapper = modal.querySelector('#baganCanvasWrapper');
    const badge = modal.querySelector('#baganZoomBadge');
    const card = modal.querySelector('#baganCanvasCard');

    // Tentukan zoom awal yang paling nyaman sesuai ukuran layar
    if (viewport) {
        const availW = (window.innerWidth || viewport.clientWidth) - 40;
        const availH = (window.innerHeight || viewport.clientHeight) - 120;
        const autoFit = Math.min(availW / BASE_W, availH / BASE_H);
        
        // Di layar desktop (>900px), gunakan pas layar atau 1.0 (mana yang lebih pas)
        // Di layar mobile (<768px), set 0.85 atau 1.0 sehingga teks nama guru langsung jelas & bisa di-swipe
        if (window.innerWidth < 768) {
            baganCurrentZoom = 0.85; // Ukuran pas untuk ponsel: sangat tajam dan mudah di-swipe
        } else {
            baganCurrentZoom = Math.min(Math.max(autoFit, 0.6), 1.0);
        }
        
        card.style.transform = `scale(${baganCurrentZoom})`;
        wrapper.style.width = `${Math.round(BASE_W * baganCurrentZoom)}px`;
        wrapper.style.height = `${Math.round(BASE_H * baganCurrentZoom)}px`;
        badge.textContent = `${Math.round(baganCurrentZoom * 100)}%`;
    }

    modal.classList.add('active');
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';

    if (viewport) {
        setTimeout(() => {
            viewport.scrollLeft = 0;
            viewport.scrollTop = 0;
        }, 50);
    }
};


/* -------------------------------------------------------------------
   GALERI FOTO PUBLIK DENGAN PAGINASI, FILTER & LIGHTBOX PERBESAR
   ------------------------------------------------------------------- */
window._allPublicGallery = [];
window._publicGalleryPage = 1;
window._publicGalleryPageSize = 9;

window.filterPublicGallery = function(targetPage) {
    if (typeof targetPage === 'number') window._publicGalleryPage = targetPage;
    const galleryGrid = document.querySelector('.gallery-grid');
    const paginationBox = document.getElementById('publicGaleriPagination');
    if (!galleryGrid) return;

    const searchInput = document.getElementById('publicGaleriSearchInput');
    const categorySelect = document.getElementById('publicGaleriCategorySelect');
    const query = (searchInput ? searchInput.value : '').trim().toLowerCase();
    const category = categorySelect ? categorySelect.value : 'ALL';

    const filtered = (window._allPublicGallery || []).filter(item => {
        const matchesQuery = !query || 
            (item.judul || '').toLowerCase().includes(query) ||
            (item.kategori || '').toLowerCase().includes(query);

        const matchesCat = category === 'ALL' || (item.kategori || '').toUpperCase().includes(category.toUpperCase());
        return matchesQuery && matchesCat;
    });

    if (filtered.length === 0) {
        galleryGrid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 45px 20px; background: #f8fafc; border-radius: 12px; border: 1.5px dashed #cbd5e1; color: #64748b;">
                <span style="font-size: 32px; display: block; margin-bottom: 8px;">📷</span>
                <strong style="color: #1e293b; font-size: 16px;">Tidak ditemukan foto kegiatan yang cocok.</strong>
                <p style="font-size: 13px; margin: 4px 0 0;">Coba kata kunci lain atau pilih "Semua Foto Dokumentasi".</p>
            </div>
        `;
        if (paginationBox) paginationBox.style.display = 'none';
        return;
    }

    const totalPages = Math.ceil(filtered.length / window._publicGalleryPageSize);
    if (window._publicGalleryPage > totalPages) window._publicGalleryPage = totalPages;
    if (window._publicGalleryPage < 1) window._publicGalleryPage = 1;

    const startIdx = (window._publicGalleryPage - 1) * window._publicGalleryPageSize;
    const pagedItems = filtered.slice(startIdx, startIdx + window._publicGalleryPageSize);

    galleryGrid.innerHTML = pagedItems.map(item => `
        <div class="gallery-item" style="cursor: pointer;" title="Klik untuk memperbesar foto">
            <img src="${item.src}" alt="${escapeHTML(item.judul)}" loading="lazy" decoding="async">
            <div class="gallery-overlay">
                <div class="gallery-cat">${escapeHTML((item.kategori || 'KEGIATAN SEKOLAH').toUpperCase())}</div>
                <div class="gallery-title">${escapeHTML(item.judul)}</div>
            </div>
        </div>
    `).join('');

    const galleryItems = galleryGrid.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
        item.addEventListener('click', function () {
            const img = this.querySelector('img');
            if (img && typeof window.openLightboxWith === 'function') {
                window.openLightboxWith(img.src, img.alt);
            }
        });
    });

    // Render Paginasi Galeri
    if (paginationBox) {
        paginationBox.style.display = 'flex';
        let buttonsHtml = '';

        buttonsHtml += `<button type="button" class="pagination-btn" ${window._publicGalleryPage <= 1 ? 'disabled' : ''} onclick="window.filterPublicGallery(${window._publicGalleryPage - 1})">◀ Sebelumnya</button>`;

        for (let p = 1; p <= totalPages; p++) {
            buttonsHtml += `<button type="button" class="pagination-btn ${p === window._publicGalleryPage ? 'active' : ''}" onclick="window.filterPublicGallery(${p})">${p}</button>`;
        }

        buttonsHtml += `<button type="button" class="pagination-btn" ${window._publicGalleryPage >= totalPages ? 'disabled' : ''} onclick="window.filterPublicGallery(${window._publicGalleryPage + 1})">Selanjutnya ▶</button>`;

        paginationBox.innerHTML = `
            <div>Menampilkan <strong>${startIdx + 1} - ${Math.min(startIdx + window._publicGalleryPageSize, filtered.length)}</strong> dari <strong>${filtered.length}</strong> koleksi foto ${query || category !== 'ALL' ? '(disaring)' : '(Arsip Tersimpan)'}</div>
            <div class="pagination-controls">${buttonsHtml}</div>
        `;
    }
};

function loadDynamicGallery() {
    const galleryGrid = document.querySelector('.gallery-grid');
    if (!galleryGrid) return;

    let items = null;
    // 1. Prioritas Utama: Google Cloud Firebase
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.galeri) && window.SDN_DATABASE.galeri.length > 0) {
        items = window.SDN_DATABASE.galeri;
    }
    // 2. Fallback: LocalStorage Cache
    if (!items) {
        try {
            const raw = localStorage.getItem('sdn_galeri_data');
            if (raw && !raw.includes('unsplash')) {
                const parsed = JSON.parse(raw);
                if (Array.isArray(parsed) && parsed.length > 0) items = parsed;
            }
        } catch (e) {}
    }

    if (items) {
        // Filter konten draft agar tidak tampil pada pengunjung publik
        items = (items || []).filter(item => item && item.status !== 'draft');
        window._allPublicGallery = items;
        window.filterPublicGallery(1);
    }
}


function initGalleryLightbox() {
    // 1. Setup handler penutup pada semua modal dan tombol close
    const allModals = document.querySelectorAll('.lightbox-modal');
    const allCloseBtns = document.querySelectorAll('.lightbox-close');

    allCloseBtns.forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            window.closeActiveLightbox();
        });
    });

    allModals.forEach(modal => {
        modal.addEventListener('click', function (e) {
            // Tutup jika klik pada area latar belakang gelap (di luar gambar)
            if (e.target === modal || e.target.classList.contains('lightbox-content')) {
                window.closeActiveLightbox();
            }
        });
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            window.closeActiveLightbox();
        }
    });

    // 2. Tampilkan galeri foto dinamis
    loadDynamicGallery();

    // 3. Pasang klik perbesar pada setiap item galeri (jika halaman memiliki gallery-item)
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
        item.addEventListener('click', function () {
            const img = this.querySelector('img');
            if (img) {
                window.openLightboxWith(img.src, img.alt);
            }
        });
    });

    // 4. Pasang klik perbesar pada foto berita (jika ada di halaman)
    const newsImgs = document.querySelectorAll('.news-img');
    newsImgs.forEach(img => {
        img.style.cursor = 'pointer';
        img.setAttribute('title', 'Klik untuk melihat foto lebih jelas');
        img.addEventListener('click', function () {
            window.openLightboxWith(this.src, this.alt);
        });
    });
}


/* -------------------------------------------------------------------
   5B. INTERAKSI HERO BANNER & ZOOM FOTO GERBANG
   ------------------------------------------------------------------- */
function initHeroInteractions() {
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

/* -------------------------------------------------------------------
   6. SIMULASI PENDAFTARAN PPDB ONLINE
   ------------------------------------------------------------------- */

/* -------------------------------------------------------------------
   5C. RENDER INFORMASI PPDB DARI PENGATURAN ADMIN
   ------------------------------------------------------------------- */
function renderPPDBPublicInfo() {
    let cfg = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && window.SDN_DATABASE.ppdb_config && typeof window.SDN_DATABASE.ppdb_config === 'object') {
        cfg = window.SDN_DATABASE.ppdb_config;
    }
    // 2. Fallback: LocalStorage Cache
    if (!cfg) {
        try {
            const raw = localStorage.getItem('sdn_ppdb_config');
            if (raw) {
                const parsed = JSON.parse(raw);
                if (parsed && typeof parsed === 'object') cfg = parsed;
            }
        } catch (e) {}
    }
    if (!cfg) return;

    try {
        const titleEl = document.getElementById('ppdbTitleDisplay');
        const badgeEl = document.getElementById('ppdbStatusBadge');
        const syaratList = document.getElementById('ppdbSyaratList');
        const waktuEl = document.getElementById('ppdbWaktuItem');
        const jamEl = document.getElementById('ppdbJamItem');
        const kuotaEl = document.getElementById('ppdbKuotaItem');
        const biayaEl = document.getElementById('ppdbBiayaItem');
        const kontakEl = document.getElementById('ppdbKontakItem');
        const formEl = document.getElementById('ppdbForm');

        if (titleEl && cfg.tahunAjaran) {
            titleEl.textContent = `PPDB SD Negeri Inpres Arso VIII`;
        }

        if (badgeEl) {
            if (cfg.status === 'TUTUP') {
                badgeEl.style.background = '#dc2626';
                badgeEl.style.color = '#ffffff';
                badgeEl.textContent = '🔴 PENDAFTARAN PPDB DITUTUP';
            } else {
                badgeEl.style.background = '#16a34a';
                badgeEl.style.color = '#ffffff';
                badgeEl.textContent = '🟢 PENDAFTARAN PPDB DIBUKA';
            }
        }

        if (waktuEl && cfg.jadwal) {
            waktuEl.innerHTML = `<strong>Waktu Pendaftaran:</strong> ${cfg.jadwal}`;
        }
        if (jamEl && cfg.jamPelayanan) {
            jamEl.innerHTML = `<strong>Jam Pelayanan:</strong> ${cfg.jamPelayanan}`;
        }
        if (kuotaEl && cfg.kuota) {
            kuotaEl.innerHTML = `<strong>Kuota Kelas I:</strong> ${cfg.kuota}`;
        }
        if (biayaEl && cfg.biaya) {
            biayaEl.innerHTML = `<strong>Biaya Pendaftaran:</strong> <span style="color: #16a34a; font-weight: 800;">${cfg.biaya}</span>`;
        }
        if (kontakEl && cfg.kontak) {
            kontakEl.innerHTML = `<strong>Narahubung Panitia:</strong> ${cfg.kontak}`;
        }

        // Syarat
        if (syaratList && cfg.syarat) {
            const lines = cfg.syarat.split('\n').map(l => l.trim()).filter(l => l.length > 0);
            if (lines.length > 0) {
                syaratList.innerHTML = lines.map(line => `<li>${line}</li>`).join('');
            }
        }

        // Jika status TUTUP, tampilkan peringatan di atas form & disable tombol kirim
        if (formEl) {
            let notice = document.getElementById('ppdbClosedNotice');
            const submitBtn = formEl.querySelector('button[type="submit"]');

            if (cfg.status === 'TUTUP') {
                if (!notice) {
                    notice = document.createElement('div');
                    notice.id = 'ppdbClosedNotice';
                    notice.style.background = '#fee2e2';
                    notice.style.border = '2px solid #ef4444';
                    notice.style.color = '#991b1b';
                    notice.style.padding = '16px';
                    notice.style.borderRadius = '8px';
                    notice.style.textAlign = 'center';
                    notice.style.fontWeight = '700';
                    notice.style.marginBottom = '20px';
                    notice.innerHTML = '⚠️ Pendaftaran Peserta Didik Baru (PPDB) saat ini sedang ditutup. Silakan nantikan pembukaan gelombang berikutnya atau hubungi pihak sekolah.';
                    formEl.parentNode.insertBefore(notice, formEl);
                }
                if (submitBtn) {
                    submitBtn.disabled = true;
                    submitBtn.style.opacity = '0.5';
                    submitBtn.style.cursor = 'not-allowed';
                    submitBtn.textContent = '⛔ Pendaftaran Saat Ini Ditutup';
                }
            } else {
                if (notice) notice.remove();
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.style.opacity = '1';
                    submitBtn.style.cursor = 'pointer';
                    submitBtn.textContent = '🚀 Kirim Pendaftaran & Dapatkan Bukti Registrasi';
                }
            }
        }
    } catch (e) {
        console.error('Error rendering PPDB public info:', e);
    }
}

function initPPDBForm() {
    const ppdbForm = document.getElementById('ppdbForm');
    const resultBox = document.getElementById('ppdbResult');

    if (!ppdbForm) return;

    ppdbForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Verifikasi Anti-Bot Manusia
        const honeypot = document.getElementById('ppdbHoneypot')?.value;
        const answer = parseInt(document.getElementById('ppdbCaptchaAnswer')?.value || '0', 10);
        if (honeypot || answer !== window._ppdbExpectedCaptcha) {
            alert('❌ Verifikasi Keamanan: Jawaban penjumlahan tidak sesuai. Silakan hitung kembali untuk memverifikasi pendaftar asli.');
            initPPDBHumanCaptcha();
            return;
        }

        const nama = document.getElementById('ppdbNama')?.value || 'Calon Siswa';
        const ttl = document.getElementById('ppdbTtl')?.value || '-';
        const gender = document.getElementById('ppdbGender')?.value || '-';
        const orangtua = document.getElementById('ppdbOrtu')?.value || '-';
        const alamat = document.getElementById('ppdbAlamat')?.value || '-';
        const nohp = document.getElementById('ppdbHp')?.value || '-';
        const regId = 'PPDB-' + Math.floor(100000 + Math.random() * 900000);
        const tglDaftar = new Date().toLocaleDateString('id-ID', {
            day: 'numeric',
            month: 'long',
            year: 'numeric'
        });

        const newSubmission = {
            id: regId,
            tgl: tglDaftar,
            nama: nama,
            gender: gender,
            ttl: ttl,
            ortu: orangtua,
            hp: nohp,
            alamat: alamat,
            status: "Menunggu Berkas"
        };

        // Simpan otomatis ke penyimpanan lokal browser pendaftar
        try {
            const raw = localStorage.getItem('sdn_ppdb_submissions');
            const list = raw ? JSON.parse(raw) : [];
            list.unshift(newSubmission);
            localStorage.setItem('sdn_ppdb_submissions', JSON.stringify(list));
        } catch (err) {
            console.log('Local storage error', err);
        }

        // Simpan langsung ke Google Cloud agar Admin Sekolah seketika menerima data pendaftar baru
        if (typeof fetch === 'function') {
            fetch('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/ppdb_submissions.json')
                .then(r => r.json())
                .then(cloudList => {
                    const merged = Array.isArray(cloudList) ? cloudList : [];
                    merged.unshift(newSubmission);
                    return fetch('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/ppdb_submissions.json', {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(merged)
                    });
                })
                .catch(err => console.warn('PPDB cloud sync warning:', err));
        }

        if (resultBox) {
            resultBox.innerHTML = `
                <div style="background: #ecfdf5; border: 2px solid #10b981; border-radius: 12px; padding: 25px; margin-top: 25px;">
                    <div style="text-align: center; margin-bottom: 20px;">
                        <span style="background: #10b981; color: white; padding: 4px 14px; border-radius: 9999px; font-size: 12px; font-weight: 700;">PENDAFTARAN BERHASIL DISIMPAN</span>
                        <h3 style="color: #065f46; margin-top: 10px; font-size: 20px;">Bukti Pendaftaran Sementara PPDB</h3>
                        <p style="font-size: 13px; color: #047857;">SD NEGERI INPRES ARSO VIII - KABUPATEN KEEROM</p>
                    </div>
                    <table style="width: 100%; border-collapse: collapse; font-size: 13.5px; margin-bottom: 20px;">
                        <tr style="border-bottom: 1px solid #d1fae5;"><td style="padding: 8px; font-weight: bold; width: 150px;">Nomor Registrasi</td><td style="padding: 8px; font-weight: 800; color: #065f46;">${regId}</td></tr>
                        <tr style="border-bottom: 1px solid #d1fae5;"><td style="padding: 8px; font-weight: bold;">Tanggal Daftar</td><td style="padding: 8px;">${tglDaftar}</td></tr>
                        <tr style="border-bottom: 1px solid #d1fae5;"><td style="padding: 8px; font-weight: bold;">Nama Calon Siswa</td><td style="padding: 8px;">${nama}</td></tr>
                        <tr style="border-bottom: 1px solid #d1fae5;"><td style="padding: 8px; font-weight: bold;">Tempat / Tgl Lahir</td><td style="padding: 8px;">${ttl}</td></tr>
                        <tr style="border-bottom: 1px solid #d1fae5;"><td style="padding: 8px; font-weight: bold;">Jenis Kelamin</td><td style="padding: 8px;">${gender}</td></tr>
                        <tr style="border-bottom: 1px solid #d1fae5;"><td style="padding: 8px; font-weight: bold;">Nama Orang Tua / Wali</td><td style="padding: 8px;">${orangtua}</td></tr>
                        <tr style="border-bottom: 1px solid #d1fae5;"><td style="padding: 8px; font-weight: bold;">Alamat Tempat Tinggal</td><td style="padding: 8px;">${alamat}</td></tr>
                        <tr><td style="padding: 8px; font-weight: bold;">No. WhatsApp / Telepon</td><td style="padding: 8px;">${nohp}</td></tr>
                    </table>
                    <div style="background: #ffffff; padding: 14px; border-radius: 8px; font-size: 12.5px; color: #475569; margin-bottom: 20px; border-left: 4px solid #10b981;">
                        <strong>Catatan untuk Orang Tua / Wali:</strong><br>
                        Silakan bawa bukti ini beserta fotokopi Akta Kelahiran dan Kartu Keluarga (KK) ke kantor SDN Inpres Arso VIII (Jln. Sulawesi, Kampung Dukwia, Arso Barat) atau konfirmasi melalui WhatsApp ke <strong>0812-4821-9125</strong>.
                    </div>
                    <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                        <button onclick="window.print()" class="btn btn-primary" style="padding: 8px 18px; font-size: 13px;">🖨️ Cetak Bukti Pendaftaran</button>
                        <a href="https://wa.me/6281248219125?text=Halo%20Panitia%20PPDB%20SDN%20Inpres%20Arso%20VIII,%20saya%20sudah%20mendaftar%20online%20dengan%20No.%20Registrasi%20${regId}%20atas%20nama%20${encodeURIComponent(nama)}." target="_blank" class="btn" style="background: #25d366; color: white; padding: 8px 18px; font-size: 13px;">💬 Konfirmasi via WhatsApp</a>
                    </div>
                </div>
            `;
            resultBox.scrollIntoView({ behavior: 'smooth' });
        }
    });
}

/* -------------------------------------------------------------------
   7. FORMULIR KONTAK INTERAKTIF & WHATSAPP DIRECT
   ------------------------------------------------------------------- */
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return;

    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Verifikasi Anti-Bot Manusia
        const honeypot = document.getElementById('contactHoneypot')?.value;
        const answer = parseInt(document.getElementById('contactCaptchaAnswer')?.value || '0', 10);
        if (honeypot || answer !== window._contactExpectedCaptcha) {
            alert('❌ Verifikasi Keamanan: Jawaban penjumlahan tidak sesuai. Silakan hitung kembali untuk memverifikasi pengirim asli.');
            initContactHumanCaptcha();
            return;
        }

        const nama = document.getElementById('contactName')?.value || '';
        const phone = document.getElementById('contactPhone')?.value || '';
        const subject = document.getElementById('contactSubject')?.value || 'Pertanyaan';
        const message = document.getElementById('contactMessage')?.value || '';

        // Simpan pesan ke Google Cloud Firebase Database agar terbaca di Admin
        const newMsg = {
            id: 'MSG-' + Date.now(),
            nama: nama,
            telepon: phone,
            subjek: subject,
            pesan: message,
            tanggal: new Date().toLocaleDateString('id-ID', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' }) + ' WIT',
            status: 'Belum Ditanggapi'
        };
        if (typeof fetch === 'function') {
            const msgUrl = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/pesan_kontak.json';
            fetch(msgUrl)
                .then(r => r.json())
                .then(list => {
                    const arr = Array.isArray(list) ? list : [];
                    arr.unshift(newMsg);
                    return fetch(msgUrl, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(arr)
                    });
                })
                .catch(err => console.warn('Pesan kontak save error:', err));
        }

        // Tampilkan pesan sukses
        alert(`Terima kasih, Bapak/Ibu ${nama}!\nPesan Anda telah diterima oleh SDN Inpres Arso VIII. Kami akan segera menghubungi Anda melalui nomor ${phone}.`);

        // Tanyakan apakah ingin langsung lanjut ke WhatsApp
        const waPrompt = confirm('Apakah Anda ingin langsung meneruskan pesan ini ke WhatsApp resmi SDN Inpres Arso VIII?');
        if (waPrompt) {
            const waText = encodeURIComponent(
                `Halo SDN Inpres Arso VIII,\n\nNama: ${nama}\nNo. HP: ${phone}\nPerihal: ${subject}\n\nPesan:\n${message}`
            );
            window.open(`https://wa.me/6281248219125?text=${waText}`, '_blank');
        }

        contactForm.reset();
    });
}

/* -------------------------------------------------------------------
   8. AKTIFKAN MENU NAVIGASI SESUAI HALAMAN YANG SEDANG DIBUKA
   ------------------------------------------------------------------- */
function highlightActiveNavLink() {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('nav.main-nav .nav-link, nav.main-nav .nav-dropdown-item');
    const dropdownToggle = document.querySelector('.nav-dropdown-toggle');

    const profilePages = ['profil.html', 'guru.html', 'siswa.html', 'sapras.html', 'sop.html'];
    if (dropdownToggle) {
        if (profilePages.includes(currentPath)) {
            dropdownToggle.classList.add('active');
        } else {
            dropdownToggle.classList.remove('active');
        }
    }

    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (currentPath === '' && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

/* -------------------------------------------------------------------
   9. MUAT PENGUMUMAN DINAMIS DARI DASHBOARD ADMIN
   ------------------------------------------------------------------- */
function loadDynamicAnnouncements() {
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
        // Filter konten draft agar tidak tampil pada pengunjung publik
        items = (items || []).filter(item => item && item.status !== 'draft');

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

/* -------------------------------------------------------------------
   10. SINKRONISASI BERITA DINAMIS (DARI ADMIN LOCALSTORAGE)
   ------------------------------------------------------------------- */
const defaultMainNewsList = [
    {
        id: 1,
        judul: "Komitmen Bersama Pendidik SDN Inpres Arso VIII Menyambut Tahun Ajaran Baru",
        kategori: "Karakter & Budi Pekerti",
        penulis: "Tim Humas Sekolah",
        tanggal: "05 November 2026",
        foto: "images/gerbang-sekolah.jpg",
        snippet: "Kepala Sekolah Adi Puspito, S.Pd bersama 11 tenaga pendidik berfoto bersama di depan Gapura Resmi SDN Inpres Arso VIII. Seluruh dewan guru berkomitmen mewujudkan mutu pendidikan berkualitas, berakhlak mulia, dan unggul IPTEK di Kabupaten Keerom.",
        isi: "Kepala Sekolah Adi Puspito, S.Pd bersama 11 tenaga pendidik berfoto bersama di depan Gapura Resmi SDN Inpres Arso VIII. Seluruh dewan guru berkomitmen mewujudkan mutu pendidikan berkualitas, berakhlak mulia, dan unggul IPTEK di Kabupaten Keerom. Melalui kebersamaan dan kerja sama dengan orang tua serta Komite Sekolah, SDN Inpres Arso VIII terus berbenah menghadirkan lingkungan belajar yang aman, nyaman, dan berdaya saing."
    },
    {
        id: 2,
        judul: "Pemanfaatan Jaringan Starlink untuk Simulasi ANBK & Pembelajaran Komputer",
        kategori: "Teknologi & ANBK",
        penulis: "Tim IT Sekolah",
        tanggal: "02 November 2026",
        foto: "images/kegiatan-anbk-komputer.jpg",
        snippet: "Siswa kelas V dan VI mulai mengenal asesmen digital dan pencarian materi sains menggunakan fasilitas internet satelit Starlink di ruang TIK sekolah.",
        isi: "Pemanfaatan jaringan internet satelit Starlink dan modem Telkomsel Orbit di SDN Inpres Arso VIII memberikan kemudahan bagi dewan guru dan siswa kelas tinggi dalam mengakses bank soal ANBK, portal Kemendikbudristek, serta materi pembelajaran interaktif berbasis multimedia."
    },
    {
        id: 3,
        judul: "Semarak Senam Kebugaran Jasmani dan Olahraga Bersama Seluruh Siswa & Guru",
        kategori: "Kesehatan & Olahraga",
        penulis: "Ferdinand, S.Pd",
        tanggal: "28 Oktober 2026",
        foto: "images/kegiatan-senam-bersama.jpg",
        snippet: "Menjaga kebugaran jasmani dan membina kekompakan antar murid, SDN Inpres Arso VIII menyelenggarakan agenda senam irama ceria rutin setiap hari Jumat.",
        isi: "Kegiatan senam pagi bersama dipimpin oleh Guru Penjaskes Bapak Ferdinand, S.Pd dan diikuti oleh seluruh siswa dari Kelas I hingga Kelas VI serta segenap dewan guru. Olahraga rutin ini terbukti meningkatkan semangat dan daya konsentrasi siswa dalam mengikuti proses belajar mengajar."
    },
    {
        id: 4,
        judul: "Pembinaan Rohani dan Peringatan Hari Besar Keagamaan Siswa",
        kategori: "Karakter & Budi Pekerti",
        penulis: "Dewan Guru Agama",
        tanggal: "24 Oktober 2026",
        foto: "images/kegiatan-keagamaan-rohani.jpg",
        snippet: "Menjunjung tinggi toleransi dan keberagaman, sekolah membina keimanan siswa melalui pembagian kelas keagamaan Islam, Kristen Protestan, dan Katolik secara intensif.",
        isi: "SDN Inpres Arso VIII mengedepankan pembentukan budi pekerti luhur bagi seluruh generasi muda. Setiap pekan, guru agama Islam, Kristen Protestan, dan Katolik membimbing para siswa sesuai keyakinan masing-masing dalam suasana persaudaraan yang damai dan toleran di Tanah Papua."
    }
];


/* -------------------------------------------------------------------
   10. SINKRONISASI BERITA & ARSIP RESMI PUBLIK (PAGINASI & FILTER)
   ------------------------------------------------------------------- */
window._allPublicNews = [];
window._publicNewsPage = 1;
window._publicNewsPageSize = 6;

window.filterPublicNews = function(targetPage) {
    if (typeof targetPage === 'number') window._publicNewsPage = targetPage;
    const beritaGrid = document.getElementById('beritaListGrid');
    const paginationBox = document.getElementById('publicBeritaPagination');
    if (!beritaGrid) return;

    const searchInput = document.getElementById('publicBeritaSearchInput');
    const categorySelect = document.getElementById('publicBeritaCategorySelect');
    const query = (searchInput ? searchInput.value : '').trim().toLowerCase();
    const category = categorySelect ? categorySelect.value : 'ALL';

    const filtered = (window._allPublicNews || []).filter(item => {
        const matchesQuery = !query || 
            (item.judul || '').toLowerCase().includes(query) ||
            (item.snippet || '').toLowerCase().includes(query) ||
            (item.penulis || '').toLowerCase().includes(query) ||
            (item.tanggal || '').toLowerCase().includes(query) ||
            (item.kategori || '').toLowerCase().includes(query);

        const matchesCat = category === 'ALL' || (item.kategori || '').toLowerCase().includes(category.toLowerCase());
        return matchesQuery && matchesCat;
    });

    if (filtered.length === 0) {
        beritaGrid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 45px 20px; background: #f8fafc; border-radius: 12px; border: 1.5px dashed #cbd5e1; color: #64748b;">
                <span style="font-size: 32px; display: block; margin-bottom: 8px;">🔍</span>
                <strong style="color: #1e293b; font-size: 16px;">Tidak ditemukan arsip berita yang sesuai.</strong>
                <p style="font-size: 13px; margin: 4px 0 0;">Coba kata kunci pencarian lain atau pilih "Semua Kategori" untuk melihat kembali seluruh arsip.</p>
            </div>
        `;
        if (paginationBox) paginationBox.style.display = 'none';
        return;
    }

    const totalPages = Math.ceil(filtered.length / window._publicNewsPageSize);
    if (window._publicNewsPage > totalPages) window._publicNewsPage = totalPages;
    if (window._publicNewsPage < 1) window._publicNewsPage = 1;

    const startIdx = (window._publicNewsPage - 1) * window._publicNewsPageSize;
    const pagedItems = filtered.slice(startIdx, startIdx + window._publicNewsPageSize);

    beritaGrid.innerHTML = '';
    pagedItems.forEach(item => {
        const card = document.createElement('div');
        card.className = 'news-card';
        const imgThumb = item.foto || 'images/gerbang-sekolah.jpg';
        card.innerHTML = `
            <div class="news-img-holder">
                <img src="${imgThumb}" alt="${escapeHTML(item.judul)}" class="news-img" decoding="async" loading="lazy">
                <span class="news-tag" style="background: var(--secondary);">${escapeHTML(item.kategori || 'Kegiatan')}</span>
            </div>
            <div class="news-body">
                <div class="news-date">📅 ${escapeHTML(item.tanggal)} | Oleh: ${escapeHTML(item.penulis || 'Humas Sekolah')}</div>
                <h3 class="news-title">
                    <a href="javascript:void(0)" onclick="if(window.openLightboxWith) window.openLightboxWith('${imgThumb}', '${escapeHTML(item.judul)}')">${escapeHTML(item.judul)}</a>
                </h3>
                <p class="news-snippet">${escapeHTML(item.snippet || '')}</p>
                ${item.isi && item.isi !== item.snippet ? `<div style="font-size: 13.5px; color: #475569; line-height: 1.6; margin-top: 10px; border-top: 1px dashed #e2e8f0; padding-top: 10px;">${escapeHTML(item.isi)}</div>` : ''}
                <div style="margin-top: 14px;">
                    <button type="button" class="btn btn-secondary" style="font-size: 11.5px; padding: 6px 14px; font-weight: 700;" onclick="if(window.openLightboxWith) window.openLightboxWith('${imgThumb}', '${escapeHTML(item.judul)}')">
                        🔍 Lihat Foto Dokumentasi
                    </button>
                </div>
            </div>
        `;
        // Klik pada gambar untuk perbesar tajam di lightbox
        const imgEl = card.querySelector('.news-img');
        if (imgEl) {
            imgEl.style.cursor = 'zoom-in';
            imgEl.addEventListener('click', function() {
                if (typeof window.openLightboxWith === 'function') {
                    window.openLightboxWith(imgThumb, item.judul);
                }
            });
        }
        beritaGrid.appendChild(card);
    });

    // Render Paginasi Berita
    if (paginationBox) {
        paginationBox.style.display = 'flex';
        let buttonsHtml = '';

        buttonsHtml += `<button type="button" class="pagination-btn" ${window._publicNewsPage <= 1 ? 'disabled' : ''} onclick="window.filterPublicNews(${window._publicNewsPage - 1})">◀ Sebelumnya</button>`;

        for (let p = 1; p <= totalPages; p++) {
            buttonsHtml += `<button type="button" class="pagination-btn ${p === window._publicNewsPage ? 'active' : ''}" onclick="window.filterPublicNews(${p})">${p}</button>`;
        }

        buttonsHtml += `<button type="button" class="pagination-btn" ${window._publicNewsPage >= totalPages ? 'disabled' : ''} onclick="window.filterPublicNews(${window._publicNewsPage + 1})">Selanjutnya ▶</button>`;

        paginationBox.innerHTML = `
            <div>Menampilkan <strong>${startIdx + 1} - ${Math.min(startIdx + window._publicNewsPageSize, filtered.length)}</strong> dari <strong>${filtered.length}</strong> total berita ${query || category !== 'ALL' ? '(disaring)' : '(Arsip Tersimpan)'}</div>
            <div class="pagination-controls">${buttonsHtml}</div>
        `;
    }
};

function loadDynamicNews() {
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
    // Filter konten draft agar tidak tampil pada pengunjung publik
    newsData = (newsData || []).filter(item => item && item.status !== 'draft');
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
                    <img src="${photo}" alt="${safeTitle}" class="showcase-slide-img" onclick="if(window.openLightboxWith){ window.openLightboxWith('${photo.replace(/'/g, "\'")}', '${safeTitle}'); }" title="Klik untuk memperbesar foto berita" decoding="async" loading="${idx === 0 ? 'eager' : 'lazy'}">
                </div>
                <div class="school-photo-caption">
                    <div>
                        <span class="showcase-category-pill" style="background: ${color}; color: white;">${icon} ${escapeHTML(categoryName)}</span>
                        <h3 class="showcase-slide-title">${safeTitle}</h3>
                        <p class="showcase-slide-desc">${escapeHTML(cleanSnippet)}</p>
                    </div>
                    <div class="showcase-btn-group">
                        <button type="button" class="btn btn-showcase-zoom" onclick="if(window.openLightboxWith){ window.openLightboxWith('${photo.replace(/'/g, "\'")}', '${safeTitle}'); }">🔍 Perbesar Foto</button>
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
    initKKGShowcaseSlider();
}

/* -------------------------------------------------------------------
   10B. SINKRONISASI SAMBUTAN KEPALA SEKOLAH DINAMIS (BERANDA / INDEX.HTML)
   ------------------------------------------------------------------- */
const defaultMainSambutan = {
    nama: "Adi Puspito, S.Pd",
    jabatan: "Kepala Sekolah SDN Inpres Arso VIII (Pembina Utama Muda, IV/c)",
    judul: "Mendidik dengan Hati, Merajut Asa di Ujung Timur Nusantara",
    foto: "images/kepala-sekolah.jpg",
    isi: "Tabea, Salam Sejahtera, Assalamu'alaikum Warahmatullahi Wabarakatuh.\n\nPuji syukur kita panjatkan ke hadirat Tuhan Yang Maha Esa atas tersedianya website resmi SD Negeri Inpres Arso VIII. Terletak di Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, sekolah kami terus berikhtiar memberikan layanan pendidikan terbaik yang merata bagi seluruh anak didik tanpa membedakan latar belakang suku, agama, dan budaya.\n\nWalaupun berada di daerah perbatasan dengan keterbatasan sarana prasarana yang sedang kami terus upayakan peningkatannya, kami bersyukur telah difasilitasi dengan koneksi internet satelit Starlink dan Telkomsel Orbit. Hal ini memacu semangat anak-anak dan para dewan guru untuk tidak tertinggal dalam penguasaan literasi digital dan teknologi informasi modern.\n\nMari bersama-sama komite sekolah, para orang tua, dan masyarakat Kampung Dukwia kita jaga dan bimbing anak-anak kita menjadi generasi yang beriman, berbudi pekerti luhur, sehat jasmani, dan mencintai lingkungan hidup."
};

function loadDynamicSambutan() {
    let data = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && window.SDN_DATABASE.sambutan && typeof window.SDN_DATABASE.sambutan === 'object' && (window.SDN_DATABASE.sambutan.nama || window.SDN_DATABASE.sambutan.isi)) {
        data = Object.assign({}, defaultMainSambutan, window.SDN_DATABASE.sambutan);
    }
    // 2. Fallback: LocalStorage Cache
    if (!data) {
        try {
            const raw = localStorage.getItem('sdn_sambutan_data');
            if (raw) {
                const parsed = JSON.parse(raw);
                if (parsed && (parsed.nama || parsed.foto || parsed.isi)) {
                    data = Object.assign({}, defaultMainSambutan, parsed);
                }
            }
        } catch (e) {}
    }

    // 3. Fallback bawaan
    if (!data) data = defaultMainSambutan;

    const fotoEl = document.getElementById('sambutanFoto');
    const badgeEl = document.getElementById('sambutanBadge');
    const judulEl = document.getElementById('sambutanJudul');
    const isiWrapper = document.getElementById('sambutanIsiWrapper');
    const namaEl = document.getElementById('sambutanNama');
    const jabatanEl = document.getElementById('sambutanJabatan');

    if (fotoEl && data.foto) fotoEl.src = data.foto;
    if (badgeEl && data.nama) badgeEl.textContent = `${data.nama} (Kepala Sekolah)`;
    if (judulEl && data.judul) judulEl.textContent = data.judul;
    if (namaEl && data.nama) namaEl.textContent = data.nama;
    if (jabatanEl && data.jabatan) jabatanEl.textContent = data.jabatan;

    if (isiWrapper && data.isi) {
        const paragraphs = data.isi.split(/\n\s*\n/).filter(p => p.trim().length > 0);
        isiWrapper.innerHTML = '';
        paragraphs.forEach((p, idx) => {
            const pEl = document.createElement('p');
            if (idx === 0 && (p.toLowerCase().includes('tabea') || p.toLowerCase().includes('assalamu') || p.toLowerCase().includes('salam'))) {
                pEl.innerHTML = `<em>${escapeHTML(p)}</em>`;
            } else {
                pEl.innerHTML = escapeHTML(p)
                    .replace(/SD Negeri Inpres Arso VIII/g, '<strong>SD Negeri Inpres Arso VIII</strong>')
                    .replace(/Starlink/g, '<strong>Starlink</strong>')
                    .replace(/Telkomsel Orbit/g, '<strong>Telkomsel Orbit</strong>');
            }
            isiWrapper.appendChild(pEl);
        });
    }
}


/* -------------------------------------------------------------------
   11. SINKRONISASI DATA DEWAN GURU DINAMIS (DARI ADMIN LOCALSTORAGE)
   ------------------------------------------------------------------- */
const defaultMainGuruList = [
    { id: 1, nama: "Adi Puspito, S.Pd", nip: "196702141992031009", jabatan: "Kepala Sekolah", status: "PNS", gol: "Pembina Utama Muda, IV/c", ttl: "Banyuwangi, 14-02-1967", nuptk: "4546745649200010", foto: "images/kepala-sekolah.jpg" },
    { id: 7, nama: "Yuli Syetia Sari, S.Pd", nip: "199203132022212024", jabatan: "Guru Kelas I", status: "P3K", gol: "Golongan IX", ttl: "Jayapura, 13-03-1992", nuptk: "8645770671230192", foto: "images/guru-yuli.jpg" },
    { id: 3, nama: "Elias Tabuni, S.Pd", nip: "196903091993011001", jabatan: "Guru Kelas II", status: "PNS", gol: "Pembina Utama Muda, IV/c", ttl: "Pyramit, 09-03-1969", nuptk: "3641747652200002", foto: "images/guru-elias.jpg" },
    { id: 12, nama: "Rita Paulina Wabiser, S.Pd", nip: "-", jabatan: "Guru Kelas III", status: "Honor", gol: "-", ttl: "Biak, 18-07-1997", nuptk: "-", foto: "images/guru-rita.jpg" },
    { id: 2, nama: "Warno, S.Pd.SD", nip: "197206061993051001", jabatan: "Guru Kelas IV", status: "PNS", gol: "Pembina Utama Muda, IV/c", ttl: "Ponorogo, 06-06-1972", nuptk: "1938750652200032", foto: "images/guru-warno.jpg" },
    { id: 5, nama: "Rini Handayani, S.Pd", nip: "198408042015072002", jabatan: "Guru Kelas V", status: "PNS", gol: "Penata Muda Tk.I, III/b", ttl: "Ponorogo, 04-08-1984", nuptk: "6136762665300023", foto: "images/guru-rini.jpg" },
    { id: 6, nama: "Cicik Mursidah, S.Pd", nip: "199512062020122023", jabatan: "Guru Kelas VI", status: "PNS", gol: "Penata Muda, III/a", ttl: "Bojonegoro, 06-12-1995", nuptk: "8538773674230073", foto: "images/guru-cicik.jpg" },
    { id: 4, nama: "Ferdinand, S.Pd", nip: "197305281997111001", jabatan: "Guru Penjaskes / PJOK", status: "PNS", gol: "Pembina Tk.I, IV/b", ttl: "Abepura, 28-05-1973", nuptk: "7860751653200002", foto: "images/guru-ferdinand.jpg" },
    { id: 8, nama: "Zainal Habiib Al Arif, S.Pd", nip: "199707062024211013", jabatan: "Guru Pendidikan Agama Islam", status: "P3K", gol: "Golongan IX", ttl: "Arso, 06-07-1997", nuptk: "2038775676130133", foto: "images/guru-zainal.jpg" },
    { id: 9, nama: "Flavianus Rainaldus, S.Ag", nip: "-", jabatan: "Guru Pendidikan Agama Katolik", status: "Honor", gol: "-", ttl: "Bebot, 15-05-1990", nuptk: "3847768669130452", foto: "images/guru-flavianus.jpg" },
    { id: 10, nama: "Esther Tina Maria Panjaitan, S.Pd", nip: "-", jabatan: "Guru Pendidikan Agama Protestan", status: "Honor", gol: "-", ttl: "Ujung Bandar, 20-10-1988", nuptk: "0352766667230403", foto: "images/guru-esther.jpg" },
    { id: 11, nama: "Umi Wildana Zulfa", nip: "-", jabatan: "Guru Bahasa Inggris", status: "Honor", gol: "-", ttl: "Keerom, 23-07-2001", nuptk: "5055779680230013", foto: "images/guru-umi.jpg" }
];

/* -------------------------------------------------------------------
   SINKRONISASI CERDAS BAGAN STRUKTUR ORGANISASI SEKOLAH DENGAN DATA GURU
   Mendukung: 1) Upload Gambar Bagan Baru & 2) Konek Otomatis Susunan Guru
   ------------------------------------------------------------------- */
function syncBaganStrukturOrganisasi(teachers) {
    const customContainer = document.getElementById('baganCustomImageContainer');
    const customImg = document.getElementById('baganCustomImg');
    const svgContainer = document.getElementById('baganSvgContainer');

    // 1. Periksa apakah ada berkas gambar bagan kustom yang diunggah dari Halaman Admin
    let customBagan = '';
    if (window.SDN_DATABASE && window.SDN_DATABASE.bagan_struktur) {
        customBagan = window.SDN_DATABASE.bagan_struktur;
    } else {
        try {
            customBagan = localStorage.getItem('sdn_bagan_struktur') || '';
        } catch (e) {}
    }

    if (customBagan && customBagan.length > 50) {
        if (customContainer) customContainer.style.display = 'block';
        if (customImg) customImg.src = customBagan;
        if (svgContainer) svgContainer.style.display = 'none';
        window._currentActiveBaganSrc = customBagan;
        return;
    } else {
        if (customContainer) customContainer.style.display = 'none';
        if (svgContainer) svgContainer.style.display = 'block';
        window._currentActiveBaganSrc = 'images/bagan-struktur-organisasi.svg';
    }

    // 2. Jika mode Bagan Vektor Interaktif: Sinkronkan nama-nama guru secara otomatis dari database
    if (!Array.isArray(teachers) || teachers.length === 0) return;

    function findTeacher(pattern) {
        const regex = new RegExp(pattern, 'i');
        return teachers.find(t => regex.test(t.jabatan || '')) || null;
    }

    function formatSvgName(fullName, centerX, isSmallBox) {
        if (!fullName) return '';
        const name = fullName.trim();
        const threshold = isSmallBox ? 16 : 19;
        if (name.length > threshold && name.includes(' ')) {
            const spaces = [];
            for (let i = 0; i < name.length; i++) {
                if (name[i] === ' ') spaces.push(i);
            }
            if (spaces.length > 0) {
                const mid = name.length / 2.0;
                let bestIdx = spaces[0];
                let minDiff = Math.abs(bestIdx - mid);
                for (let j = 1; j < spaces.length; j++) {
                    const diff = Math.abs(spaces[j] - mid);
                    if (diff < minDiff) {
                        minDiff = diff;
                        bestIdx = spaces[j];
                    }
                }
                const s1 = name.slice(0, bestIdx);
                const s2 = name.slice(bestIdx + 1);
                return `<tspan x="${centerX}" y="27">${escapeHTML(s1)}</tspan><tspan x="${centerX}" y="43">${escapeHTML(s2)}</tspan>`;
            }
        }
        const y = isSmallBox ? '33' : '32';
        return `<tspan x="${centerX}" y="${y}">${escapeHTML(name)}</tspan>`;
    }

    function updateTextEl(id, teacher, centerX, isSmallBox) {
        const el = document.getElementById(id);
        if (el && teacher && teacher.nama) {
            el.innerHTML = formatSvgName(teacher.nama, centerX, isSmallBox);
        }
    }

    const tKepsek = findTeacher('kepala\\s*sekolah') || teachers.find(t => t.id === 1);
    const tKelas1 = findTeacher('kelas\\s*1|kelas\\s*i\\b');
    const tKelas2 = findTeacher('kelas\\s*2|kelas\\s*ii\\b');
    const tKelas3 = findTeacher('kelas\\s*3|kelas\\s*iii\\b');
    const tKelas4 = findTeacher('kelas\\s*4|kelas\\s*iv\\b');
    const tKelas5 = findTeacher('kelas\\s*5|kelas\\s*v\\b');
    const tKelas6 = findTeacher('kelas\\s*6|kelas\\s*vi\\b');
    const tPenjas = findTeacher('penjas|pjok|olahraga');
    const tAgIslam = findTeacher('islam');
    const tAgKristen = findTeacher('protestan|kristen');
    const tAgKatolik = findTeacher('katolik');

    updateTextEl('baganSvgNamaKepsek', tKepsek, 130, false);
    updateTextEl('baganSvgNamaKelas1', tKelas1, 125, false);
    updateTextEl('baganSvgNamaKelas2', tKelas2, 125, false);
    updateTextEl('baganSvgNamaKelas3', tKelas3, 125, false);
    updateTextEl('baganSvgNamaKelas4', tKelas4, 125, false);
    updateTextEl('baganSvgNamaKelas5', tKelas5, 125, false);
    updateTextEl('baganSvgNamaKelas6', tKelas6, 125, false);
    updateTextEl('baganSvgNamaPenjas', tPenjas, 107.5, true);
    updateTextEl('baganSvgNamaAgIslam', tAgIslam, 107.5, true);
    updateTextEl('baganSvgNamaAgKristen', tAgKristen, 107.5, true);
    updateTextEl('baganSvgNamaAgKatolik', tAgKatolik, 107.5, true);
}

function loadDynamicTeachers() {
    let teachers = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.guru) && window.SDN_DATABASE.guru.length > 0) {
        teachers = window.SDN_DATABASE.guru;
    }
    // 2. Fallback: LocalStorage Cache
    if (!teachers) {
        try {
            const raw = localStorage.getItem('sdn_guru_data');
            if (raw) {
                const parsed = JSON.parse(raw);
                if (Array.isArray(parsed) && parsed.length > 0) {
                    teachers = parsed;
                }
            }
        } catch (e) {
            console.warn('Gagal membaca data guru dinamis:', e);
        }
    }

    if (!teachers) teachers = defaultMainGuruList;

    // Sinkronkan data guru ke dalam Bagan Struktur Organisasi Sekolah secara otomatis
    syncBaganStrukturOrganisasi(teachers);

    const gridEl = document.getElementById('guruGridContainer') || document.querySelector('.teachers-grid');
    const tableBody = document.getElementById('guruRecapTableBody') || (document.title.includes('Dewan Guru') ? document.querySelector('.data-table-wrapper table.data-table tbody') : null);

    if (gridEl) {
        gridEl.innerHTML = '';
        let countWali = 0, countAgama = 0, countMapel = 0, countPns = 0, countP3k = 0, countHonor = 0;

        teachers.forEach(g => {
            const jabLower = (g.jabatan || '').toLowerCase();
            const statusLower = (g.status || '').toLowerCase();

            let roleAttr = '';
            if (jabLower.includes('kepala') || jabLower.includes('kelas') || jabLower.includes('wali')) {
                roleAttr += 'wali ';
                countWali++;
            }
            if (jabLower.includes('agama')) {
                roleAttr += 'agama ';
                countAgama++;
            }
            if (jabLower.includes('penjas') || jabLower.includes('inggris') || jabLower.includes('mapel')) {
                roleAttr += 'mapel ';
                if (jabLower.includes('penjas')) roleAttr += 'penjas ';
                if (jabLower.includes('inggris')) roleAttr += 'inggris ';
                countMapel++;
            }

            let statusAttr = 'honor';
            let badgeClass = 'badge-status honor';
            let badgeLabel = g.status || 'Honor';

            if (statusLower.includes('pns')) {
                statusAttr = 'pns';
                badgeClass = 'badge-status pns';
                badgeLabel = g.gol && g.gol !== '-' ? `PNS ${g.gol.split(',')[1] || g.gol}` : 'PNS';
                countPns++;
            } else if (statusLower.includes('p3k')) {
                statusAttr = 'p3k';
                badgeClass = 'badge-status p3k';
                badgeLabel = 'P3K';
                countP3k++;
            } else {
                countHonor++;
            }

            const fotoSrc = g.foto || 'images/dewan-guru.jpg';

            const card = document.createElement('div');
            card.className = 'teacher-card';
            card.setAttribute('data-role', roleAttr.trim());
            card.setAttribute('data-status', statusAttr);

            card.innerHTML = `
                <img src="${fotoSrc}" alt="${escapeHTML(g.nama)}" class="teacher-avatar" style="cursor: pointer;" onclick="if(window.openLightboxWith) window.openLightboxWith(this.src, this.alt)">
                <span class="${badgeClass}">${escapeHTML(badgeLabel)}</span>
                <h3 class="teacher-name" style="margin-top: 8px;">${escapeHTML(g.nama)}</h3>
                <div class="teacher-role">${escapeHTML(g.jabatan)}</div>
                <div class="teacher-details">
                    <span><strong>NIP:</strong> ${escapeHTML(g.nip || '-')}</span>
                    <span><strong>NUPTK:</strong> ${escapeHTML(g.nuptk || '-')}</span>
                    <span><strong>Pangkat:</strong> ${escapeHTML(g.gol || '-')}</span>
                    <span><strong>TTL:</strong> ${escapeHTML(g.ttl || '-')}</span>
                </div>
            `;
            gridEl.appendChild(card);
        });

        // Update pills filter guru
        const filterBtns = document.querySelectorAll('.filter-teacher-btn');
        filterBtns.forEach(btn => {
            const f = btn.getAttribute('data-filter');
            if (f === 'all') btn.textContent = `Semua GTK (${teachers.length})`;
            else if (f === 'wali') btn.textContent = `Wali Kelas (${countWali})`;
            else if (f === 'agama') btn.textContent = `Guru Agama (${countAgama})`;
            else if (f === 'mapel') btn.textContent = `Guru Mapel (${countMapel})`;
            else if (f === 'pns') btn.textContent = `PNS (${countPns})`;
            else if (f === 'p3k') btn.textContent = `P3K (${countP3k})`;
            else if (f === 'honor') btn.textContent = `Honor (${countHonor})`;
        });

        // Re-bind filter & search handler
        if (typeof initTeacherFilter === 'function') {
            initTeacherFilter();
        }
    }

    if (tableBody) {
        tableBody.innerHTML = '';
        teachers.forEach((g, index) => {
            const tr = document.createElement('tr');
            let statusBadge = g.status === 'PNS' ? 'badge-status pns' : (g.status === 'P3K' ? 'badge-status p3k' : 'badge-status honor');
            tr.innerHTML = `
                <td style="text-align: center; font-weight: bold;">${index + 1}</td>
                <td><strong>${escapeHTML(g.nama)}</strong><br><small style="color: var(--dark-muted);">${escapeHTML(g.nip || '-')}</small></td>
                <td>${escapeHTML(g.jabatan)}</td>
                <td><span class="${statusBadge}">${escapeHTML(g.status || 'Honor')}</span></td>
                <td>${escapeHTML(g.gol || '-')}</td>
                <td>${escapeHTML(g.ttl || '-')}</td>
                <td>${escapeHTML(g.nuptk || '-')}</td>
            `;
            tableBody.appendChild(tr);
        });
    }
}


/* -------------------------------------------------------------------
   12. SINKRONISASI DATA SISWA PER KELAS (DARI ADMIN LOCALSTORAGE)
   ------------------------------------------------------------------- */
const defaultMainSiswaData = {
    k1_l: 11, k1_p: 15,
    k2_l: 14, k2_p: 11,
    k3_l: 14, k3_p: 13,
    k4_l: 12, k4_p: 11,
    k5_l: 13, k5_p: 14,
    k6_l: 13, k6_p: 16
};

function loadDynamicStudentData() {
    let s = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && window.SDN_DATABASE.siswa && typeof window.SDN_DATABASE.siswa === 'object') {
        s = Object.assign({}, defaultMainSiswaData, window.SDN_DATABASE.siswa);
    }
    // 2. Fallback: LocalStorage Cache
    if (!s) {
        try {
            const raw = localStorage.getItem('sdn_siswa_counts') || localStorage.getItem('sdn_siswa_kelas');
            if (raw) {
                const parsed = JSON.parse(raw);
                if (parsed && typeof parsed === 'object') {
                    s = Object.assign({}, defaultMainSiswaData, parsed);
                }
            }
        } catch (e) {
            console.warn('Gagal membaca data siswa dinamis:', e);
        }
    }

    if (!s) s = defaultMainSiswaData;

    const k1 = (s.k1_l || 0) + (s.k1_p || 0);
    const k2 = (s.k2_l || 0) + (s.k2_p || 0);
    const k3 = (s.k3_l || 0) + (s.k3_p || 0);
    const k4 = (s.k4_l || 0) + (s.k4_p || 0);
    const k5 = (s.k5_l || 0) + (s.k5_p || 0);
    const k6 = (s.k6_l || 0) + (s.k6_p || 0);

    const totalL = (s.k1_l || 0) + (s.k2_l || 0) + (s.k3_l || 0) + (s.k4_l || 0) + (s.k5_l || 0) + (s.k6_l || 0);
    const totalP = (s.k1_p || 0) + (s.k2_p || 0) + (s.k3_p || 0) + (s.k4_p || 0) + (s.k5_p || 0) + (s.k6_p || 0);
    const totalAll = totalL + totalP;

    // 1. UPDATE DI HALAMAN KESISWAAN (siswa.html)
    const elTotal = document.getElementById('countTotalSiswa');
    const elL = document.getElementById('countSiswaL');
    const elP = document.getElementById('countSiswaP');
    const elPropL = document.getElementById('propSiswaL');
    const elPropP = document.getElementById('propSiswaP');

    if (elTotal) elTotal.textContent = totalAll;
    if (elL) elL.textContent = totalL;
    if (elP) elP.textContent = totalP;
    if (elPropL) elPropL.textContent = `Proporsi ${totalAll ? ((totalL / totalAll) * 100).toFixed(1) : 0}%`;
    if (elPropP) elPropP.textContent = `Proporsi ${totalAll ? ((totalP / totalAll) * 100).toFixed(1) : 0}%`;

    // Update Baris Tabel di siswa.html
    const tableBody = document.getElementById('siswaPublicTableBody');
    if (tableBody) {
        // Ambil data dewan guru terbaru dari database / localStorage untuk sinkronisasi nama/gelar real-time
        let gurus = [];
        try {
            const rawGuru = localStorage.getItem('sdn_guru_data');
            if (rawGuru) gurus = JSON.parse(rawGuru);
        } catch (e) {}
        if (!gurus.length && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.guru)) {
            gurus = window.SDN_DATABASE.guru;
        }

        function resolveWaliName(storedName, defaultFallback, classNum) {
            if (storedName) {
                const found = gurus.find(g => g.nama === storedName);
                if (found) return found.nama;
                return storedName;
            }
            const romans = ['i', 'ii', 'iii', 'iv', 'v', 'vi'];
            const r = romans[classNum - 1];
            const foundByJabatan = gurus.find(g => g.jabatan && (g.jabatan.toLowerCase().includes(`kelas ${r}`) || g.jabatan.toLowerCase().includes(`kelas ${classNum}`)));
            if (foundByJabatan) return foundByJabatan.nama;
            return defaultFallback;
        }

        const rowsData = [
            { no: 1, kelas: "Kelas I (Satu)", wali: resolveWaliName(s.k1_wali, "Yuli Syetia Sari, S.Pd", 1), l: s.k1_l || 0, p: s.k1_p || 0, tot: k1 },
            { no: 2, kelas: "Kelas II (Dua)", wali: resolveWaliName(s.k2_wali, "Elias Tabuni, S.Pd", 2), l: s.k2_l || 0, p: s.k2_p || 0, tot: k2 },
            { no: 3, kelas: "Kelas III (Tiga)", wali: resolveWaliName(s.k3_wali, "Rita Paulina Wabiser, S.Pd", 3), l: s.k3_l || 0, p: s.k3_p || 0, tot: k3 },
            { no: 4, kelas: "Kelas IV (Empat)", wali: resolveWaliName(s.k4_wali, "Warno, S.Pd.SD", 4), l: s.k4_l || 0, p: s.k4_p || 0, tot: k4 },
            { no: 5, kelas: "Kelas V (Lima)", wali: resolveWaliName(s.k5_wali, "Rini Handayani, S.Pd", 5), l: s.k5_l || 0, p: s.k5_p || 0, tot: k5 },
            { no: 6, kelas: "Kelas VI (Enam)", wali: resolveWaliName(s.k6_wali, "Cicik Mursidah, S.Pd", 6), l: s.k6_l || 0, p: s.k6_p || 0, tot: k6 }
        ];

        tableBody.innerHTML = '';
        rowsData.forEach(r => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td style="text-align: center; font-weight: bold;">${r.no}</td>
                <td><strong>${r.kelas}</strong></td>
                <td>${r.wali}</td>
                <td style="text-align: center; font-weight: 700; color: #1d4ed8;">${r.l}</td>
                <td style="text-align: center; font-weight: 700; color: #be185d;">${r.p}</td>
                <td style="text-align: center; font-weight: 800; font-size: 15px;">${r.tot}</td>
                <td>1 Rombel</td>
            `;
            tableBody.appendChild(tr);
        });
    }

    const tfootL = document.getElementById('publicTotalL');
    const tfootP = document.getElementById('publicTotalP');
    const tfootAll = document.getElementById('publicTotalAll');
    if (tfootL) tfootL.textContent = totalL;
    if (tfootP) tfootP.textContent = totalP;
    if (tfootAll) tfootAll.textContent = totalAll;

    // Update Visualisasi Grafik Bar di siswa.html
    const grafikContainer = document.getElementById('siswaGrafikContainer');
    if (grafikContainer) {
        const classesData = [
            { name: "Kelas I", tot: k1, l: s.k1_l || 0, p: s.k1_p || 0 },
            { name: "Kelas II", tot: k2, l: s.k2_l || 0, p: s.k2_p || 0 },
            { name: "Kelas III", tot: k3, l: s.k3_l || 0, p: s.k3_p || 0 },
            { name: "Kelas IV", tot: k4, l: s.k4_l || 0, p: s.k4_p || 0 },
            { name: "Kelas V", tot: k5, l: s.k5_l || 0, p: s.k5_p || 0 },
            { name: "Kelas VI", tot: k6, l: s.k6_l || 0, p: s.k6_p || 0 }
        ];

        grafikContainer.innerHTML = classesData.map(c => {
            const pL = c.tot ? ((c.l / c.tot) * 100).toFixed(1) : 50;
            const pP = c.tot ? ((c.p / c.tot) * 100).toFixed(1) : 50;
            return `
                <div>
                    <div style="display: flex; justify-content: space-between; font-size: 13.5px; font-weight: 700; margin-bottom: 6px;">
                        <span>${c.name} (Total: ${c.tot} Siswa)</span>
                        <span>Laki-laki: ${c.l} | Perempuan: ${c.p}</span>
                    </div>
                    <div style="height: 24px; background: #e2e8f0; border-radius: 6px; overflow: hidden; display: flex;">
                        <div style="width: ${pL}%; background: #2563eb; color: white; font-size: 11px; display: flex; align-items: center; justify-content: center; font-weight: bold;">${c.l} L</div>
                        <div style="width: ${pP}%; background: #db2777; color: white; font-size: 11px; display: flex; align-items: center; justify-content: center; font-weight: bold;">${c.p} P</div>
                    </div>
                </div>
            `;
        }).join('');
    }
}


/* -------------------------------------------------------------------
   13. SINKRONISASI DATA SARPRAS DINAMIS (DARI ADMIN LOCALSTORAGE)
   ------------------------------------------------------------------- */
const defaultMainSarprasList = [
    { id: 1, nama: "Kantor Sekolah", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Digunakan bersama oleh Kepala Sekolah dan Dewan Guru" },
    { id: 2, nama: "Ruang Guru", kondisi: "tidak-ada", kepemilikan: "-", keterangan: "Perlu Usulan Pembangunan Baru (guru saat ini masih berkumpul di ruang kantor)" },
    { id: 3, nama: "Ruang Kelas I", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Ditempati 26 siswa kelas 1" },
    { id: 4, nama: "Ruang Kelas II", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Ditempati 25 siswa kelas 2" },
    { id: 5, nama: "Ruang Kelas III", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Ditempati 27 siswa kelas 3" },
    { id: 6, nama: "Ruang Kelas IV", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Ditempati 23 siswa kelas 4" },
    { id: 7, nama: "Ruang Kelas V", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Ditempati 27 siswa kelas 5" },
    { id: 8, nama: "Ruang Kelas VI", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Ditempati 29 siswa kelas 6" },
    { id: 9, nama: "Ruang TIK (Teknologi Informasi & Komunikasi)", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Pusat perangkat Starlink & Komputer" },
    { id: 10, nama: "Ruang Agama Kristen", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Bimbingan rohani Protestan" },
    { id: 11, nama: "Ruang Agama Katolik", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Bimbingan rohani Katolik" },
    { id: 12, nama: "Ruang Perpustakaan", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Perlu pengadaan rak buku dan perbaikan atap" },
    { id: 13, nama: "Rumah Penjaga Sekolah", kondisi: "rusak-berat", kepemilikan: "Pemerintah", keterangan: "Perlu Rehabilitasi Menyeluruh" },
    { id: 14, nama: "Rumah Kepala Sekolah", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Rumah dinas di area sekolah" },
    { id: 15, nama: "Meja Guru di Kantor", kondisi: "baik", kepemilikan: "Pemerintah", keterangan: "Layak pakai untuk administrasi" },
    { id: 16, nama: "Meja Guru di Kelas", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Perlu servis engsel / kayu" },
    { id: 17, nama: "Kursi Guru", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Perlu penambahan dan perbaikan" },
    { id: 18, nama: "Meja Siswa", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Sebagian perlu direparasi" },
    { id: 19, nama: "Bangku Siswa", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Perlu perawatan berkala" },
    { id: 20, nama: "Lemari di Kelas", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Tempat penyimpanan buku pegangan" },
    { id: 21, nama: "Proyektor Infocus", kondisi: "baik", kepemilikan: "Pemerintah", keterangan: "Fungsi normal untuk presentasi" },
    { id: 22, nama: "Komputer", kondisi: "baik", kepemilikan: "Pemerintah", keterangan: "Operasional ANBK & Guru" },
    { id: 23, nama: "Laptop Guru", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Sebagian baik, sebagian lambat/perlu servis" },
    { id: 24, nama: "Layar Proyektor", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Ada unit baik dan unit perlu ganti kain" },
    { id: 25, nama: "Printer", kondisi: "baik", kepemilikan: "Pemerintah", keterangan: "Cetak soal dan laporan sekolah" },
    { id: 26, nama: "Kulkas", kondisi: "baik", kepemilikan: "Pemerintah", keterangan: "Fasilitas ruang kantor" },
    { id: 27, nama: "Warles (Wireless Mic / Audio)", kondisi: "baik", kepemilikan: "Pemerintah", keterangan: "Dipakai kegiatan upacara & senam" },
    { id: 28, nama: "Ampli Power", kondisi: "baik", kepemilikan: "Pemerintah", keterangan: "Penguat suara pengeras sekolah" },
    { id: 29, nama: "Dispenser Air", kondisi: "baik", kepemilikan: "Pemerintah", keterangan: "Penyedia air minum dewan guru" },
    { id: 30, nama: "Spiker Aktif", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Sebagian unit perlu perbaikan kabel/suara" },
    { id: 31, nama: "Sofa Tamu Kantor", kondisi: "rusak-sedang", kepemilikan: "Pemerintah", keterangan: "Tempat duduk tamu & komite" }
];

function loadDynamicSapras() {
    let items = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.sarpras) && window.SDN_DATABASE.sarpras.length > 0) {
        items = window.SDN_DATABASE.sarpras;
    }
    // 2. Fallback: LocalStorage Cache
    if (!items) {
        try {
            const raw = localStorage.getItem('sdn_sarpras_data');
            if (raw) {
                const parsed = JSON.parse(raw);
                if (Array.isArray(parsed) && parsed.length > 0) {
                    items = parsed;
                }
            }
        } catch (e) {
            console.warn('Gagal membaca data sarpras dinamis:', e);
        }
    }

    if (!items) items = defaultMainSarprasList;

    const tableBody = document.getElementById('saprasPublicTableBody') || (document.title.includes('Sarana') ? document.querySelector('.data-table-wrapper table.data-table tbody') : null);
    if (!tableBody) return;

    let countBaik = 0, countSedang = 0, countBerat = 0, countTidakAda = 0;
    tableBody.innerHTML = '';

    items.forEach((item, index) => {
        if (item.kondisi === 'baik') countBaik++;
        else if (item.kondisi === 'rusak-sedang') countSedang++;
        else if (item.kondisi === 'rusak-berat') countBerat++;
        else if (item.kondisi === 'tidak-ada') countTidakAda++;

        let badgeHtml = '';
        if (item.kondisi === 'baik') {
            badgeHtml = '<span class="cond-badge cond-baik">✅ Baik</span>';
        } else if (item.kondisi === 'rusak-sedang') {
            badgeHtml = '<span class="cond-badge cond-rusak-sedang">⚠️ Rusak Sedang</span>';
        } else if (item.kondisi === 'rusak-berat') {
            badgeHtml = '<span class="cond-badge cond-rusak-berat">⛔ Rusak Berat</span>';
        } else {
            badgeHtml = '<span class="cond-badge cond-tidak-ada">❌ Tidak Ada</span>';
        }

        const tr = document.createElement('tr');
        tr.className = 'sapras-row';
        tr.setAttribute('data-condition', item.kondisi);
        tr.innerHTML = `
            <td style="text-align: center;">${index + 1}</td>
            <td><strong>${escapeHTML(item.nama)}</strong></td>
            <td>${badgeHtml}</td>
            <td>${escapeHTML(item.kepemilikan || 'Pemerintah')}</td>
            <td>${escapeHTML(item.keterangan || '-')}</td>
        `;
        tableBody.appendChild(tr);
    });

    // Update kartu rekap kondisi di sapras.html
    const elBaik = document.getElementById('countSaprasBaik');
    const elSedang = document.getElementById('countSaprasSedang');
    const elBerat = document.getElementById('countSaprasBerat');
    const elTidakAda = document.getElementById('countSaprasTidakAda');

    if (elBaik) elBaik.textContent = `${countBaik} Item`;
    if (elSedang) elSedang.textContent = `${countSedang} Item`;
    if (elBerat) elBerat.textContent = `${countBerat} Item`;
    if (elTidakAda) elTidakAda.textContent = `${countTidakAda} Ruang`;

    // Update pill filter sarpras
    const filterBtns = document.querySelectorAll('.filter-sapras-btn');
    filterBtns.forEach(btn => {
        const f = btn.getAttribute('data-filter');
        if (f === 'all') btn.textContent = `Semua (${items.length})`;
    });

    // Re-bind filter sarpras
    if (typeof initSaprasFilter === 'function') {
        initSaprasFilter();
    }
}


/* ==========================================================================
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
            uraianList = item.uraian_kerja.split('\n').map(s => s.trim().replace(/^[-*•\d.]+\s*/, '')).filter(s => s.length > 0);
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

/* ==========================================================================
   DYNAMIC PENGEMBANGAN GURU (K3S & KKG) LOADER (DENGAN PERBESAR FOTO / LIGHTBOX)
   ========================================================================== */

/* -------------------------------------------------------------------
   PENGEMBANGAN GURU (KKKS & KKG) DENGAN PAGINASI & FILTER REALTIME
   ------------------------------------------------------------------- */
window._allPublicKKG = [];
window._publicKKGPage = 1;
window._publicKKGPageSize = 5;

window.filterPublicKKG = function(targetPage) {
    if (typeof targetPage === 'number') window._publicKKGPage = targetPage;
    const tableBody = document.getElementById('kkgJadwalTableBody');
    const paginationBox = document.getElementById('publicKKGPagination');
    if (!tableBody) return;

    const searchInput = document.getElementById('publicKKGSearchInput');
    const kelompokSelect = document.getElementById('publicKKGFilterKelompok');
    const statusSelect = document.getElementById('publicKKGFilterStatus');

    const query = (searchInput ? searchInput.value : '').trim().toLowerCase();
    const kelompok = kelompokSelect ? kelompokSelect.value : 'ALL';
    const status = statusSelect ? statusSelect.value : 'ALL';

    const filtered = (window._allPublicKKG || []).filter(j => {
        const matchesQuery = !query ||
            (j.agenda || '').toLowerCase().includes(query) ||
            (j.pemateri || '').toLowerCase().includes(query) ||
            (j.tuan_rumah || '').toLowerCase().includes(query) ||
            (j.notulen || '').toLowerCase().includes(query) ||
            (j.tanggal || '').toLowerCase().includes(query);

        let matchesKelompok = true;
        if (kelompok !== 'ALL') {
            matchesKelompok = (j.kelompok || '').toLowerCase().includes(kelompok.toLowerCase());
        }

        let matchesStatus = true;
        if (status !== 'ALL') {
            matchesStatus = (j.status || '').toLowerCase().includes(status.toLowerCase());
        }

        return matchesQuery && matchesKelompok && matchesStatus;
    });

    if (filtered.length === 0) {
        tableBody.innerHTML = `
            <tr>
                <td colspan="7" style="text-align: center; padding: 35px 20px; color: #64748b; background: #f8fafc;">
                    <span style="font-size: 28px; display: block; margin-bottom: 6px;">🔍</span>
                    <strong>Tidak ada jadwal pertemuan yang sesuai dengan pencarian.</strong><br>
                    <small>Silakan ubah filter kelompok atau kosongkan kata kunci pencarian.</small>
                </td>
            </tr>
        `;
        if (paginationBox) paginationBox.style.display = 'none';
        return;
    }

    const totalPages = Math.ceil(filtered.length / window._publicKKGPageSize);
    if (window._publicKKGPage > totalPages) window._publicKKGPage = totalPages;
    if (window._publicKKGPage < 1) window._publicKKGPage = 1;

    const startIdx = (window._publicKKGPage - 1) * window._publicKKGPageSize;
    const pagedItems = filtered.slice(startIdx, startIdx + window._publicKKGPageSize);

    tableBody.innerHTML = '';
    pagedItems.forEach((j, index) => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid #e2e8f0';
        if (index % 2 === 1) tr.style.backgroundColor = '#f8fafc';

        let kelBadgeStyle = 'background: #e0f2fe; color: #0369a1;';
        if (j.kelompok && (j.kelompok.includes('Kelompok A') || j.kelompok.includes('Fase A') || j.kelompok.includes('Agama') || j.kelompok.includes('Awal'))) {
            kelBadgeStyle = 'background: #d1fae5; color: #065f46;';
        } else if (j.kelompok && (j.kelompok.includes('Kelompok B') || j.kelompok.includes('PJOK') || j.kelompok.includes('Inggris') || j.kelompok.includes('Tinggi'))) {
            kelBadgeStyle = 'background: #e0f2fe; color: #0369a1;';
        } else if (j.kelompok && j.kelompok.includes('K3S')) {
            kelBadgeStyle = 'background: #fef3c7; color: #92400e;';
        }

        let statusBadge = '<span style="background: #dcfce7; color: #166534; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Terlaksana</span>';
        if (j.status && (j.status.toLowerCase().includes('akan') || j.status.toLowerCase().includes('dijadwalkan') || j.status.toLowerCase().includes('mendatang'))) {
            statusBadge = '<span style="background: #dbeafe; color: #1e40af; font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">Dijadwalkan</span>';
        }

        let fotoCell = '<span style="color: #94a3b8; font-size: 11px;">-</span>';
        if (j.foto) {
            fotoCell = `
                <div style="display: flex; flex-direction: column; align-items: center; gap: 4px;">
                    <img src="${j.foto}" alt="${escapeHTML(j.agenda)}" style="width: 52px; height: 38px; object-fit: cover; border-radius: 6px; cursor: pointer; box-shadow: 0 1px 4px rgba(0,0,0,0.15);" onclick="if(window.openLightboxWith) window.openLightboxWith('${j.foto}', '${escapeHTML(j.agenda)} - ${escapeHTML(j.tuan_rumah || '')}')" title="Klik untuk perbesar">
                    <button type="button" onclick="if(window.openLightboxWith) window.openLightboxWith('${j.foto}', '${escapeHTML(j.agenda)} - ${escapeHTML(j.tuan_rumah || '')}')" style="background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 4px; cursor: pointer;">
                        🔍 Perbesar
                    </button>
                </div>
            `;
        }

        let pemateriText = '';
        if (j.pemateri) {
            pemateriText = `<div style="font-size: 12px; color: #0284c7; margin-top: 4px; font-weight: 600;">🎙️ <strong>Pemateri:</strong> ${escapeHTML(j.pemateri)}</div>`;
        }

        let notulenText = '';
        if (j.notulen) {
            notulenText = `<div style="font-size: 11.5px; color: #64748b; margin-top: 4px; font-style: italic;">📝 <strong>Notulen:</strong> ${escapeHTML(j.notulen)}</div>`;
        }

        let tuanRumahCell = escapeHTML(j.tuan_rumah || '-');
        if ((j.tuan_rumah || '').includes('Arso VIII')) {
            tuanRumahCell = `<span style="color: #0284c7; font-weight: 800;">🏫 ${escapeHTML(j.tuan_rumah)}</span><br><span style="background: #0284c7; color: white; font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 4px; display: inline-block; margin-top: 3px;">Tuan Rumah Gusek 1</span>`;
        }

        tr.innerHTML = `
            <td style="padding: 12px 14px; font-weight: 700; text-align: center;">${startIdx + index + 1}</td>
            <td style="padding: 12px 14px; font-weight: 600;">${escapeHTML(j.tanggal || j.bulan || '-')}</td>
            <td style="padding: 12px 14px; font-weight: 700;">${tuanRumahCell}</td>
            <td style="padding: 12px 14px;"><span class="badge-tag" style="${kelBadgeStyle} font-size: 11px;">${escapeHTML(j.kelompok || '-')}</span></td>
            <td style="padding: 12px 14px;">
                <div style="font-weight: 700; color: #0f172a;">${escapeHTML(j.agenda || '-')}</div>
                ${pemateriText}
                ${notulenText}
            </td>
            <td style="padding: 12px 14px; text-align: center;">${fotoCell}</td>
            <td style="padding: 12px 14px; text-align: center;">${statusBadge}</td>
        `;
        tableBody.appendChild(tr);
    });

    // Render Paginasi KKG
    if (paginationBox) {
        paginationBox.style.display = 'flex';
        let buttonsHtml = '';

        buttonsHtml += `<button type="button" class="pagination-btn" ${window._publicKKGPage <= 1 ? 'disabled' : ''} onclick="window.filterPublicKKG(${window._publicKKGPage - 1})">◀ Sebelumnya</button>`;

        for (let p = 1; p <= totalPages; p++) {
            buttonsHtml += `<button type="button" class="pagination-btn ${p === window._publicKKGPage ? 'active' : ''}" onclick="window.filterPublicKKG(${p})">${p}</button>`;
        }

        buttonsHtml += `<button type="button" class="pagination-btn" ${window._publicKKGPage >= totalPages ? 'disabled' : ''} onclick="window.filterPublicKKG(${window._publicKKGPage + 1})">Selanjutnya ▶</button>`;

        paginationBox.innerHTML = `
            <div>Menampilkan <strong>${startIdx + 1} - ${Math.min(startIdx + window._publicKKGPageSize, filtered.length)}</strong> dari <strong>${filtered.length}</strong> agenda pertemuan ${query || kelompok !== 'ALL' || status !== 'ALL' ? '(disaring)' : '(Arsip Tersimpan)'}</div>
            <div class="pagination-controls">${buttonsHtml}</div>
        `;
    }
};

function loadDynamicKKG() {
    let kkgData = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && window.SDN_DATABASE.kkg && typeof window.SDN_DATABASE.kkg === 'object') {
        kkgData = window.SDN_DATABASE.kkg;
    }
    // 2. Fallback: LocalStorage Cache
    if (!kkgData) {
        try {
            const raw = localStorage.getItem('sdn_kkg_data');
            if (raw) kkgData = JSON.parse(raw);
        } catch (e) {}
    }

    if (!kkgData) return;

    // 1. Update Identitas Gugus & Program K3S jika di halaman pengembangan-guru.html
    const elSekretariat = document.getElementById('pgGusekSekretariat');
    if (elSekretariat && kkgData.gusek_info && kkgData.gusek_info.alamat_sekretariat) {
        elSekretariat.textContent = kkgData.gusek_info.alamat_sekretariat;
    }
    const elKetua = document.getElementById('pgGusekKetua');
    if (elKetua && kkgData.gusek_info && kkgData.gusek_info.ketua) {
        const nipStr = kkgData.gusek_info.nip_ketua ? ` (NIP ${kkgData.gusek_info.nip_ketua})` : '';
        elKetua.textContent = `${kkgData.gusek_info.ketua}${nipStr}`;
    }
    const elWaktu = document.getElementById('pgGusekWaktu');
    if (elWaktu && kkgData.gusek_info) {
        elWaktu.textContent = kkgData.gusek_info.hari_rutin || (kkgData.k3s && kkgData.k3s.jadwal) || 'Hari Rabu Bergilir';
    }
    const elDasarSK = document.getElementById('pgGusekDasarSK');
    if (elDasarSK && kkgData.gusek_info) {
        elDasarSK.textContent = kkgData.gusek_info.dasar_hukum || kkgData.gusek_info.tanggal_penetapan || 'SK Resmi Gusek 1 Arso Barat';
    }
    const elDeskripsi = document.getElementById('pgGusekDeskripsi');
    if (elDeskripsi && kkgData.gusek_info && kkgData.gusek_info.deskripsi) {
        elDeskripsi.textContent = kkgData.gusek_info.deskripsi;
    }

    // Update Program Kerja K3S
    const elK3SList = document.getElementById('pgK3SProgramsList');
    if (elK3SList && kkgData.k3s && Array.isArray(kkgData.k3s.uraian_kerja) && kkgData.k3s.uraian_kerja.length > 0) {
        elK3SList.innerHTML = kkgData.k3s.uraian_kerja.map(p => `<li>${escapeHTML(p)}</li>`).join('');
    }
    const elK3SKetuaBox = document.getElementById('pgK3SKetuaBox');
    if (elK3SKetuaBox && kkgData.gusek_info && kkgData.gusek_info.ketua) {
        const nipStr = kkgData.gusek_info.nip_ketua ? ` (NIP ${kkgData.gusek_info.nip_ketua})` : '';
        elK3SKetuaBox.innerHTML = `👤 Ketua Pengelola KKKS Gusek 1: <strong style="color: #0f172a;">${escapeHTML(kkgData.gusek_info.ketua)}${escapeHTML(nipStr)}</strong> bersama Forum Kepala Sekolah se-Gusek 1 Arso Barat (termasuk SDN Inpres Arso VIII)`;
    }

    // Update KKG Kelompok A
    const elKelAJudul = document.getElementById('pgKelompokAJudul');
    if (elKelAJudul && kkgData.kkg_kelompok_a && kkgData.kkg_kelompok_a.nama_kelompok) {
        elKelAJudul.textContent = kkgData.kkg_kelompok_a.nama_kelompok;
    }
    const elKelACakupan = document.getElementById('pgKelompokACakupan');
    if (elKelACakupan && kkgData.kkg_kelompok_a && kkgData.kkg_kelompok_a.cakupan) {
        elKelACakupan.textContent = kkgData.kkg_kelompok_a.cakupan;
    }
    const elKelAJadwal = document.getElementById('pgKelompokAJadwal');
    if (elKelAJadwal && kkgData.kkg_kelompok_a && kkgData.kkg_kelompok_a.jadwal) {
        elKelAJadwal.textContent = kkgData.kkg_kelompok_a.jadwal;
    }
    const elKelAList = document.getElementById('pgKelompokAProgramsList');
    if (elKelAList && kkgData.kkg_kelompok_a && Array.isArray(kkgData.kkg_kelompok_a.uraian_kerja) && kkgData.kkg_kelompok_a.uraian_kerja.length > 0) {
        elKelAList.innerHTML = kkgData.kkg_kelompok_a.uraian_kerja.map(p => `<li>${escapeHTML(p)}</li>`).join('');
    }

    // Update KKG Kelompok B
    const elKelBJudul = document.getElementById('pgKelompokBJudul');
    if (elKelBJudul && kkgData.kkg_kelompok_b && kkgData.kkg_kelompok_b.nama_kelompok) {
        elKelBJudul.textContent = kkgData.kkg_kelompok_b.nama_kelompok;
    }
    const elKelBCakupan = document.getElementById('pgKelompokBCakupan');
    if (elKelBCakupan && kkgData.kkg_kelompok_b && kkgData.kkg_kelompok_b.cakupan) {
        elKelBCakupan.textContent = kkgData.kkg_kelompok_b.cakupan;
    }
    const elKelBJadwal = document.getElementById('pgKelompokBJadwal');
    if (elKelBJadwal && kkgData.kkg_kelompok_b && kkgData.kkg_kelompok_b.jadwal) {
        elKelBJadwal.textContent = kkgData.kkg_kelompok_b.jadwal;
    }
    const elKelBList = document.getElementById('pgKelompokBProgramsList');
    if (elKelBList && kkgData.kkg_kelompok_b && Array.isArray(kkgData.kkg_kelompok_b.uraian_kerja) && kkgData.kkg_kelompok_b.uraian_kerja.length > 0) {
        elKelBList.innerHTML = kkgData.kkg_kelompok_b.uraian_kerja.map(p => `<li>${escapeHTML(p)}</li>`).join('');
    }

    // 2. Jadwal Pertemuan Tabel & Dokumentasi
    const jadwalList = Array.isArray(kkgData.jadwal_pertemuan) ? kkgData.jadwal_pertemuan : (Array.isArray(kkgData) ? kkgData : []);
    window._allPublicKKG = jadwalList;

    if (typeof window.filterPublicKKG === 'function') {
        window.filterPublicKKG(1);
    }

    // Render galeri dokumentasi KKG sebagai Showcase Slider Carousel Otomatis (Maksimal 6 kegiatan terbaru & 6 titik agar rapi)
    const sliderWrapper = document.getElementById('kkgShowcaseSliderWrapper');
    const track = document.getElementById('kkgShowcaseSliderTrack');
    const dotsBar = document.getElementById('kkgShowcaseDotsBar');
    if (sliderWrapper && track && dotsBar) {
        const itemsWithPhoto = jadwalList.filter(item => item.foto && item.foto.length > 0).slice(0, 6);
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
    }
}

function loadDynamicSOP() {
    let sopData = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && window.SDN_DATABASE.sop_data && typeof window.SDN_DATABASE.sop_data === 'object') {
        sopData = window.SDN_DATABASE.sop_data;
    }
    // 2. Fallback: LocalStorage Cache
    if (!sopData) {
        try {
            const raw = localStorage.getItem('sdn_sop_data');
            if (raw) sopData = JSON.parse(raw);
        } catch (e) {}
    }

    if (!sopData) return;

    // Helper untuk format teks poin (jika mengandung ' – ' tebalkan bagian depan)
    function formatRuleItem(text) {
        if (!text) return '';
        const parts = text.split(' – ');
        if (parts.length > 1) {
            return `<strong>${escapeHTML(parts[0])}</strong> – ${escapeHTML(parts.slice(1).join(' – '))}`;
        }
        return escapeHTML(text);
    }

    // 1. Tata Tertib Guru (di sop.html dan guru.html)
    if (Array.isArray(sopData.tata_tertib_guru) && sopData.tata_tertib_guru.length > 0) {
        const elSopGuru = document.getElementById('sopTataTertibGuruList');
        if (elSopGuru) {
            elSopGuru.innerHTML = sopData.tata_tertib_guru.map(item => `<li>${formatRuleItem(item)}</li>`).join('');
        }
        const elGuruTatib = document.getElementById('guruTataTertibList');
        if (elGuruTatib) {
            elGuruTatib.innerHTML = sopData.tata_tertib_guru.map(item => `<li>${formatRuleItem(item)}</li>`).join('');
        }
    }

    // 2. Tata Tertib Siswa (di sop.html)
    if (Array.isArray(sopData.tata_tertib_siswa) && sopData.tata_tertib_siswa.length > 0) {
        const elSopSiswa = document.getElementById('sopTataTertibSiswaList');
        if (elSopSiswa) {
            elSopSiswa.innerHTML = sopData.tata_tertib_siswa.map(item => `<li>${formatRuleItem(item)}</li>`).join('');
        }
    }

    // 3. Jadwal Piket Guru Harian (Senin - Jumat)
    if (sopData.piket_guru && typeof sopData.piket_guru === 'object') {
        const hariList = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat'];

        // Render di sop.html (#sopJadwalPiketGuruGrid)
        const elSopPiket = document.getElementById('sopJadwalPiketGuruGrid');
        if (elSopPiket) {
            elSopPiket.innerHTML = hariList.map(h => {
                const teachers = Array.isArray(sopData.piket_guru[h]) ? sopData.piket_guru[h] : [];
                const teacherItems = teachers.map(t => `<li><strong>${escapeHTML(t)}</strong></li>`).join('');
                return `
                    <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 14px 18px;">
                        <div style="font-weight: 800; color: var(--primary); font-size: 14px; margin-bottom: 6px;">${h.toUpperCase()}</div>
                        <ul style="margin: 0; padding-left: 18px; font-size: 13.5px; color: #1e293b;">
                            ${teacherItems || '<li><em>Belum diatur</em></li>'}
                        </ul>
                    </div>
                `;
            }).join('');
        }

        // Render di guru.html (#guruJadwalPiketGrid)
        const elGuruPiket = document.getElementById('guruJadwalPiketGrid');
        if (elGuruPiket) {
            elGuruPiket.innerHTML = hariList.map(h => {
                const teachers = Array.isArray(sopData.piket_guru[h]) ? sopData.piket_guru[h] : [];
                const teacherItems = teachers.map((t, idx) => `<div style="font-size: 13.5px; font-weight: 600; color: #0f172a;">${idx + 1}. ${escapeHTML(t)}</div>`).join('');
                return `
                    <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: 8px; padding: 14px;">
                        <strong style="color: var(--primary); font-size: 13.5px; display: block; margin-bottom: 6px;">${h.toUpperCase()}</strong>
                        ${teacherItems || '<div style="font-size: 13px; color: #94a3b8;">Belum diatur</div>'}
                    </div>
                `;
            }).join('');
        }
    }

    // 4. Jadwal Pemakaian Seragam Guru (5 Siklus Mingguan)
    if (Array.isArray(sopData.seragam_guru) && sopData.seragam_guru.length > 0) {
        // Render di sop.html (#sopTabelSeragamGuruBody)
        const elSopSeragam = document.getElementById('sopTabelSeragamGuruBody');
        if (elSopSeragam) {
            elSopSeragam.innerHTML = sopData.seragam_guru.map(s => `
                <tr>
                    <td><strong>${escapeHTML(s.siklus || '')}</strong></td>
                    <td><span class="tag-seragam tag-keki">${escapeHTML(s.senin_selasa || '')}</span></td>
                    <td><span class="tag-seragam tag-putih">${escapeHTML(s.rabu || '')}</span></td>
                    <td><span class="tag-seragam tag-hijau">${escapeHTML(s.kamis || '')}</span></td>
                    <td><span class="tag-seragam tag-merah">${escapeHTML(s.jumat || '')}</span></td>
                </tr>
            `).join('');
        }

        // Render di guru.html (#guruSeragamTableBody)
        const elGuruSeragam = document.getElementById('guruSeragamTableBody');
        if (elGuruSeragam) {
            elGuruSeragam.innerHTML = sopData.seragam_guru.map((s, idx) => `
                <tr style="border-bottom: 1px solid #f1f5f9;">
                    <td style="padding: 10px;"><strong>${escapeHTML(s.siklus || 'Minggu ' + (idx + 1))}</strong></td>
                    <td style="padding: 10px;"><span style="background: #fef3c7; color: #92400e; padding: 3px 8px; border-radius: 4px; font-weight: 600;">${escapeHTML(s.senin_selasa || '')}</span></td>
                    <td style="padding: 10px;">${escapeHTML(s.rabu || '')}</td>
                    <td style="padding: 10px; font-weight: 600;">${escapeHTML(s.kamis || '')}</td>
                    <td style="padding: 10px; font-weight: 600;">${escapeHTML(s.jumat || '')}</td>
                </tr>
            `).join('');
        }
    }

    // 5. Pembina Pramuka Siaga & Penggalang
    if (sopData.pramuka_pembina) {
        const elPramukaJadwal = document.getElementById('sopPramukaJadwalText');
        if (elPramukaJadwal && sopData.pramuka_pembina.jadwal) {
            elPramukaJadwal.innerHTML = `<strong>Waktu Pelaksanaan:</strong> ${escapeHTML(sopData.pramuka_pembina.jadwal)}`;
        }

        const siagaTeachers = Array.isArray(sopData.pramuka_pembina.siaga) ? sopData.pramuka_pembina.siaga : [];
        const penggalangTeachers = Array.isArray(sopData.pramuka_pembina.penggalang) ? sopData.pramuka_pembina.penggalang : [];

        // sop.html
        const elSopSiaga = document.getElementById('sopPramukaSiagaList');
        if (elSopSiaga && siagaTeachers.length > 0) {
            elSopSiaga.innerHTML = siagaTeachers.map(t => `<li>${escapeHTML(t)}</li>`).join('');
        }
        const elSopPenggalang = document.getElementById('sopPramukaPenggalangList');
        if (elSopPenggalang && penggalangTeachers.length > 0) {
            elSopPenggalang.innerHTML = penggalangTeachers.map(t => `<li>${escapeHTML(t)}</li>`).join('');
        }

        // guru.html
        const elGuruSiaga = document.getElementById('guruPramukaSiagaList');
        if (elGuruSiaga && siagaTeachers.length > 0) {
            elGuruSiaga.innerHTML = siagaTeachers.map(t => `<li>${escapeHTML(t)}</li>`).join('');
        }
        const elGuruPenggalang = document.getElementById('guruPramukaPenggalangList');
        if (elGuruPenggalang && penggalangTeachers.length > 0) {
            elGuruPenggalang.innerHTML = penggalangTeachers.map(t => `<li>${escapeHTML(t)}</li>`).join('');
        }
    }
}



function loadDynamicAgenda() {
    const container = document.getElementById('dynamicAgendaContainer');
    if (!container) return;

    let items = null;
    // 1. Prioritas Utama: Google Cloud Firebase Realtime
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.agenda) && window.SDN_DATABASE.agenda.length > 0) {
        items = window.SDN_DATABASE.agenda;
    }
    // 2. Fallback: LocalStorage Cache
    if (!items) {
        try {
            const raw = localStorage.getItem('sdn_agenda_data');
            if (raw) {
                const parsed = JSON.parse(raw);
                if (Array.isArray(parsed) && parsed.length > 0) items = parsed;
            }
        } catch (e) {}
    }

    if (!items || items.length === 0) return;

    container.innerHTML = '';
    items.forEach(item => {
        const div = document.createElement('div');
        div.style.cssText = 'display: flex; gap: 14px; align-items: center;';
        div.innerHTML = `
            <div style="background: var(--primary-subtle); color: var(--primary); padding: 8px 14px; border-radius: 8px; text-align: center; min-width: 65px; flex-shrink: 0;">
                <div style="font-size: 18px; font-weight: 800; line-height: 1.1;">${escapeHTML(item.tanggal || '01')}</div>
                <div style="font-size: 11px; font-weight: 700; text-transform: uppercase;">${escapeHTML(item.bulan || 'Bln')}</div>
            </div>
            <div>
                <h4 style="font-size: 14.5px; font-weight: 700; margin-bottom: 2px; color: #0f172a;">${escapeHTML(item.judul || '')}</h4>
                <p style="font-size: 12.5px; color: var(--dark-muted); margin: 0; line-height: 1.4;">${escapeHTML(item.keterangan || '')}</p>
            </div>
        `;
        container.appendChild(div);
    });
}


/* -------------------------------------------------------------------
   SISTEM VERIFIKASI KEAMANAN MANUSIA (ANTI-BOT & ANTI-SPAM)
   ------------------------------------------------------------------- */
window._ppdbExpectedCaptcha = 0;
window._contactExpectedCaptcha = 0;

function initPPDBHumanCaptcha() {
    const qElem = document.getElementById('ppdbCaptchaQuestion');
    const aElem = document.getElementById('ppdbCaptchaAnswer');
    if (!qElem) return;
    const num1 = Math.floor(Math.random() * 8) + 1;
    const num2 = Math.floor(Math.random() * 8) + 1;
    window._ppdbExpectedCaptcha = num1 + num2;
    qElem.textContent = `${num1} + ${num2} = ?`;
    if (aElem) aElem.value = '';
}

function initContactHumanCaptcha() {
    const qElem = document.getElementById('contactCaptchaQuestion');
    const aElem = document.getElementById('contactCaptchaAnswer');
    if (!qElem) return;
    const num1 = Math.floor(Math.random() * 8) + 1;
    const num2 = Math.floor(Math.random() * 8) + 1;
    window._contactExpectedCaptcha = num1 + num2;
    qElem.textContent = `${num1} + ${num2} = ?`;
    if (aElem) aElem.value = '';
}


/* -------------------------------------------------------------------
   5C. AUTO-SLIDING FEATURED SHOWCASE (SLIDER BERITA & KEGIATAN UTAMA)
   ------------------------------------------------------------------- */

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

function initFeaturedShowcaseSlider() {
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

/* -------------------------------------------------------------------
   CEK MANDIRI STATUS KELULUSAN / PENERIMAAN PPDB OLEH ORANG TUA
   ------------------------------------------------------------------- */
window.checkPublicPPDBStatus = function() {
    const input = document.getElementById('inputCheckPPDB');
    const resultBox = document.getElementById('checkPPDBResult');
    if (!input || !resultBox) return;

    const query = input.value.trim().toLowerCase();
    if (!query) {
        alert('Silakan ketik Nomor Registrasi (contoh: PPDB-123456) atau Nama Calon Siswa terlebih dahulu.');
        input.focus();
        return;
    }

    resultBox.style.display = 'block';
    resultBox.innerHTML = '<div style="background: rgba(255,255,255,0.15); padding: 12px; border-radius: 8px; text-align: center; color: white; font-size: 13px;">⏳ Mencari data pendaftaran di server...</div>';

    // Coba ambil data dari localStorage atau Google Cloud Firebase
    function processSearch(list) {
        const matches = list.filter(item => {
            const idMatch = (item.id || '').toLowerCase().includes(query);
            const nameMatch = (item.nama || '').toLowerCase().includes(query);
            return idMatch || nameMatch;
        });

        if (matches.length === 0) {
            resultBox.innerHTML = `
                <div style="background: #ffffff; color: #1e293b; padding: 20px; border-radius: 10px; border-left: 5px solid #f59e0b; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="font-size: 20px;">⚠️</span>
                        <strong style="font-size: 15px; color: #b45309;">Data Tidak Ditemukan</strong>
                    </div>
                    <p style="font-size: 13px; color: #475569; margin: 0 0 10px;">
                        Pencarian untuk <strong>"${query}"</strong> belum ditemukan di sistem. Pastikan ejaan nama atau nomor registrasi sudah benar (contoh: <code>PPDB-123456</code>).
                    </p>
                    <p style="font-size: 12.5px; color: #64748b; margin: 0;">
                        Jika Anda baru mendaftar atau mendaftar manual di sekolah, silakan hubungi Narahubung Panitia via WhatsApp: 
                        <a href="https://wa.me/6281248219125?text=Halo%20Panitia%20PPDB%20SDN%20Inpres%20Arso%20VIII,%20saya%20ingin%20menanyakan%20status%20pendaftaran%20atas%20nama:%20${encodeURIComponent(query)}" target="_blank" style="color: #0284c7; font-weight: bold; text-decoration: underline;">0812-4821-9125 (Pak Adi Puspito)</a>.
                    </p>
                </div>
            `;
            return;
        }

        let outputHtml = '';
        matches.forEach(item => {
            const isAccepted = item.status === 'Diterima';
            const isRejected = item.status === 'Tidak Diterima';
            
            let statusBadge = '';
            let statusDesc = '';
            
            if (isAccepted) {
                statusBadge = '<span style="background: #16a34a; color: white; padding: 4px 12px; border-radius: 999px; font-size: 12px; font-weight: 800;">✓ DITERIMA / LOLOS SELEKSI</span>';
                statusDesc = `
                    <div style="background: #f0fdf4; border: 1px solid #86efac; padding: 12px; border-radius: 8px; margin-top: 12px; font-size: 12.5px; color: #166534;">
                        <strong>🎉 Selamat! Calon peserta didik dinyatakan Diterima di SD Negeri Inpres Arso VIII.</strong><br>
                        Silakan hadir ke kantor sekolah pada jam kerja (08.00 - 12.00 WIT) membawa fotokopi KK (2 lembar), Akta Kelahiran (2 lembar), dan Pas Foto 3x4 (2 lembar) untuk menyelesaikan proses daftar ulang.
                    </div>
                `;
            } else if (isRejected) {
                statusBadge = '<span style="background: #dc2626; color: white; padding: 4px 12px; border-radius: 999px; font-size: 12px; font-weight: 800;">✕ BELUM DAPAT DITERIMA</span>';
                statusDesc = `
                    <div style="background: #fef2f2; border: 1px solid #fca5a5; padding: 12px; border-radius: 8px; margin-top: 12px; font-size: 12.5px; color: #991b1b;">
                        Mohon maaf, kuota daya tampung kelas I tahun ini telah terpenuhi. Terima kasih banyak atas kepercayaan Anda kepada SD Negeri Inpres Arso VIII.
                    </div>
                `;
            } else {
                statusBadge = '<span style="background: #d97706; color: white; padding: 4px 12px; border-radius: 999px; font-size: 12px; font-weight: 800;">⏳ MENUNGGU VERIFIKASI BERKAS</span>';
                statusDesc = `
                    <div style="background: #fefce8; border: 1px solid #fde047; padding: 12px; border-radius: 8px; margin-top: 12px; font-size: 12.5px; color: #854d0e;">
                        Data formulir online telah masuk. Silakan hadir ke sekolah untuk menyerahkan fotokopi KK dan Akta Kelahiran kepada panitia untuk diproses.
                    </div>
                `;
            }

            outputHtml += `
                <div style="background: #ffffff; color: #0f172a; padding: 18px; border-radius: 10px; margin-bottom: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; border-bottom: 1px solid #e2e8f0; padding-bottom: 10px; margin-bottom: 10px;">
                        <div>
                            <div style="font-size: 16px; font-weight: 800; color: #0369a1;">${item.nama}</div>
                            <div style="font-size: 12px; color: #64748b;">No. Registrasi: <strong>${item.id}</strong> • Tanggal: ${item.tgl}</div>
                        </div>
                        <div>${statusBadge}</div>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 8px; font-size: 12.5px; color: #334155;">
                        <div><strong>Jenis Kelamin:</strong> ${item.gender}</div>
                        <div><strong>Tempat, Tgl Lahir:</strong> ${item.ttl}</div>
                        <div><strong>Orang Tua / Wali:</strong> ${item.ortu}</div>
                        <div><strong>Alamat:</strong> ${item.alamat}</div>
                    </div>
                    ${statusDesc}
                </div>
            `;
        });

        resultBox.innerHTML = outputHtml;
    }

    // Ambil dari Google Cloud Firebase terlebih dahulu agar status yang diubah Admin langsung terbaca
    if (typeof fetch === 'function') {
        fetch('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/ppdb_submissions.json?t=' + Date.now())
            .then(res => res.json())
            .then(cloudData => {
                if (Array.isArray(cloudData) && cloudData.length > 0) {
                    processSearch(cloudData);
                } else {
                    const localRaw = localStorage.getItem('sdn_ppdb_submissions');
                    const localData = localRaw ? JSON.parse(localRaw) : [];
                    processSearch(localData);
                }
            })
            .catch(() => {
                const localRaw = localStorage.getItem('sdn_ppdb_submissions');
                const localData = localRaw ? JSON.parse(localRaw) : [];
                processSearch(localData);
            });
    } else {
        const localRaw = localStorage.getItem('sdn_ppdb_submissions');
        const localData = localRaw ? JSON.parse(localRaw) : [];
        processSearch(localData);
    }
};

/* -------------------------------------------------------------------
   12. SINKRONISASI PROFIL, KONTAK & BERANDA SECARA REALTIME
   ------------------------------------------------------------------- */
function loadDynamicProfil() {
    let profilData = null;
    if (window.SDN_DATABASE && window.SDN_DATABASE.profil && typeof window.SDN_DATABASE.profil === 'object') {
        profilData = window.SDN_DATABASE.profil;
    }
    if (!profilData) {
        try {
            const raw = localStorage.getItem('sdn_profil_data');
            if (raw) profilData = JSON.parse(raw);
        } catch (e) {}
    }
    if (!profilData) return;

    // 1. Visi
    const visiEl = document.getElementById('profilVisiQuote');
    if (visiEl && profilData.visi) {
        visiEl.textContent = `"${profilData.visi}"`;
    }

    // 2. Misi
    const misiEl = document.getElementById('profilMisiList');
    if (misiEl && profilData.misi) {
        const items = Array.isArray(profilData.misi) ? profilData.misi : String(profilData.misi).split('\n').filter(m => m.trim());
        if (items.length > 0) {
            misiEl.innerHTML = '';
            items.forEach(m => {
                const li = document.createElement('li');
                li.textContent = m.trim();
                misiEl.appendChild(li);
            });
        }
    }

    // 3. Tujuan
    const tujuanEl = document.getElementById('profilTujuanList');
    if (tujuanEl && profilData.tujuan) {
        const items = Array.isArray(profilData.tujuan) ? profilData.tujuan : String(profilData.tujuan).split('\n').filter(t => t.trim());
        if (items.length > 0) {
            tujuanEl.innerHTML = '';
            items.forEach(t => {
                const li = document.createElement('li');
                li.textContent = t.trim();
                tujuanEl.appendChild(li);
            });
        }
    }

    // 4. Sejarah Singkat
    const sejarahText = document.getElementById('profilSejarahText');
    if (sejarahText && profilData.sejarah) {
        const paras = String(profilData.sejarah).split(/\n\s*\n/).map(p => p.trim()).filter(p => p.length > 0);
        if (paras.length > 0) {
            sejarahText.innerHTML = paras.map(p => `<p style="margin-bottom: 14px;">${escapeHTML(p)}</p>`).join('');
        }
    }

    // 5. Data Legalitas & Identitas Satuan Pendidikan
    if (profilData.identitas && typeof profilData.identitas === 'object') {
        const id = profilData.identitas;
        const npsnEl = document.getElementById('profilNPSN');
        const luasEl = document.getElementById('profilLuasTanah');
        const dayaEl = document.getElementById('profilDayaListrik');
        const alamatEl = document.getElementById('profilAlamat');
        const skOpEl = document.getElementById('profilSKOperasional');

        if (npsnEl && id.npsn) npsnEl.textContent = id.npsn;
        if (luasEl && id.luas_tanah) luasEl.textContent = id.luas_tanah;
        if (dayaEl && id.daya_listrik) dayaEl.textContent = id.daya_listrik;
        if (alamatEl && id.alamat) alamatEl.textContent = id.alamat;
        if (skOpEl && id.sk_izin_operasional) skOpEl.textContent = id.sk_izin_operasional;
    }
}

function loadDynamicKontak() {
    let kontakData = null;
    if (window.SDN_DATABASE && window.SDN_DATABASE.kontak && typeof window.SDN_DATABASE.kontak === 'object') {
        kontakData = window.SDN_DATABASE.kontak;
    }
    if (!kontakData) {
        try {
            const raw = localStorage.getItem('sdn_kontak_data');
            if (raw) kontakData = JSON.parse(raw);
        } catch (e) {}
    }
    if (!kontakData) return;

    const alamat = document.getElementById('kontakAlamatText');
    if (alamat && kontakData.alamat) alamat.textContent = kontakData.alamat;

    const telp = document.getElementById('kontakTeleponText');
    if (telp && kontakData.telepon) telp.textContent = kontakData.telepon;

    const email = document.getElementById('kontakEmailText');
    if (email && kontakData.email) email.textContent = kontakData.email;

    const jam = document.getElementById('kontakJamKerjaText');
    if (jam && kontakData.jam_kerja) jam.textContent = kontakData.jam_kerja;
}

function loadDynamicBeranda() {
    let berandaData = null;
    if (window.SDN_DATABASE && window.SDN_DATABASE.beranda && typeof window.SDN_DATABASE.beranda === 'object') {
        berandaData = window.SDN_DATABASE.beranda;
    }
    if (!berandaData) return;

    const marquee = document.getElementById('heroMarqueeText');
    if (marquee && berandaData.marquee) {
        marquee.textContent = berandaData.marquee;
    }
}
