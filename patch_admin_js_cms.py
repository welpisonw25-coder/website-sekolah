# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

# 1. Update formBerita submit to capture status
target_berita_submit = "const judul = document.getElementById('beritaJudul').value.trim();"
replace_berita_submit = """const statusEl = document.getElementById('beritaStatus');
        const statusVal = statusEl ? statusEl.value : 'published';
        const judul = document.getElementById('beritaJudul').value.trim();"""
if target_berita_submit in admin_js:
    admin_js = admin_js.replace(target_berita_submit, replace_berita_submit, 1)
    print("Patched formBerita submit to capture status")

target_berita_obj = "foto: currentImageDataUrl || editItem.foto || 'images/gerbang-sekolah.jpg'"
replace_berita_obj = "foto: currentImageDataUrl || editItem.foto || 'images/gerbang-sekolah.jpg',\n                    status: statusVal"
if target_berita_obj in admin_js:
    admin_js = admin_js.replace(target_berita_obj, replace_berita_obj, 1)
    print("Patched berita object in editItem")

target_berita_new_obj = "foto: currentImageDataUrl || 'images/gerbang-sekolah.jpg'"
replace_berita_new_obj = "foto: currentImageDataUrl || 'images/gerbang-sekolah.jpg',\n                status: statusVal"
if target_berita_new_obj in admin_js:
    admin_js = admin_js.replace(target_berita_new_obj, replace_berita_new_obj, 1)
    print("Patched berita object in newItem")

# 2. Update formPengumuman submit to capture status
target_peng_submit = "const judul = document.getElementById('pengumumanJudul').value.trim();"
replace_peng_submit = """const statusEl = document.getElementById('pengumumanStatus');
        const statusVal = statusEl ? statusEl.value : 'published';
        const judul = document.getElementById('pengumumanJudul').value.trim();"""
if target_peng_submit in admin_js:
    admin_js = admin_js.replace(target_peng_submit, replace_peng_submit, 1)
    print("Patched formPengumuman submit to capture status")

