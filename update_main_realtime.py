# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Cloud Fetch Block at the top of js/main.js
old_fetch_block = """    // Pembaruan data otomatis dari Google Cloud Database (Realtime di semua HP & Laptop)
    if (typeof fetch === 'function') {
        const cloudUrl = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json?t=' + Date.now();
        fetch(cloudUrl, { cache: 'no-store' })
            .then(res => {
                if (res.ok) return res.json();
                throw new Error('Cloud fetch failed');
            })
            .then(db => {
                if (db && typeof db === 'object') {
                    window.SDN_DATABASE = db;
                    // Sinkronkan ke LocalStorage agar offline/refresh seketika konsisten
                    try {
                        if (db.sambutan) localStorage.setItem('sdn_sambutan_data', JSON.stringify(db.sambutan));
                        if (db.galeri) localStorage.setItem('sdn_galeri_data', JSON.stringify(db.galeri));
                        if (db.berita) localStorage.setItem('sdn_berita_data', JSON.stringify(db.berita));
                        if (db.pengumuman) localStorage.setItem('sdn_pengumuman_data', JSON.stringify(db.pengumuman));
                        if (db.guru) localStorage.setItem('sdn_guru_data', JSON.stringify(db.guru));
                        if (db.sarpras) localStorage.setItem('sdn_sarpras_data', JSON.stringify(db.sarpras));
                        if (db.kolaborasi) localStorage.setItem('sdn_kolaborasi_data', JSON.stringify(db.kolaborasi));
                        if (db.kkg) localStorage.setItem('sdn_kkg_data', JSON.stringify(db.kkg));
                        if (db.sop_data) localStorage.setItem('sdn_sop_data', JSON.stringify(db.sop_data));
                        if (db.siswa) {
                            localStorage.setItem('sdn_siswa_counts', JSON.stringify(db.siswa));
                            localStorage.setItem('sdn_siswa_kelas', JSON.stringify(db.siswa));
                        }
                        if (db.ppdb_config) localStorage.setItem('sdn_ppdb_config', JSON.stringify(db.ppdb_config));
                    } catch (e) {}

                    // Segera render ulang dengan data terbaru dari Google Cloud
                    loadDynamicAnnouncements();
                    loadDynamicNews();
                    loadDynamicSambutan();
                    loadDynamicGallery();
                    loadDynamicTeachers();
                    loadDynamicStudentData();
                    loadDynamicSapras();
                    loadDynamicKolaborasi();
                    loadDynamicKKG();
                    loadDynamicSOP();
                    renderPPDBPublicInfo();
                }
            })
            .catch(() => {
                // Fallback ke file data_sekolah.json lokal jika cloud tidak terjangkau
                fetch('data_sekolah.json?t=' + Date.now(), { cache: 'no-store' })
                    .then(res => res.json())
                    .then(db => {
                        if (db && typeof db === 'object') {
                            window.SDN_DATABASE = db;
                            loadDynamicAnnouncements();
                            loadDynamicNews();
                            loadDynamicSambutan();
                            loadDynamicGallery();
                            loadDynamicTeachers();
                            loadDynamicStudentData();
                            loadDynamicSapras();
                            loadDynamicKolaborasi();
                            loadDynamicKKG();
                            loadDynamicSOP();
                            renderPPDBPublicInfo();
                        }
                    }).catch(() => {});
            });
    }

    // Pembaruan seketika antar-tab jika admin mengedit di tab sebelah
    window.addEventListener('storage', function(e) {
        if (!e.key || e.key.startsWith('sdn_')) {
            loadDynamicAnnouncements();
            loadDynamicNews();
            loadDynamicSambutan();
            loadDynamicGallery();
            loadDynamicTeachers();
            loadDynamicStudentData();
            loadDynamicSapras();
            loadDynamicKolaborasi();
            loadDynamicKKG();
            loadDynamicSOP();
            renderPPDBPublicInfo();
        }
    });"""

new_fetch_block = """    // Eksekusi pembaruan realtime dari Google Cloud Database (Realtime di semua HP & Laptop)
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
    });"""

assert old_fetch_block in content, "old_fetch_block not found in js/main.js"
content = content.replace(old_fetch_block, new_fetch_block)

