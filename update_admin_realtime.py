# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_content = f.read()

# 1. Update syncToServer in js/admin.js
old_sync_to_server = """function syncToServer(category, data) {
    showSyncToast('☁️ Menyimpan langsung ke Google Cloud Database...');

    // 1. Simpan langsung ke Google Firebase (Cloud Database) agar seketika berubah di semua HP & Laptop di dunia
    const cloudUrl = (category === 'all')
        ? 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json'
        : `https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/${category}.json`;

    fetch(cloudUrl, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => {
        if (res.ok) {
            showSyncToast('🎉 SUKSES! Perubahan langsung aktif & detik ini juga tayang di semua HP & Laptop!');
        } else {
            showSyncToast('⚠️ Database Google sedang memproses. Pastikan Rules sudah aktif.', true);
        }
    })
    .catch(err => {
        console.warn('Cloud sync error:', err);
    });

    // 2. Jika sedang membuka dari server lokal laptop, sinkronkan juga ke file lokal
    if (window.location.origin.includes('localhost') || window.location.origin.includes('127.0.0.1')) {
        fetch('/api/sync_data', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ category: category, data: data })
        }).catch(() => {});
    }
}"""

new_sync_to_server = """function syncToServer(category, data) {
    showSyncToast('☁️ Menyimpan langsung ke Google Cloud Database...');

    // 1. Simpan langsung ke Google Firebase (Cloud Database)
    // Menggunakan PATCH ke root node agar data_sekolah.json & child node terupdate seketika
    const rootUrl = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json';
    const rootPayload = (category === 'all') ? data : { [category]: data };

    fetch(rootUrl, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(rootPayload)
    })
    .then(res => {
        if (res.ok) {
            showSyncToast('🎉 SUKSES! Perubahan langsung aktif & detik ini juga tayang di semua HP & Laptop!');
        } else {
            // Fallback PUT jika PATCH bermasalah
            const subUrl = (category === 'all')
                ? rootUrl
                : `https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/${category}.json`;
            fetch(subUrl, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            }).then(r => {
                if (r.ok) showSyncToast('🎉 SUKSES! Perubahan langsung aktif di internet!');
            }).catch(() => {});
        }
    })
    .catch(err => {
        console.warn('Cloud sync error:', err);
        // Fallback PUT ke category node
        if (category !== 'all') {
            const subUrl = `https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/${category}.json`;
            fetch(subUrl, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            }).then(r => {
                if (r.ok) showSyncToast('🎉 SUKSES! Perubahan langsung aktif di internet!');
            }).catch(() => {});
        }
    });

    // 2. Jika sedang membuka dari server lokal laptop, sinkronkan juga ke file lokal
    if (window.location.origin.includes('localhost') || window.location.origin.includes('127.0.0.1')) {
        fetch('/api/sync_data', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ category: category, data: data })
        }).catch(() => {});
    }
}"""

assert old_sync_to_server in admin_content, "old_sync_to_server not found in js/admin.js"
admin_content = admin_content.replace(old_sync_to_server, new_sync_to_server)

# 2. Update cloud fetch on DOMContentLoaded in js/admin.js
old_admin_fetch = """    // Sinkronisasi otomatis data terbaru dari Google Cloud saat dashboard admin dibuka di HP/Laptop mana saja
    if (typeof fetch === 'function') {
        fetch('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json?t=' + Date.now(), { cache: 'no-store' })
            .then(res => res.json())
            .then(db => {
                if (db && typeof db === 'object') {
                    if (db.berita) localStorage.setItem('sdn_berita_data', JSON.stringify(db.berita));
                    if (db.sambutan) localStorage.setItem('sdn_sambutan_data', JSON.stringify(db.sambutan));
                    if (db.pengumuman) localStorage.setItem('sdn_pengumuman_data', JSON.stringify(db.pengumuman));
                    if (db.galeri) localStorage.setItem('sdn_galeri_data', JSON.stringify(db.galeri));
                    if (db.guru) localStorage.setItem('sdn_guru_data', JSON.stringify(db.guru));
                    if (db.siswa) {
                        localStorage.setItem('sdn_siswa_counts', JSON.stringify(db.siswa));
                        localStorage.setItem('sdn_siswa_kelas', JSON.stringify(db.siswa));
                    }
                    if (db.sarpras) localStorage.setItem('sdn_sarpras_data', JSON.stringify(db.sarpras));
                    if (db.kolaborasi) localStorage.setItem('sdn_kolaborasi_data', JSON.stringify(db.kolaborasi));
                    if (db.kkg) localStorage.setItem('sdn_kkg_data', JSON.stringify(db.kkg));
                    if (db.sop_data) localStorage.setItem('sdn_sop_data', JSON.stringify(db.sop_data));
                    if (db.ppdb_config) localStorage.setItem('sdn_ppdb_config', JSON.stringify(db.ppdb_config));
                    if (db.ppdb_submissions) localStorage.setItem('sdn_ppdb_submissions', JSON.stringify(db.ppdb_submissions));

                    initSambutanManager();
                    initBeritaManager();
                    initPengumumanManager();
                    initSiswaManager();
                    initGuruManager();
                    initPPDBConfigManager();
                    initPPDBManager();
                    initGaleriManager();
                    initSarprasManager();
                    initKolaborasiManager();
                    initKKGManager();
                    initSOPManager();
                }
            })
            .catch(() => {});
    }"""