# 3. Add Activity Logging & New Managers at the end of admin.js
new_managers_code = '''
/* -------------------------------------------------------------------
   14. SISTEM LOG AKTIVITAS PENGELOLA (AUDIT TRAIL)
   ------------------------------------------------------------------- */
function logAdminActivity(aksi, keterangan) {
    try {
        let logs = [];
        if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.admin_logs)) {
            logs = window.SDN_DATABASE.admin_logs;
        } else {
            try {
                const raw = localStorage.getItem('sdn_admin_logs');
                if (raw) logs = JSON.parse(raw);
            } catch (e) {}
        }

        const now = new Date();
        const waktuStr = now.toLocaleDateString('id-ID', { day: '2-digit', month: 'short', year: 'numeric' }) + ', ' +
                         now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' }) + ' WIT';

        const currentUser = localStorage.getItem('sdn_admin_user') || 'admin';
        const currentRole = (currentUser === 'kepsek' || currentUser === 'admin') ? 'Kepala Sekolah / Super Admin' : (currentUser === 'operator' ? 'Operator Sekolah' : 'Dewan Guru');

        const newEntry = {
            id: 'LOG-' + Date.now(),
            waktu: waktuStr,
            user: currentUser,
            role: currentRole,
            aksi: aksi || 'Pembaruan Data',
            keterangan: keterangan || '-'
        };

        logs.unshift(newEntry);
        if (logs.length > 50) logs = logs.slice(0, 50);

        if (window.SDN_DATABASE) window.SDN_DATABASE.admin_logs = logs;
        safeAdminSet('sdn_admin_logs', logs);

        // Sync to cloud
        syncToServer('admin_logs', logs);
        if (typeof renderActivityLogs === 'function') renderActivityLogs();
    } catch (err) {
        console.warn('Logging error:', err);
    }
}

function renderActivityLogs() {
    const tbody = document.getElementById('adminLogsTableBody');
    if (!tbody) return;

    let logs = [];
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.admin_logs)) {
        logs = window.SDN_DATABASE.admin_logs;
    } else {
        try {
            const raw = localStorage.getItem('sdn_admin_logs');
            if (raw) logs = JSON.parse(raw);
        } catch (e) {}
    }

    if (!logs || logs.length === 0) {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: #94a3b8; padding: 18px;">Belum ada catatan aktivitas tercatat.</td></tr>';
        return;
    }

    tbody.innerHTML = '';
    logs.slice(0, 25).forEach(l => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid #f1f5f9';
        tr.innerHTML = `
            <td style="padding: 9px 12px; font-weight: 600; color: #475569; white-space: nowrap;">📅 ${escapeHTML(l.waktu)}</td>
            <td style="padding: 9px 12px; font-weight: 700; color: #0284c7;">👤 ${escapeHTML(l.user)}</td>
            <td style="padding: 9px 12px; color: #334155;"><span style="background: #f1f5f9; padding: 2px 8px; border-radius: 4px; font-size: 11.5px; font-weight: 700;">${escapeHTML(l.role)}</span></td>
            <td style="padding: 9px 12px; font-weight: 700; color: #0f172a;">${escapeHTML(l.aksi)}</td>
            <td style="padding: 9px 12px; color: #64748b; font-size: 12.5px;">${escapeHTML(l.keterangan)}</td>
        `;
        tbody.appendChild(tr);
    });
}

/* -------------------------------------------------------------------
   15. PENGELOLA PROFIL SEKOLAH (Visi, Misi, Tujuan, Sejarah, Identitas)
   ------------------------------------------------------------------- */
function getProfilData() {
    if (window.SDN_DATABASE && window.SDN_DATABASE.profil && typeof window.SDN_DATABASE.profil === 'object') {
        return window.SDN_DATABASE.profil;
    }
    try {
        const raw = localStorage.getItem('sdn_profil_data');
        if (raw) return JSON.parse(raw);
    } catch (e) {}
    return {
        visi: "Terwujudnya Peserta Didik yang Beriman, Bertakwa, Berakhlak Mulia, Cerdas, Terampil, Mandiri, dan Berwawasan Lingkungan.",
        misi: [
            "Menanamkan nilai-nilai keagamaan dan budi pekerti luhur dalam kehidupan sehari-hari.",
            "Melaksanakan pembelajaran aktif, inovatif, kreatif, dan menyenangkan berbasis Kurikulum Merdeka.",
            "Meningkatkan literasi, numerasi, dan penguasaan TIK berbasis satelit Starlink.",
            "Mengembangkan bakat dan minat melalui kepramukaan dan seni budaya Papua.",
            "Menciptakan lingkungan sekolah yang bersih, asri, dan aman."
        ],
        tujuan: "Membentuk lulusan beriman, bertakwa, berkarakter Profil Pelajar Pancasila, menguasai ilmu pengetahuan dan teknologi, serta berjiwa mandiri.",
        sejarah: "SD Negeri Inpres Arso VIII didirikan pada tahun 1984 untuk melayani kebutuhan pendidikan dasar anak-anak masyarakat transmigrasi dan masyarakat adat di wilayah Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua.",
        identitas: {
            npsn: "60301140",
            nss: "101250302008",
            akreditasi: "A (Unggul)",
            status_kepemilikan: "Pemerintah Daerah",
            sk_pendirian: "01/SK/PDK/1984",
            sk_izin_operasional: "421/045/DISDIK/2018",
            luas_tanah: "5.400 m²",
            daya_listrik: "2.200 Watt",
            alamat: "Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua 99473"
        }
    };
}

function populateProfilForm() {
    const data = getProfilData();
    const visiEl = document.getElementById('profilVisiInput');
    const misiEl = document.getElementById('profilMisiInput');
    const tujuanEl = document.getElementById('profilTujuanInput');
    const sejarahEl = document.getElementById('profilSejarahInput');

    if (visiEl) visiEl.value = data.visi || '';
    if (misiEl) misiEl.value = Array.isArray(data.misi) ? data.misi.join('\\n') : (data.misi || '');
    if (tujuanEl) tujuanEl.value = Array.isArray(data.tujuan) ? data.tujuan.join('\\n') : (data.tujuan || '');
    if (sejarahEl) sejarahEl.value = data.sejarah || '';

    const id = data.identitas || {};
    const npsnEl = document.getElementById('identitasNPSN');
    const nssEl = document.getElementById('identitasNSS');
    const akredEl = document.getElementById('identitasAkreditasi');
    const kepemilikanEl = document.getElementById('identitasKepemilikan');
    const skPendirianEl = document.getElementById('identitasSKPendirian');
    const skOperasionalEl = document.getElementById('identitasSKOperasional');
    const luasEl = document.getElementById('identitasLuasTanah');
    const dayaEl = document.getElementById('identitasDayaListrik');
    const alamatEl = document.getElementById('identitasAlamat');

    if (npsnEl) npsnEl.value = id.npsn || '60301140';
    if (nssEl) nssEl.value = id.nss || '101250302008';
    if (akredEl) akredEl.value = id.akreditasi || 'A (Unggul)';
    if (kepemilikanEl) kepemilikanEl.value = id.status_kepemilikan || 'Pemerintah Daerah';
    if (skPendirianEl) skPendirianEl.value = id.sk_pendirian || '01/SK/PDK/1984';
    if (skOperasionalEl) skOperasionalEl.value = id.sk_izin_operasional || '421/045/DISDIK/2018';
    if (luasEl) luasEl.value = id.luas_tanah || '5.400 m²';
    if (dayaEl) dayaEl.value = id.daya_listrik || '2.200 Watt';
    if (alamatEl) alamatEl.value = id.alamat || 'Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua 99473';
}

function saveProfilData() {
    const data = {
        visi: document.getElementById('profilVisiInput')?.value.trim() || '',
        misi: (document.getElementById('profilMisiInput')?.value || '').split('\\n').map(m => m.trim()).filter(m => m.length > 0),
        tujuan: document.getElementById('profilTujuanInput')?.value.trim() || '',
        sejarah: document.getElementById('profilSejarahInput')?.value.trim() || '',
        identitas: {
            npsn: document.getElementById('identitasNPSN')?.value.trim() || '60301140',
            nss: document.getElementById('identitasNSS')?.value.trim() || '101250302008',
            akreditasi: document.getElementById('identitasAkreditasi')?.value.trim() || 'A (Unggul)',
            status_kepemilikan: document.getElementById('identitasKepemilikan')?.value.trim() || 'Pemerintah Daerah',
            sk_pendirian: document.getElementById('identitasSKPendirian')?.value.trim() || '01/SK/PDK/1984',
            sk_izin_operasional: document.getElementById('identitasSKOperasional')?.value.trim() || '421/045/DISDIK/2018',
            luas_tanah: document.getElementById('identitasLuasTanah')?.value.trim() || '5.400 m²',
            daya_listrik: document.getElementById('identitasDayaListrik')?.value.trim() || '2.200 Watt',
            alamat: document.getElementById('identitasAlamat')?.value.trim() || 'Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua 99473'
        }
    };

    if (window.SDN_DATABASE) window.SDN_DATABASE.profil = data;
    safeAdminSet('sdn_profil_data', data);
    syncToServer('profil', data);
    logAdminActivity('Pembaruan Profil Sekolah', 'Memperbarui Visi, Misi, Sejarah, dan Data Pokok Legalitas');
    showSyncToast('🎉 Profil Sekolah berhasil diperbarui dan aktif di internet!');
    alert('✅ Profil Sekolah berhasil disimpan dan langsung aktif di website publik!');
}

/* -------------------------------------------------------------------
   16. PENGELOLA KONTAK RESMI & KOTAK MASUK PESAN TAMU
   ------------------------------------------------------------------- */
function getKontakData() {
    if (window.SDN_DATABASE && window.SDN_DATABASE.kontak && typeof window.SDN_DATABASE.kontak === 'object') {
        return window.SDN_DATABASE.kontak;
    }
    try {
        const raw = localStorage.getItem('sdn_kontak_data');
        if (raw) return JSON.parse(raw);
    } catch (e) {}
    return {
        alamat: "Jalan Sulawesi, RW 03 / RT 05, Kampung Dukwia, Distrik Arso Barat, Kab. Keerom, Papua 99473",
        telepon: "0812-4821-9125",
        whatsapp: "6281248219125",
        email: "sdninpresarso8@gmail.com",
        jam_kerja: "Senin – Jumat: 07.15 – 12.30 WIT",
        maps_embed: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3985.748123456789!2d140.703999!3d-2.822991!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMsKwNDknMjIuOCJTIDE0MMKwNDInMTQuNCJF!5e0!3m2!1sid!2sid!4v1",
        koordinat: "Lat -2.822991º, Long 140.703999º"
    };
}

function populateKontakForm() {
    const data = getKontakData();
    const telpEl = document.getElementById('kontakInputTelepon');
    const waEl = document.getElementById('kontakInputWhatsApp');
    const emailEl = document.getElementById('kontakInputEmail');
    const jamEl = document.getElementById('kontakInputJamKerja');
    const alamatEl = document.getElementById('kontakInputAlamat');
    const coordEl = document.getElementById('kontakInputKoordinat');
    const mapsEl = document.getElementById('kontakInputMaps');

    if (telpEl) telpEl.value = data.telepon || '0812-4821-9125';
    if (waEl) waEl.value = data.whatsapp || '6281248219125';
    if (emailEl) emailEl.value = data.email || 'sdninpresarso8@gmail.com';
    if (jamEl) jamEl.value = data.jam_kerja || 'Senin – Jumat: 07.15 – 12.30 WIT';
    if (alamatEl) alamatEl.value = data.alamat || 'Jalan Sulawesi, RW 03 / RT 05, Kampung Dukwia, Distrik Arso Barat, Kab. Keerom, Papua 99473';
    if (coordEl) coordEl.value = data.koordinat || 'Lat -2.822991º, Long 140.703999º';
    if (mapsEl) mapsEl.value = data.maps_embed || '';

    renderPesanKontakTable();
}

function saveKontakData() {
    const data = {
        telepon: document.getElementById('kontakInputTelepon')?.value.trim() || '0812-4821-9125',
        whatsapp: document.getElementById('kontakInputWhatsApp')?.value.trim() || '6281248219125',
        email: document.getElementById('kontakInputEmail')?.value.trim() || 'sdninpresarso8@gmail.com',
        jam_kerja: document.getElementById('kontakInputJamKerja')?.value.trim() || 'Senin – Jumat: 07.15 – 12.30 WIT',
        alamat: document.getElementById('kontakInputAlamat')?.value.trim() || '',
        koordinat: document.getElementById('kontakInputKoordinat')?.value.trim() || '',
        maps_embed: document.getElementById('kontakInputMaps')?.value.trim() || ''
    };

    if (window.SDN_DATABASE) window.SDN_DATABASE.kontak = data;
    safeAdminSet('sdn_kontak_data', data);
    syncToServer('kontak', data);
    logAdminActivity('Pembaruan Kontak Sekolah', 'Memperbarui saluran komunikasi resmi dan nomor WhatsApp');
    showSyncToast('🎉 Informasi Kontak Resmi berhasil diperbarui di internet!');
    alert('✅ Informasi Kontak Sekolah berhasil disimpan!');
}

function getPesanKontakData() {
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.pesan_kontak)) {
        return window.SDN_DATABASE.pesan_kontak;
    }
    try {
        const raw = localStorage.getItem('sdn_pesan_kontak');
        if (raw) return JSON.parse(raw);
    } catch (e) {}
    return [
        {
            id: "MSG-001",
            nama: "Markus Wenda",
            telepon: "0813-4455-6677",
            subjek: "Informasi Siswa Pindahan",
            pesan: "Selamat siang Kepala Sekolah, kami berencana memindahkan anak kami ke kelas 4 di SDN Inpres Arso VIII. Mohon info kelengkapan berkasnya.",
            tanggal: "14 Nov 2026 10:15 WIT",
            status: "Ditanggapi"
        }
    ];
}

function renderPesanKontakTable() {
    const tbody = document.getElementById('pesanKontakTableBody');
    if (!tbody) return;

    const list = getPesanKontakData();
    if (!list || list.length === 0) {
        tbody.innerHTML = '<tr><td colspan="7" style="text-align: center; color: #94a3b8; padding: 20px;">Belum ada pesan masuk dari form kontak publik.</td></tr>';
        return;
    }

    tbody.innerHTML = '';
    list.forEach(item => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid #f1f5f9';
        const isAnswered = item.status === 'Ditanggapi' || item.status === 'Selesai';
        const statusBadge = isAnswered 
            ? '<span style="background: #dcfce7; color: #166534; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 999px;">✅ Ditanggapi</span>'
            : '<span style="background: #fee2e2; color: #991b1b; font-size: 11px; font-weight: 800; padding: 3px 8px; border-radius: 999px;">⏳ Menunggu</span>';

        const waClean = (item.telepon || '').replace(/[^0-9]/g, '');
        const waLink = waClean ? `https://wa.me/${waClean.startsWith('0') ? '62' + waClean.slice(1) : waClean}` : '#';

        tr.innerHTML = `
            <td style="padding: 10px 12px; font-size: 12px; color: #64748b; white-space: nowrap;">📅 ${escapeHTML(item.tanggal || '-')}</td>
            <td style="padding: 10px 12px; font-weight: 700; color: var(--primary-dark);">${escapeHTML(item.nama || '-')}</td>
            <td style="padding: 10px 12px; font-weight: 600; color: #0284c7;">${escapeHTML(item.telepon || '-')}</td>
            <td style="padding: 10px 12px; font-weight: 700;">${escapeHTML(item.subjek || '-')}</td>
            <td style="padding: 10px 12px; color: #475569; font-size: 13px; line-height: 1.5; max-width: 320px;">${escapeHTML(item.pesan || '-')}</td>
            <td style="padding: 10px 12px; white-space: nowrap;">${statusBadge}</td>
            <td style="padding: 10px 12px; text-align: center; white-space: nowrap;">
                <a href="${waLink}" target="_blank" class="btn" style="background: #25d366; color: white; padding: 5px 9px; font-size: 11.5px; border-radius: 6px; text-decoration: none; margin-right: 4px;" title="Balas via WhatsApp">💬 WA</a>
                <button type="button" onclick="togglePesanStatus('${item.id}');" class="btn" style="background: #f1f5f9; border: 1px solid #cbd5e1; color: #334155; padding: 5px 8px; font-size: 11px; border-radius: 6px; cursor: pointer; margin-right: 4px;" title="Tandai Status Selesai / Menunggu">✔️</button>
                <button type="button" onclick="deletePesanKontak('${item.id}');" class="btn" style="background: #fee2e2; border: 1px solid #fca5a5; color: #991b1b; padding: 5px 8px; font-size: 11px; border-radius: 6px; cursor: pointer;" title="Hapus Pesan">🗑️</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function togglePesanStatus(id) {
    const list = getPesanKontakData();
    const item = list.find(m => m.id === id);
    if (!item) return;

    item.status = (item.status === 'Ditanggapi' || item.status === 'Selesai') ? 'Belum Ditanggapi' : 'Ditanggapi';
    if (window.SDN_DATABASE) window.SDN_DATABASE.pesan_kontak = list;
    safeAdminSet('sdn_pesan_kontak', list);
    syncToServer('pesan_kontak', list);
    renderPesanKontakTable();
    showSyncToast('Status pesan diperbarui.');
}

function deletePesanKontak(id) {
    if (!confirm('Hapus pesan kontak ini?')) return;
    let list = getPesanKontakData();
    list = list.filter(m => m.id !== id);
    if (window.SDN_DATABASE) window.SDN_DATABASE.pesan_kontak = list;
    safeAdminSet('sdn_pesan_kontak', list);
    syncToServer('pesan_kontak', list);
    renderPesanKontakTable();
    logAdminActivity('Penghapusan Pesan Kontak', 'Menghapus pesan ID ' + id);
    showSyncToast('Pesan berhasil dihapus.');
}

/* -------------------------------------------------------------------
   17. PENGELOLA BERANDA (Running Text / Marquee & Tagline)
   ------------------------------------------------------------------- */
function populateBerandaForm() {
    let berandaData = null;
    if (window.SDN_DATABASE && window.SDN_DATABASE.beranda && typeof window.SDN_DATABASE.beranda === 'object') {
        berandaData = window.SDN_DATABASE.beranda;
    }
    const input = document.getElementById('berandaMarqueeInput');
    if (input && berandaData && berandaData.marquee) {
        input.value = berandaData.marquee;
    }
}

function saveBerandaMarquee() {
    const input = document.getElementById('berandaMarqueeInput');
    if (!input) return;
    const val = input.value.trim();

    let berandaData = (window.SDN_DATABASE && window.SDN_DATABASE.beranda) ? window.SDN_DATABASE.beranda : {};
    berandaData.marquee = val;

    if (window.SDN_DATABASE) window.SDN_DATABASE.beranda = berandaData;
    safeAdminSet('sdn_beranda_data', berandaData);
    syncToServer('beranda', berandaData);
    logAdminActivity('Pembaruan Teks Berjalan Beranda', 'Memperbarui teks pengumuman berjalan beranda');
    showSyncToast('🎉 Teks pengumuman berjalan berhasil disimpan dan aktif di Beranda!');
    alert('✅ Teks pengumuman berjalan Beranda berhasil diperbarui!');
}

/* -------------------------------------------------------------------
   18. PENGELOLA PENGGUNA & HAK AKSES SISTEM (MULTI-ROLE)
   ------------------------------------------------------------------- */
function getUserData() {
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.admin_users)) {
        return window.SDN_DATABASE.admin_users;
    }
    try {
        const raw = localStorage.getItem('sdn_admin_users');
        if (raw) return JSON.parse(raw);
    } catch (e) {}
    return [
        { id: "USR-001", username: "kepsek", nama: "Adi Puspito, S.Pd", role: "Kepala Sekolah", level: "superadmin", email: "adipuspito@gmail.com", status: "Aktif", akses: ["Semua Menu", "Publikasi", "Kelola Akun", "Hapus Data"] },
        { id: "USR-002", username: "operator", nama: "Warno, S.Pd", role: "Operator Sekolah", level: "operator", email: "operator.arso8@gmail.com", status: "Aktif", akses: ["Siswa", "PPDB", "Sarpras", "Berita", "Pengumuman", "Galeri", "Kontak"] },
        { id: "USR-003", username: "guru", nama: "Ferdinandus Belau, S.Pd", role: "Dewan Guru / Editor", level: "guru", email: "guru.arso8@gmail.com", status: "Aktif", akses: ["Berita", "Pengumuman", "KKG", "SOP", "Galeri"] }
    ];
}

function renderUserTable() {
    const tbody = document.getElementById('adminUsersTableBody');
    if (!tbody) return;

    const list = getUserData();
    tbody.innerHTML = '';
    list.forEach(u => {
        const tr = document.createElement('tr');
        tr.style.borderBottom = '1px solid #f1f5f9';
        const roleColor = u.level === 'superadmin' ? '#991b1b' : (u.level === 'operator' ? '#0369a1' : '#15803d');
        const roleBg = u.level === 'superadmin' ? '#fee2e2' : (u.level === 'operator' ? '#e0f2fe' : '#dcfce7');
        const aksesList = Array.isArray(u.akses) ? u.akses.join(', ') : (u.akses || '-');

        tr.innerHTML = `
            <td style="padding: 10px 12px; font-weight: 800; color: #0f172a;">👤 ${escapeHTML(u.username)}</td>
            <td style="padding: 10px 12px; font-weight: 700; color: var(--primary-dark);">${escapeHTML(u.nama)}</td>
            <td style="padding: 10px 12px;"><span style="background: ${roleBg}; color: ${roleColor}; font-size: 11.5px; font-weight: 800; padding: 3px 10px; border-radius: 999px;">${escapeHTML(u.role)}</span></td>
            <td style="padding: 10px 12px; color: #64748b; font-size: 12.5px;">${escapeHTML(u.email || '-')}</td>
            <td style="padding: 10px 12px; font-size: 12px; color: #334155;">${escapeHTML(aksesList)}</td>
            <td style="padding: 10px 12px;"><span style="background: #dcfce7; color: #166534; font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 4px;">Aktif</span></td>
            <td style="padding: 10px 12px; text-align: center; white-space: nowrap;">
                <button type="button" onclick="editUserRole('${u.id}');" class="btn" style="background: #f1f5f9; border: 1px solid #cbd5e1; color: #334155; padding: 4px 8px; font-size: 11px; border-radius: 6px; cursor: pointer; margin-right: 4px;" title="Ubah Wewenang">✏️ Edit</button>
                ${u.username !== 'kepsek' && u.username !== 'admin' ? `<button type="button" onclick="deleteUser('${u.id}');" class="btn" style="background: #fee2e2; border: 1px solid #fca5a5; color: #991b1b; padding: 4px 8px; font-size: 11px; border-radius: 6px; cursor: pointer;" title="Hapus Akun">🗑️</button>` : ''}
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function showAddUserModal() {
    const username = prompt('Masukkan Username baru (huruf kecil tanpa spasi, contoh: guru_budi):');
    if (!username) return;
    const cleanUser = username.trim().toLowerCase();

    const list = getUserData();
    if (list.some(u => u.username === cleanUser)) {
        alert('❌ Username sudah digunakan! Silakan gunakan username lain.');
        return;
    }

    const nama = prompt('Masukkan Nama Lengkap beserta Gelar:');
    if (!nama) return;

    const roleChoice = prompt('Pilih Peran Akun:\\n1 = Kepala Sekolah (Akses Penuh)\\n2 = Operator Sekolah (Data Pokok & Informasi)\\n3 = Dewan Guru (Editor Konten & Pembelajaran)\\n\\nKetik 1, 2, atau 3:', '3');
    let role = 'Dewan Guru / Editor';
    let level = 'guru';
    let akses = ['Berita', 'Pengumuman', 'KKG', 'SOP', 'Galeri'];

    if (roleChoice === '1') {
        role = 'Kepala Sekolah';
        level = 'superadmin';
        akses = ['Semua Menu', 'Publikasi', 'Kelola Akun', 'Hapus Data'];
    } else if (roleChoice === '2') {
        role = 'Operator Sekolah';
        level = 'operator';
        akses = ['Siswa', 'PPDB', 'Sarpras', 'Berita', 'Pengumuman', 'Galeri', 'Kontak'];
    }

    const email = prompt('Masukkan Alamat Email Pengguna:', `${cleanUser}@gmail.com`) || '';

    const newUser = {
        id: 'USR-' + Date.now(),
        username: cleanUser,
        nama: nama.trim(),
        role: role,
        level: level,
        email: email.trim(),
        status: 'Aktif',
        akses: akses
    };

    list.push(newUser);
    if (window.SDN_DATABASE) window.SDN_DATABASE.admin_users = list;
    safeAdminSet('sdn_admin_users', list);
    syncToServer('admin_users', list);
    renderUserTable();
    logAdminActivity('Penambahan Pengguna Baru', `Menambahkan akun ${cleanUser} dengan peran ${role}`);
    showSyncToast(`Akun ${cleanUser} berhasil ditambahkan.`);
    alert(`✅ Akun pengguna ${cleanUser} (${role}) berhasil ditambahkan ke sistem!`);
}

function editUserRole(id) {
    const list = getUserData();
    const u = list.find(item => item.id === id);
    if (!u) return;

    const newNama = prompt('Nama Lengkap:', u.nama);
    if (newNama) u.nama = newNama.trim();

    const newEmail = prompt('Email:', u.email);
    if (newEmail) u.email = newEmail.trim();

    const roleChoice = prompt('Pilih Peran Baru:\\n1 = Kepala Sekolah (Akses Penuh)\\n2 = Operator Sekolah\\n3 = Dewan Guru\\n\\nKetik 1, 2, atau 3 (atau biarkan kosong):');
    if (roleChoice === '1') {
        u.role = 'Kepala Sekolah';
        u.level = 'superadmin';
        u.akses = ['Semua Menu', 'Publikasi', 'Kelola Akun', 'Hapus Data'];
    } else if (roleChoice === '2') {
        u.role = 'Operator Sekolah';
        u.level = 'operator';
        u.akses = ['Siswa', 'PPDB', 'Sarpras', 'Berita', 'Pengumuman', 'Galeri', 'Kontak'];
    } else if (roleChoice === '3') {
        u.role = 'Dewan Guru / Editor';
        u.level = 'guru';
        u.akses = ['Berita', 'Pengumuman', 'KKG', 'SOP', 'Galeri'];
    }

    if (window.SDN_DATABASE) window.SDN_DATABASE.admin_users = list;
    safeAdminSet('sdn_admin_users', list);
    syncToServer('admin_users', list);
    renderUserTable();
    logAdminActivity('Pembaruan Wewenang Akun', `Memperbarui data dan hak akses akun ${u.username}`);
    showSyncToast('Data pengguna berhasil diperbarui.');
}

function deleteUser(id) {
    if (!confirm('Apakah Anda yakin ingin menghapus akun pengguna ini?')) return;
    let list = getUserData();
    const target = list.find(u => u.id === id);
    if (!target) return;

    list = list.filter(u => u.id !== id);
    if (window.SDN_DATABASE) window.SDN_DATABASE.admin_users = list;
    safeAdminSet('sdn_admin_users', list);
    syncToServer('admin_users', list);
    renderUserTable();
    logAdminActivity('Penghapusan Akun Pengguna', `Menghapus akun ${target.username} (${target.role})`);
    showSyncToast('Akun pengguna berhasil dihapus.');
}

// INJEKSI PADA REFRESH ADMIN MANAGERS
const _prevRefresh = window.refreshAdminManagers;
window.refreshAdminManagers = function() {
    if (typeof _prevRefresh === 'function') {
        try { _prevRefresh(); } catch (e) {}
    }
    try { populateProfilForm(); } catch (e) {}
    try { populateKontakForm(); } catch (e) {}
    try { populateBerandaForm(); } catch (e) {}
    try { renderUserTable(); } catch (e) {}
    try { renderActivityLogs(); } catch (e) {}
};

// INITIALIZATION DI AKHIR DOM READY
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        populateProfilForm();
        populateKontakForm();
        populateBerandaForm();
        renderUserTable();
        renderActivityLogs();
    }, 400);
});
'''

admin_js += new_managers_code

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(admin_js)

print("Successfully injected all CMS managers, audit logs, and user roles into js/admin.js!")