# 2. Add safeSetStorage and refreshDataFromCloud definition before DOMContentLoaded
target_before_dom = "document.addEventListener('DOMContentLoaded', function () {"
new_cloud_helpers = """// HELPER PENYIMPANAN LOCALSTORAGE AMAN (Mencegah QuotaExceededError galeri memblokir berita/pengumuman)
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
                loadDynamicKKG();
                loadDynamicSOP();
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
                        loadDynamicKKG();
                        loadDynamicSOP();
                        renderPPDBPublicInfo();
                    }
                }).catch(() => {});
        });
};

document.addEventListener('DOMContentLoaded', function () {"""

assert target_before_dom in content, "target_before_dom not found in js/main.js"
content = content.replace(target_before_dom, new_cloud_helpers, 1)

# 3. Update loadDynamicGallery
old_gallery = """function loadDynamicGallery() {
    const galleryGrid = document.querySelector('.gallery-grid');
    if (!galleryGrid) return;

    let items = null;
    try {
        const raw = localStorage.getItem('sdn_galeri_data');
        if (raw && !raw.includes('unsplash')) {
            const parsed = JSON.parse(raw);
            if (Array.isArray(parsed)) items = parsed;
        }
    } catch (e) {}

    if (!items && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.galeri)) {
        items = window.SDN_DATABASE.galeri;
    }"""

new_gallery = """function loadDynamicGallery() {
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
    }"""

assert old_gallery in content, "old_gallery not found in js/main.js"
content = content.replace(old_gallery, new_gallery)

# 4. Update loadDynamicAnnouncements
old_announcements = """function loadDynamicAnnouncements() {
    try {
        let items = null;
        try {
            const raw = localStorage.getItem('sdn_pengumuman_data');
            if (raw) {
                const parsed = JSON.parse(raw);
                if (Array.isArray(parsed) && parsed.length > 0) items = parsed;
            }
        } catch (e) {}

        if (!items && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.pengumuman) && window.SDN_DATABASE.pengumuman.length > 0) {
            items = window.SDN_DATABASE.pengumuman;
        }"""

new_announcements = """function loadDynamicAnnouncements() {
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
        }"""

assert old_announcements in content, "old_announcements not found in js/main.js"
content = content.replace(old_announcements, new_announcements)

# 5. Update loadDynamicNews
old_news = """function loadDynamicNews() {
    let newsData = null;
    try {
        const stored = localStorage.getItem('sdn_berita_data');
        if (stored && !stored.includes('unsplash')) {
            const parsed = JSON.parse(stored);
            if (Array.isArray(parsed) && parsed.length > 0) {
                newsData = parsed;
            }
        }
    } catch (e) {}

    if (!newsData && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.berita) && window.SDN_DATABASE.berita.length > 0) {
        newsData = window.SDN_DATABASE.berita;
    }"""

new_news = """function loadDynamicNews() {
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
    }"""

assert old_news in content, "old_news not found in js/main.js"
content = content.replace(old_news, new_news)

# 6. Update loadDynamicSambutan
old_sambutan = """function loadDynamicSambutan() {
    let data = null;
    // 1. Cek LocalStorage dulu (perubahan langsung admin di browser ini)
    try {
        const raw = localStorage.getItem('sdn_sambutan_data');
        if (raw) {
            const parsed = JSON.parse(raw);
            if (parsed && (parsed.nama || parsed.foto || parsed.isi)) {
                data = Object.assign({}, defaultMainSambutan, parsed);
            }
        }
    } catch (e) {}

    // 2. Fallback ke window.SDN_DATABASE
    if (!data && window.SDN_DATABASE && window.SDN_DATABASE.sambutan && typeof window.SDN_DATABASE.sambutan === 'object') {
        data = Object.assign({}, defaultMainSambutan, window.SDN_DATABASE.sambutan);
    }"""

new_sambutan = """function loadDynamicSambutan() {
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
    }"""

assert old_sambutan in content, "old_sambutan not found in js/main.js"
content = content.replace(old_sambutan, new_sambutan)

# 7. Update loadDynamicTeachers
old_teachers = """function loadDynamicTeachers() {
    let teachers = null;
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

    if (!teachers && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.guru) && window.SDN_DATABASE.guru.length > 0) {
        teachers = window.SDN_DATABASE.guru;
    }"""

new_teachers = """function loadDynamicTeachers() {
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
    }"""

assert old_teachers in content, "old_teachers not found in js/main.js"
content = content.replace(old_teachers, new_teachers)

