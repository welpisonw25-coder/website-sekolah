import re

with open("js/main.js", "r", encoding="utf-8") as f:
    code = f.read()

# 1. NEW loadDynamicNews
new_loadDynamicNews = """
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
    }

    if (!newsData) newsData = defaultMainNewsList;
    window._allPublicNews = newsData;

    // 1. RENDER DI BERANDA (index.html: #homeNewsGrid) - HANYA 3 TERBARU
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
                    <img src="${imgThumb}" alt="${escapeHTML(item.judul)}" class="news-img">
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

    // 2. RENDER DI HALAMAN BERITA DENGAN PAGINASI & FILTER
    const beritaGrid = document.getElementById('beritaListGrid') || (document.title.includes('Berita') ? document.querySelector('.news-grid') : null);
    if (beritaGrid) {
        window.filterPublicNews(1);
    }
}
"""

pos_news_start = code.find("function loadDynamicNews()")
pos_news_end = code.find("/* -------------------------------------------------------------------\n   10B. SINKRONISASI SAMBUTAN KEPALA SEKOLAH", pos_news_start)

if pos_news_start != -1 and pos_news_end != -1:
    code = code[:pos_news_start] + new_loadDynamicNews + "\n\n" + code[pos_news_end:]
    print("✔ loadDynamicNews replaced!")

# 2. NEW loadDynamicGallery
new_loadDynamicGallery = """
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
    try {
        const raw = localStorage.getItem('sdn_galeri_data');
        if (raw && !raw.includes('unsplash')) {
            const parsed = JSON.parse(raw);
            if (Array.isArray(parsed)) items = parsed;
        }
    } catch (e) {}

    if (!items && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.galeri)) {
        items = window.SDN_DATABASE.galeri;
    }

    if (items) {
        window._allPublicGallery = items;
        window.filterPublicGallery(1);
    }
}
"""

pos_gal_start = code.find("function loadDynamicGallery()")
pos_gal_end = code.find("function initGalleryLightbox()", pos_gal_start)

if pos_gal_start != -1 and pos_gal_end != -1:
    code = code[:pos_gal_start] + new_loadDynamicGallery + "\n\n" + code[pos_gal_end:]
    print("✔ loadDynamicGallery replaced!")

# 3. NEW loadDynamicKKG
new_loadDynamicKKG = """
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
    try {
        const raw = localStorage.getItem('sdn_kkg_data');
        if (raw) kkgData = JSON.parse(raw);
    } catch (e) {}

    if (!kkgData && window.SDN_DATABASE && window.SDN_DATABASE.kkg) {
        kkgData = window.SDN_DATABASE.kkg;
    }

    if (!kkgData) return;

    const jadwalList = Array.isArray(kkgData.jadwal_pertemuan) ? kkgData.jadwal_pertemuan : (Array.isArray(kkgData) ? kkgData : []);
    window._allPublicKKG = jadwalList;

    window.filterPublicKKG(1);

    // Render galeri dokumentasi KKG jika ada container
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
    }
}
"""

pos_kkg_start = code.find("function loadDynamicKKG()")
pos_kkg_end = code.find("/* -------------------------------------------------------------------\n   AGENDA SEKOLAH DINAMIS", pos_kkg_start)
if pos_kkg_end == -1:
    pos_kkg_end = code.find("function loadDynamicAgenda()", pos_kkg_start)

if pos_kkg_start != -1 and pos_kkg_end != -1:
    code = code[:pos_kkg_start] + new_loadDynamicKKG + "\n\n" + code[pos_kkg_end:]
    print("✔ loadDynamicKKG replaced!")