new_admin_fetch = """    // Cek protokol file:// untuk memberi tahu pengguna bila membuka file offline laptop
    if (window.location.protocol === 'file:') {
        const warn = document.getElementById('fileProtocolWarning');
        if (warn) warn.style.display = 'block';
    }

    // Sinkronisasi otomatis data terbaru dari Google Cloud saat dashboard admin dibuka di HP/Laptop mana saja
    if (typeof fetch === 'function') {
        fetch('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json?t=' + Date.now(), { cache: 'no-store' })
            .then(res => res.json())
            .then(db => {
                if (db && typeof db === 'object') {
                    window.SDN_DATABASE = Object.assign(window.SDN_DATABASE || {}, db);

                    function safeAdminSet(k, v) {
                        if (!v) return;
                        try {
                            localStorage.setItem(k, typeof v === 'string' ? v : JSON.stringify(v));
                        } catch (e) {}
                    }

                    safeAdminSet('sdn_sambutan_data', db.sambutan);
                    safeAdminSet('sdn_berita_data', db.berita);
                    safeAdminSet('sdn_pengumuman_data', db.pengumuman);
                    safeAdminSet('sdn_guru_data', db.guru);
                    safeAdminSet('sdn_sarpras_data', db.sarpras);
                    safeAdminSet('sdn_kolaborasi_data', db.kolaborasi);
                    safeAdminSet('sdn_kkg_data', db.kkg);
                    safeAdminSet('sdn_sop_data', db.sop_data);
                    safeAdminSet('sdn_ppdb_config', db.ppdb_config);
                    safeAdminSet('sdn_ppdb_submissions', db.ppdb_submissions);
                    if (db.siswa) {
                        safeAdminSet('sdn_siswa_counts', db.siswa);
                        safeAdminSet('sdn_siswa_kelas', db.siswa);
                    }
                    if (db.galeri) safeAdminSet('sdn_galeri_data', db.galeri);

                    // Re-render data formulir dan tabel agar admin melihat data teranyar dari cloud
                    if (typeof window.refreshAdminManagers === 'function') {
                        window.refreshAdminManagers();
                    }
                }
            })
            .catch(() => {});
    }"""

assert old_admin_fetch in admin_content, "old_admin_fetch not found in js/admin.js"
admin_content = admin_content.replace(old_admin_fetch, new_admin_fetch)

# 3. Update getBeritaData in js/admin.js
old_get_berita = """    function getBeritaData() {
        const raw = localStorage.getItem('sdn_berita_data');
        if (raw && !raw.includes('unsplash')) {
            try {
                const parsed = JSON.parse(raw);
                return Array.isArray(parsed) ? parsed : defaultBeritaList;
            } catch (e) {
                return defaultBeritaList;
            }
        }
        saveBeritaData(defaultBeritaList);
        return defaultBeritaList;
    }"""

new_get_berita = """    function getBeritaData() {
        if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.berita) && window.SDN_DATABASE.berita.length > 0) {
            return window.SDN_DATABASE.berita;
        }
        const raw = localStorage.getItem('sdn_berita_data');
        if (raw && !raw.includes('unsplash')) {
            try {
                const parsed = JSON.parse(raw);
                return Array.isArray(parsed) ? parsed : defaultBeritaList;
            } catch (e) {
                return defaultBeritaList;
            }
        }
        return defaultBeritaList;
    }"""

assert old_get_berita in admin_content, "old_get_berita not found in js/admin.js"
admin_content = admin_content.replace(old_get_berita, new_get_berita)