# 8. Update loadDynamicStudentData
old_students = """function loadDynamicStudentData() {
    let s = null;
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

    if (!s && window.SDN_DATABASE && window.SDN_DATABASE.siswa && typeof window.SDN_DATABASE.siswa === 'object') {
        s = Object.assign({}, defaultMainSiswaData, window.SDN_DATABASE.siswa);
    }"""

new_students = """function loadDynamicStudentData() {
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
    }"""

assert old_students in content, "old_students not found in js/main.js"
content = content.replace(old_students, new_students)

# 9. Update loadDynamicSapras
old_sapras = """function loadDynamicSapras() {
    let items = null;
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

    if (!items && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.sarpras) && window.SDN_DATABASE.sarpras.length > 0) {
        items = window.SDN_DATABASE.sarpras;
    }"""

new_sapras = """function loadDynamicSapras() {
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
    }"""

assert old_sapras in content, "old_sapras not found in js/main.js"
content = content.replace(old_sapras, new_sapras)

# 10. Update loadDynamicKolaborasi
old_kolaborasi = """function loadDynamicKolaborasi() {
    const container = document.getElementById('kolaborasiListContainer');
    if (!container) return;

    let items = null;
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

    if (!items && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.kolaborasi) && window.SDN_DATABASE.kolaborasi.length > 0) {
        items = window.SDN_DATABASE.kolaborasi;
    }"""

new_kolaborasi = """function loadDynamicKolaborasi() {
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
    }"""

assert old_kolaborasi in content, "old_kolaborasi not found in js/main.js"
content = content.replace(old_kolaborasi, new_kolaborasi)

# 11. Update loadDynamicKKG
old_kkg = """function loadDynamicKKG() {
    let kkgData = null;
    try {
        const raw = localStorage.getItem('sdn_kkg_data');
        if (raw) kkgData = JSON.parse(raw);
    } catch (e) {}

    if (!kkgData && window.SDN_DATABASE && window.SDN_DATABASE.kkg) {
        kkgData = window.SDN_DATABASE.kkg;
    }"""

new_kkg = """function loadDynamicKKG() {
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
    }"""

assert old_kkg in content, "old_kkg not found in js/main.js"
content = content.replace(old_kkg, new_kkg)

# 12. Update loadDynamicSOP
old_sop = """function loadDynamicSOP() {
    let sopData = null;
    try {
        const raw = localStorage.getItem('sdn_sop_data');
        if (raw) sopData = JSON.parse(raw);
    } catch (e) {}

    if (!sopData && window.SDN_DATABASE && window.SDN_DATABASE.sop_data) {
        sopData = window.SDN_DATABASE.sop_data;
    }"""

new_sop = """function loadDynamicSOP() {
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
    }"""

assert old_sop in content, "old_sop not found in js/main.js"
content = content.replace(old_sop, new_sop)

# 13. Update loadDynamicAgenda
old_agenda = """function loadDynamicAgenda() {
    const container = document.getElementById('dynamicAgendaContainer');
    if (!container) return;

    let items = null;
    try {
        const raw = localStorage.getItem('sdn_agenda_data');
        if (raw) {
            const parsed = JSON.parse(raw);
            if (Array.isArray(parsed) && parsed.length > 0) items = parsed;
        }
    } catch (e) {}

    if (!items && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.agenda) && window.SDN_DATABASE.agenda.length > 0) {
        items = window.SDN_DATABASE.agenda;
    }"""

new_agenda = """function loadDynamicAgenda() {
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
    }"""

assert old_agenda in content, "old_agenda not found in js/main.js"
content = content.replace(old_agenda, new_agenda)

# 14. Update renderPPDBPublicInfo
old_ppdb = """function renderPPDBPublicInfo() {
    let cfg = null;
    try {
        const raw = localStorage.getItem('sdn_ppdb_config');
        if (raw) {
            const parsed = JSON.parse(raw);
            if (parsed && typeof parsed === 'object') cfg = parsed;
        }
    } catch (e) {}

    if (!cfg && window.SDN_DATABASE && window.SDN_DATABASE.ppdb_config) {
        cfg = window.SDN_DATABASE.ppdb_config;
    }"""

new_ppdb = """function renderPPDBPublicInfo() {
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
    }"""

assert old_ppdb in content, "old_ppdb not found in js/main.js"
content = content.replace(old_ppdb, new_ppdb)

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: All 14 updates cleanly applied to js/main.js!")