# 4. NEW loadDynamicKolaborasi filter
new_loadDynamicKolaborasi = """
/* -------------------------------------------------------------------
   KEMITRAAN & KOLABORASI 6 PILAR DENGAN PENCARIAN CEPAT
   ------------------------------------------------------------------- */
window._allPublicMitra = [];

window.filterPublicMitra = function() {
    const container = document.getElementById('kolaborasiListContainer');
    if (!container) return;

    const searchInput = document.getElementById('publicMitraSearchInput');
    const query = (searchInput ? searchInput.value : '').trim().toLowerCase();

    const filtered = (window._allPublicMitra || []).filter(item => {
        if (!query) return true;
        const judul = (item.judul || '').toLowerCase();
        const ringkasan = (item.ringkasan || '').toLowerCase();
        const mitra = (item.mitra || '').toLowerCase();
        const pic = (item.penanggung_jawab || '').toLowerCase();
        const uraian = Array.isArray(item.uraian_kerja) ? item.uraian_kerja.join(' ').toLowerCase() : (item.uraian_kerja || '').toLowerCase();
        return judul.includes(query) || ringkasan.includes(query) || mitra.includes(query) || pic.includes(query) || uraian.includes(query);
    });

    if (filtered.length === 0) {
        container.innerHTML = `
            <div style="text-align: center; padding: 45px 20px; background: #f8fafc; border-radius: 12px; border: 1.5px dashed #cbd5e1; color: #64748b;">
                <span style="font-size: 32px; display: block; margin-bottom: 8px;">🤝</span>
                <strong style="color: #1e293b; font-size: 16px;">Tidak ditemukan mitra kerjasama yang cocok.</strong>
                <p style="font-size: 13px; margin: 4px 0 0;">Coba kata kunci lain seperti: Puskesmas, Polsek, Komite, Bank, dsb.</p>
            </div>
        `;
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

    container.innerHTML = '';
    filtered.forEach((item, index) => {
        const color = borderColors[index % borderColors.length];
        const badge = badgeColors[index % badgeColors.length];
        const icon = item.icon || '🤝';
        const judul = item.judul || ('Pilar Kemitraan ' + (index + 1));
        const kategori = item.kategori || 'KEMITRAAN SEKOLAH';
        const ringkasan = item.ringkasan || '';
        const pic = item.penanggung_jawab || 'Dewan Guru & Kepala Sekolah';
        const periode = item.periode || 'Berkala & Rutin';
        const status = item.status || 'Aktif Berjalan Rutin';

        let uraianList = [];
        if (Array.isArray(item.uraian_kerja)) {
            uraianList = item.uraian_kerja;
        } else if (typeof item.uraian_kerja === 'string') {
            uraianList = item.uraian_kerja.split('\\n').map(s => s.trim().replace(/^[-*•\\d.]+\\s*/, '')).filter(s => s.length > 0);
        }

        const listHtml = uraianList.map(u => '<li>' + escapeHTML(u) + '</li>').join('');

        let fotoHtml = '';
        if (item.foto) {
            fotoHtml = `
                <div style="margin-bottom: 18px; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0; background: #0f172a; box-shadow: 0 4px 14px rgba(0,0,0,0.08);">
                    <img src="${item.foto}" alt="${escapeHTML(judul)}" style="width: 100%; max-height: 380px; object-fit: cover; display: block; cursor: pointer;" onclick="if(window.openLightboxWith) window.openLightboxWith('${item.foto}', '${escapeHTML(judul)}')">
                    <div style="padding: 8px 14px; background: rgba(15, 23, 42, 0.9); color: #cbd5e1; font-size: 11.5px; display: flex; justify-content: space-between; align-items: center;">
                        <span>📷 Dokumentasi Resmi: ${escapeHTML(item.keterangan_foto || judul)}</span>
                        <button type="button" onclick="if(window.openLightboxWith) window.openLightboxWith('${item.foto}', '${escapeHTML(judul)}')" style="background: rgba(255,255,255,0.2); color: #ffffff; border: none; padding: 2px 8px; border-radius: 4px; font-size: 10px; cursor: pointer; font-weight: 700;">
                            🔍 Perbesar
                        </button>
                    </div>
                </div>
            `;
        }

        const card = document.createElement('div');
        card.className = 'card';
        card.style.cssText = `padding: 28px; border-left: 6px solid ${color}; margin-bottom: 25px; box-shadow: 0 4px 14px rgba(0,0,0,0.04);`;
        card.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; margin-bottom: 14px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <span style="font-size: 32px; background: #f8fafc; width: 52px; height: 52px; display: flex; align-items: center; justify-content: center; border-radius: 12px; border: 1px solid #e2e8f0;">${icon}</span>
                    <div>
                        <span class="badge-tag" style="background: ${badge.bg}; color: ${badge.color}; font-size: 11.5px; font-weight: 700;">${escapeHTML(kategori)}</span>
                        <h3 style="font-size: 20px; font-weight: 800; color: #0f172a; margin: 4px 0 0 0;">${escapeHTML(judul)}</h3>
                    </div>
                </div>
                <span style="background: #dcfce7; color: #166534; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 999px;">
                    ✔ ${escapeHTML(status)}
                </span>
            </div>

            <p style="font-size: 14px; color: #475569; line-height: 1.6; margin-bottom: 16px;">
                ${escapeHTML(ringkasan)}
            </p>

            ${fotoHtml}

            ${listHtml ? `
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; margin-bottom: 14px;">
                    <h4 style="font-size: 13.5px; font-weight: 800; color: #0f172a; margin: 0 0 8px 0;">📋 Rincian Kegiatan & Program Kerjasama:</h4>
                    <ul style="margin: 0; padding-left: 20px; font-size: 13px; color: #334155; line-height: 1.7;">
                        ${listHtml}
                    </ul>
                </div>
            ` : ''}

            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; font-size: 12.5px; color: #64748b; border-top: 1px dashed #e2e8f0; padding-top: 12px;">
                <div>👤 Penanggung Jawab: <strong style="color: #0f172a;">${escapeHTML(pic)}</strong></div>
                <div>⏱️ Siklus: <strong>${escapeHTML(periode)}</strong></div>
            </div>
        `;
        container.appendChild(card);
    });
};

function loadDynamicKolaborasi() {
    let items = null;
    try {
        const raw = localStorage.getItem('sdn_kolaborasi_data');
        if (raw) items = JSON.parse(raw);
    } catch (e) {}

    if (!items && window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.kolaborasi)) {
        items = window.SDN_DATABASE.kolaborasi;
    }

    if (!items || items.length === 0) return;
    window._allPublicMitra = items;
    window.filterPublicMitra();
}
"""

pos_kolab_start = code.find("function loadDynamicKolaborasi()")
pos_kolab_end = code.find("/* -------------------------------------------------------------------\n   12. PENGEMBANGAN GURU (K3S & KKG)", pos_kolab_start)

if pos_kolab_start != -1 and pos_kolab_end != -1:
    code = code[:pos_kolab_start] + new_loadDynamicKolaborasi + "\n\n" + code[pos_kolab_end:]
    print("✔ loadDynamicKolaborasi replaced!")

with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(code)

print("✔ js/main.js successfully updated with complete public pagination and live filtering!")