# 4. Guard form submission bindings in initBeritaManager
old_berita_submit_bind = """    // Submit form tambah / simpan edit berita
    if (form) {
        form.addEventListener('submit', async function(e) {"""

new_berita_submit_bind = """    // Submit form tambah / simpan edit berita
    if (form && !form._bound) {
        form._bound = true;
        form.addEventListener('submit', async function(e) {"""

assert old_berita_submit_bind in admin_content, "old_berita_submit_bind not found in js/admin.js"
admin_content = admin_content.replace(old_berita_submit_bind, new_berita_submit_bind)

# 5. Add window.refreshAdminManagers helper function
refresh_helper = """
// REFRESH SEMUA TAMPILAN ADMIN SAAT DATA CLOUD TELAH DIMUAT
window.refreshAdminManagers = function() {
    try { if (typeof renderBerita === 'function') renderBerita(); } catch (e) {}
    try { if (typeof renderPengumuman === 'function') renderPengumuman(); } catch (e) {}
    try { if (typeof renderGaleri === 'function') renderGaleri(); } catch (e) {}
    try { if (typeof renderGuruTable === 'function') renderGuruTable(); } catch (e) {}
    try { if (typeof renderSarpras === 'function') renderSarpras(); } catch (e) {}
    try { if (typeof renderKolaborasiTable === 'function') renderKolaborasiTable(); } catch (e) {}
    try { if (typeof renderKKGTable === 'function') renderKKGTable(); } catch (e) {}
    try { if (typeof populateSOPForm === 'function') populateSOPForm(); } catch (e) {}
    try { if (typeof populateKKGProfileForm === 'function') populateKKGProfileForm(); } catch (e) {}
    try { if (typeof populateSiswaForm === 'function') populateSiswaForm(); } catch (e) {}
    try { if (typeof populateSambutanForm === 'function') populateSambutanForm(); } catch (e) {}
};
"""

admin_content += refresh_helper

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(admin_content)

print("SUCCESS: js/admin.js updated cleanly!")

# Update admin.html with warning banner and connection status
with open('admin.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

warning_banner = """    <!-- BANNER PERINGATAN BILA DIBUKA DARI FILE OFFLINE LAPTOP (file:///) -->
    <div id="fileProtocolWarning" style="display: none; background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); border-bottom: 2px solid #f59e0b; padding: 12px 20px; text-align: center; font-size: 13px; color: #92400e; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        ⚠️ <strong>Perhatian Pengelola:</strong> Anda sedang membuka file Admin secara offline dari folder laptop (<code>file:///</code>). 
        Agar berita, foto, dan pengumuman yang Anda buat <strong>langsung otomatis tayang di internet (HP semua orang)</strong> tanpa perlu buka file atau jalankan .bat, silakan gunakan Dashboard Admin Online Resmi:
        <a href="https://sdninpresarso8.sch.id/admin.html" target="_blank" style="display: inline-block; margin-left: 8px; background: #d97706; color: #ffffff; padding: 5px 16px; border-radius: 6px; text-decoration: none; font-weight: 800; font-size: 12px; box-shadow: 0 2px 6px rgba(217,119,6,0.3);">🌐 Buka Admin Online Resmi (sdninpresarso8.sch.id/admin.html) →</a>
    </div>
"""

old_header_end = "</header>\n\n    <!-- LAYOUT DASHBOARD -->"
new_header_end = "</header>\n\n" + warning_banner + "\n    <!-- LAYOUT DASHBOARD -->"

if old_header_end in html_content:
    html_content = html_content.replace(old_header_end, new_header_end, 1)

status_badge = """                <div id="cloudConnectionStatus" style="display: flex; align-items: center; gap: 6px; font-size: 12px; color: #047857; background: #ecfdf5; border: 1px solid #a7f3d0; padding: 6px 14px; border-radius: 999px; font-weight: 700;" title="Terhubung langsung ke Google Cloud Realtime Database">
                    <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #10b981; box-shadow: 0 0 6px #10b981;"></span>
                    <span>Cloud Live Realtime</span>
                </div>
"""

old_clock_div = """                <div style="display: flex; align-items: center; gap: 6px; font-size: 12px; color: #475569; background: #f1f5f9; padding: 6px 14px; border-radius: 999px; font-weight: 600;">
                    <span>🕒</span>
                    <span id="witClock">Memuat waktu...</span>
                </div>"""

if old_clock_div in html_content:
    html_content = html_content.replace(old_clock_div, status_badge + old_clock_div, 1)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS: admin.html updated cleanly!")
