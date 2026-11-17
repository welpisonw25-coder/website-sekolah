# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# 1. Update refreshDataFromCloud
old_refresh = "loadDynamicSOP();\n                renderPPDBPublicInfo();"
new_refresh = """loadDynamicSOP();
                loadDynamicProfil();
                loadDynamicKontak();
                loadDynamicBeranda();
                renderPPDBPublicInfo();"""
if old_refresh in main_js:
    main_js = main_js.replace(old_refresh, new_refresh)
    print("Patched refreshDataFromCloud")

# 2. Update DOMContentLoaded
old_dom_loaders = "loadDynamicSOP();\n\n    // Eksekusi pembaruan realtime"
new_dom_loaders = """loadDynamicSOP();
    loadDynamicProfil();
    loadDynamicKontak();
    loadDynamicBeranda();

    // Eksekusi pembaruan realtime"""
if old_dom_loaders in main_js:
    main_js = main_js.replace(old_dom_loaders, new_dom_loaders)
    print("Patched DOMContentLoaded loaders")

# 3. Draft filtering in loadDynamicNews
target_news = "if (!newsData) newsData = defaultMainNewsList;\n    window._allPublicNews = newsData;"
replace_news = """if (!newsData) newsData = defaultMainNewsList;
    // Filter konten draft agar tidak tampil pada pengunjung publik
    newsData = (newsData || []).filter(item => item && item.status !== 'draft');
    window._allPublicNews = newsData;"""
if target_news in main_js:
    main_js = main_js.replace(target_news, replace_news)
    print("Patched draft filter in loadDynamicNews")

# 4. Draft filtering in loadDynamicAnnouncements
target_ann = "if (!items) items = defaultMainAnnouncementsList;\n\n        // 1. RENDER PADA BERANDA (index.html: #homePengumumanGrid)"
replace_ann = """if (!items) items = defaultMainAnnouncementsList;
        // Filter draft pengumuman agar tidak tampil pada pengunjung publik
        items = (items || []).filter(item => item && item.status !== 'draft');

        // 1. RENDER PADA BERANDA (index.html: #homePengumumanGrid)"""
if target_ann in main_js:
    main_js = main_js.replace(target_ann, replace_ann)
    print("Patched draft filter in loadDynamicAnnouncements")

# 5. Draft filtering in loadDynamicGallery
target_gal = "if (!items) items = defaultMainGalleryList;\n\n        galleryGrid.innerHTML = '';"
replace_gal = """if (!items) items = defaultMainGalleryList;
        // Filter draft galeri agar tidak tampil pada pengunjung publik
        items = (items || []).filter(item => item && item.status !== 'draft');

        galleryGrid.innerHTML = '';"""
if target_gal in main_js:
    main_js = main_js.replace(target_gal, replace_gal)
    print("Patched draft filter in loadDynamicGallery")

# 6. Add loadDynamicProfil, loadDynamicKontak, loadDynamicBeranda
target_sop_end = "/* -------------------------------------------------------------------\n   11. PENDAFTARAN PPDB ONLINE SECARA REALTIME"
new_functions = """/* -------------------------------------------------------------------
   10C. SINKRONISASI PROFIL SEKOLAH DINAMIS (profil.html)
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
    const visiElem = document.getElementById('profilVisiQuote');
    if (visiElem && profilData.visi) {
        visiElem.textContent = `"${profilData.visi}"`;
    }

    // 2. Misi
    const misiElem = document.getElementById('profilMisiList');
    if (misiElem && Array.isArray(profilData.misi) && profilData.misi.length > 0) {
        misiElem.innerHTML = '';
        profilData.misi.forEach(m => {
            const li = document.createElement('li');
            li.textContent = m;
            misiElem.appendChild(li);
        });
    }

    // 3. Tujuan
    const tujuanElem = document.getElementById('profilTujuanList');
    if (tujuanElem && profilData.tujuan) {
        tujuanElem.innerHTML = '';
        const tujuanItems = Array.isArray(profilData.tujuan) ? profilData.tujuan : profilData.tujuan.split('\\n').filter(t => t.trim());
        tujuanItems.forEach(t => {
            const li = document.createElement('li');
            li.textContent = t.trim();
            tujuanElem.appendChild(li);
        });
    }

    // 4. Sejarah
    const sejarahCard = document.getElementById('profilSejarahCard');
    if (sejarahCard && profilData.sejarah) {
        const pContainer = sejarahCard.querySelector('div');
        if (pContainer) {
            const paragraphs = profilData.sejarah.split('\\n\\n').filter(p => p.trim());
            if (paragraphs.length > 0) {
                pContainer.innerHTML = paragraphs.map(p => `<p style="margin-bottom: 14px;">${escapeHTML(p)}</p>`).join('');
            }
        }
    }

    // 5. Identitas
    if (profilData.identitas) {
        const id = profilData.identitas;
        const npsn = document.getElementById('profilNPSN');
        if (npsn && id.npsn) npsn.textContent = id.npsn;
    }
}

/* -------------------------------------------------------------------
   10D. SINKRONISASI KONTAK SEKOLAH DINAMIS (kontak.html)
   ------------------------------------------------------------------- */
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

/* -------------------------------------------------------------------
   10E. SINKRONISASI BERANDA & MARQUEE DINAMIS (index.html)
   ------------------------------------------------------------------- */
function loadDynamicBeranda() {
    let berandaData = null;
    if (window.SDN_DATABASE && window.SDN_DATABASE.beranda && typeof window.SDN_DATABASE.beranda === 'object') {
        berandaData = window.SDN_DATABASE.beranda;
    }
    if (!berandaData) return;

    const marqueeElem = document.getElementById('heroMarqueeText');
    if (marqueeElem && berandaData.marquee) {
        marqueeElem.textContent = berandaData.marquee;
    }
}

"""

if target_sop_end in main_js:
    main_js = main_js.replace(target_sop_end, new_functions + target_sop_end)
    print("Added loadDynamicProfil, loadDynamicKontak, loadDynamicBeranda")

# 7. Update contactForm submit to push to Firebase pesan_kontak
target_contact_submit = "const message = document.getElementById('contactMessage')?.value || '';"
replace_contact_submit = """const message = document.getElementById('contactMessage')?.value || '';

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
        }"""
if target_contact_submit in main_js:
    main_js = main_js.replace(target_contact_submit, replace_contact_submit)
    print("Patched contactForm to save to Firebase pesan_kontak")

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(main_js)

print("Successfully updated js/main.js with CMS public integrations!")
