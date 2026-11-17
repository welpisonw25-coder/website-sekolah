with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

# 1. Add sop_data to publishAllToOnline (around line 137)
old_publish = """        kkg: (typeof getKKGData === 'function') ? getKKGData() : (window.SDN_DATABASE.kkg || {}),
        ppdb_config: (typeof getPPDBConfig === 'function') ? getPPDBConfig() : {}"""
new_publish = """        kkg: (typeof getKKGData === 'function') ? getKKGData() : (window.SDN_DATABASE.kkg || {}),
        sop_data: (typeof getSOPData === 'function') ? getSOPData() : (window.SDN_DATABASE.sop_data || {}),
        ppdb_config: (typeof getPPDBConfig === 'function') ? getPPDBConfig() : {}"""
admin_js = admin_js.replace(old_publish, new_publish, 1)

# 2. Add initSOPManager to initial DOMContentLoaded and cloud fetch
old_init_calls = """    initKolaborasiManager();
    initKKGManager();
    initAccountSettings();"""
new_init_calls = """    initKolaborasiManager();
    initKKGManager();
    initSOPManager();
    initAccountSettings();"""
admin_js = admin_js.replace(old_init_calls, new_init_calls, 1)

old_cloud_kkg = """                    if (db.kkg) localStorage.setItem('sdn_kkg_data', JSON.stringify(db.kkg));"""
new_cloud_kkg = """                    if (db.kkg) localStorage.setItem('sdn_kkg_data', JSON.stringify(db.kkg));
                    if (db.sop_data) localStorage.setItem('sdn_sop_data', JSON.stringify(db.sop_data));"""
admin_js = admin_js.replace(old_cloud_kkg, new_cloud_kkg, 1)

old_cloud_init = """                    initKolaborasiManager();
                    initKKGManager();
                }"""
new_cloud_init = """                    initKolaborasiManager();
                    initKKGManager();
                    initSOPManager();
                }"""
admin_js = admin_js.replace(old_cloud_init, new_cloud_init, 1)

# 3. Add sop_data to initBackupRestoreManager
old_backup = """                    kolaborasi: localStorage.getItem('sdn_kolaborasi_data'),
                    kkg: localStorage.getItem('sdn_kkg_data'),"""
new_backup = """                    kolaborasi: localStorage.getItem('sdn_kolaborasi_data'),
                    kkg: localStorage.getItem('sdn_kkg_data'),
                    sop_data: localStorage.getItem('sdn_sop_data'),"""
admin_js = admin_js.replace(old_backup, new_backup, 1)

old_restore = """                        if (d.kkg) localStorage.setItem('sdn_kkg_data', d.kkg);"""
new_restore = """                        if (d.kkg) localStorage.setItem('sdn_kkg_data', d.kkg);
                        if (d.sop_data) localStorage.setItem('sdn_sop_data', d.sop_data);"""
admin_js = admin_js.replace(old_restore, new_restore, 1)

# 4. In initGuruManager: when guru changes, also trigger syncGuruWithSOP and populateSOPTeacherDropdowns
old_sync_guru = """        syncGuruWithSiswa(oldNama, nama, jabatan);"""
new_sync_guru = """        syncGuruWithSiswa(oldNama, nama, jabatan);
        if (typeof syncGuruWithSOP === 'function') syncGuruWithSOP(oldNama, nama);
        if (typeof populateSOPTeacherDropdowns === 'function') populateSOPTeacherDropdowns();"""
admin_js = admin_js.replace(old_sync_guru, new_sync_guru, 1)

old_sync_guru_new = """        syncGuruWithSiswa(null, nama, jabatan);"""
new_sync_guru_new = """        syncGuruWithSiswa(null, nama, jabatan);
        if (typeof populateSOPTeacherDropdowns === 'function') populateSOPTeacherDropdowns();"""
admin_js = admin_js.replace(old_sync_guru_new, new_sync_guru_new, 1)

# 5. Enhance initKKGManager to also manage cardKKGProfilManager
kkg_profil_logic = """
    // --- KELOLA PROFIL GUGUS 1, K3S & KKG KELOMPOK A/B (DINAMIS) ---
    const btnSimpanProfil = document.getElementById('btnSimpanKKGProfil');
    const btnResetProfil = document.getElementById('btnResetKKGProfil');

    function populateKKGProfilFields() {
        const data = getKKGData();
        const info = data.gusek_info || {};
        const k3s = data.k3s || {};
        const kelA = data.kkg_kelompok_a || {};
        const kelB = data.kkg_kelompok_b || {};

        const elSekretariat = document.getElementById('kkgSekretariatInput');
        if (elSekretariat) elSekretariat.value = info.alamat_sekretariat || '';

        const elWaktu = document.getElementById('kkgWaktuInput');
        if (elWaktu) elWaktu.value = info.hari_rutin || k3s.jadwal || '';

        const elKetua = document.getElementById('kkgKetuaInput');
        if (elKetua) elKetua.value = info.ketua || '';

        const elNIP = document.getElementById('kkgNIPKetuaInput');
        if (elNIP) elNIP.value = info.nip_ketua || '';

        const elDasarSK = document.getElementById('kkgDasarSKInput');
        if (elDasarSK) elDasarSK.value = info.dasar_hukum || info.tanggal_penetapan || '';

        const elDeskripsi = document.getElementById('kkgDeskripsiInput');
        if (elDeskripsi) elDeskripsi.value = info.deskripsi || '';

        const elK3SProg = document.getElementById('k3sProgramsInput');
        if (elK3SProg) elK3SProg.value = (k3s.uraian_kerja || []).join('\\n');

        const elKelAJudul = document.getElementById('kkgKelAJudul');
        if (elKelAJudul) elKelAJudul.value = kelA.nama_kelompok || kelA.judul || '';

        const elKelACakupan = document.getElementById('kkgKelACakupan');
        if (elKelACakupan) elKelACakupan.value = kelA.cakupan || kelA.sasaran || '';

        const elKelAJadwal = document.getElementById('kkgKelAJadwal');
        if (elKelAJadwal) elKelAJadwal.value = kelA.jadwal || '';

        const elKelAProg = document.getElementById('kkgKelAPrograms');
        if (elKelAProg) elKelAProg.value = (kelA.uraian_kerja || []).join('\\n');

        const elKelBJudul = document.getElementById('kkgKelBJudul');
        if (elKelBJudul) elKelBJudul.value = kelB.nama_kelompok || kelB.judul || '';

        const elKelBCakupan = document.getElementById('kkgKelBCakupan');
        if (elKelBCakupan) elKelBCakupan.value = kelB.cakupan || kelB.sasaran || '';

        const elKelBJadwal = document.getElementById('kkgKelBJadwal');
        if (elKelBJadwal) elKelBJadwal.value = kelB.jadwal || '';

        const elKelBProg = document.getElementById('kkgKelBPrograms');
        if (elKelBProg) elKelBProg.value = (kelB.uraian_kerja || []).join('\\n');
    }

    populateKKGProfilFields();

    if (btnSimpanProfil) {
        btnSimpanProfil.addEventListener('click', function() {
            const data = getKKGData();
            if (!data.gusek_info) data.gusek_info = {};
            if (!data.k3s) data.k3s = {};
            if (!data.kkg_kelompok_a) data.kkg_kelompok_a = {};
            if (!data.kkg_kelompok_b) data.kkg_kelompok_b = {};

            const elSekretariat = document.getElementById('kkgSekretariatInput');
            if (elSekretariat) {
                data.gusek_info.alamat_sekretariat = elSekretariat.value.trim();
                data.k3s.sekretariat = elSekretariat.value.trim();
            }

            const elWaktu = document.getElementById('kkgWaktuInput');
            if (elWaktu) {
                data.gusek_info.hari_rutin = elWaktu.value.trim();
                data.k3s.jadwal = elWaktu.value.trim();
            }

            const elKetua = document.getElementById('kkgKetuaInput');
            if (elKetua) data.gusek_info.ketua = elKetua.value.trim();

            const elNIP = document.getElementById('kkgNIPKetuaInput');
            if (elNIP) data.gusek_info.nip_ketua = elNIP.value.trim();

            const elDasarSK = document.getElementById('kkgDasarSKInput');
            if (elDasarSK) data.gusek_info.dasar_hukum = elDasarSK.value.trim();

            const elDeskripsi = document.getElementById('kkgDeskripsiInput');
            if (elDeskripsi) data.gusek_info.deskripsi = elDeskripsi.value.trim();

            const elK3SProg = document.getElementById('k3sProgramsInput');
            if (elK3SProg) {
                data.k3s.uraian_kerja = elK3SProg.value.split('\\n').map(l => l.trim()).filter(Boolean);
            }

            const elKelAJudul = document.getElementById('kkgKelAJudul');
            if (elKelAJudul) data.kkg_kelompok_a.nama_kelompok = elKelAJudul.value.trim();

            const elKelACakupan = document.getElementById('kkgKelACakupan');
            if (elKelACakupan) data.kkg_kelompok_a.cakupan = elKelACakupan.value.trim();

            const elKelAJadwal = document.getElementById('kkgKelAJadwal');
            if (elKelAJadwal) data.kkg_kelompok_a.jadwal = elKelAJadwal.value.trim();

            const elKelAProg = document.getElementById('kkgKelAPrograms');
            if (elKelAProg) {
                data.kkg_kelompok_a.uraian_kerja = elKelAProg.value.split('\\n').map(l => l.trim()).filter(Boolean);
            }

            const elKelBJudul = document.getElementById('kkgKelBJudul');
            if (elKelBJudul) data.kkg_kelompok_b.nama_kelompok = elKelBJudul.value.trim();

            const elKelBCakupan = document.getElementById('kkgKelBCakupan');
            if (elKelBCakupan) data.kkg_kelompok_b.cakupan = elKelBCakupan.value.trim();

            const elKelBJadwal = document.getElementById('kkgKelBJadwal');
            if (elKelBJadwal) data.kkg_kelompok_b.jadwal = elKelBJadwal.value.trim();

            const elKelBProg = document.getElementById('kkgKelBPrograms');
            if (elKelBProg) {
                data.kkg_kelompok_b.uraian_kerja = elKelBProg.value.split('\\n').map(l => l.trim()).filter(Boolean);
            }

            saveKKGData(data);
            showSyncToast('🎉 Profil Gugus, Sekretariat, Program K3S & KKG Kelompok A/B berhasil disimpan!');
            alert('✅ Profil Gugus 1, Sekretariat, dan Uraian Program K3S/KKG berhasil disimpan!');
        });
    }

    if (btnResetProfil) {
        btnResetProfil.addEventListener('click', function() {
            if (confirm('Pulihkan profil Gugus 1, Sekretariat, dan uraian kerja K3S / KKG ke setelan default?')) {
                const currentData = getKKGData();
                currentData.gusek_info = JSON.parse(JSON.stringify(defaultKKGData.gusek_info));
                currentData.k3s = JSON.parse(JSON.stringify(defaultKKGData.k3s));
                currentData.kkg_kelompok_a = JSON.parse(JSON.stringify(defaultKKGData.kkg_kelompok_a));
                currentData.kkg_kelompok_b = JSON.parse(JSON.stringify(defaultKKGData.kkg_kelompok_b));
                saveKKGData(currentData);
                populateKKGProfilFields();
                showSyncToast('Profil & Program Gugus dipulihkan ke default.');
                alert('Profil & Program Gugus berhasil dipulihkan.');
            }
        });
    }
"""

# Insert kkg_profil_logic right before renderTable() at the end of initKKGManager()
old_render_kkg = "    renderTable();\n}"
new_render_kkg = kkg_profil_logic + "\n    renderTable();\n}"
admin_js = admin_js.replace(old_render_kkg, new_render_kkg, 1)

# 6. Append SOP Manager implementation at the end of admin_js
sop_manager_implementation = """
/* -------------------------------------------------------------------
   14. KELOLA STANDAR OPERASIONAL PROSEDUR (SOP) & KEDISIPLINAN SEKOLAH
   Tata Tertib Guru & Siswa, Piket Harian Guru, Seragam 5 Siklus Mingguan,
   serta Pembina Pramuka Siaga & Penggalang (Terhubung ke Dewan Guru)
   ------------------------------------------------------------------- */
const defaultSOPData = {
    "tata_tertib_guru": [
        "Jam 07.00 WIT – Seluruh dewan guru sudah hadir di sekolah sebelum aktivitas pembelajaran dimulai.",
        "Budaya 5S – Menerapkan pembiasaan Senyum, Salam, Sapa, Sopan, dan Santun kepada seluruh warga sekolah dan tamu.",
        "Persiapan Upacara – Pukul 07.00 WIT persiapan barisan upacara dan tepat pukul 07.15 WIT upacara bendera dimulai secara khidmat.",
        "Pembina Upacara Bergilir – Guru secara terjadwal dan bergilir bertindak sebagai Pembina Upacara sesuai jadwal yang ditetapkan.",
        "Keteladanan Karakter – Guru senantiasa meneladani peserta didik untuk selalu menjaga ketertiban, sopan santun, dan kebersihan lingkungan sekolah.",
        "Disiplin Waktu – Disiplin waktu datang dan pulang sesuai ketentuan kedinasan yang berlaku.",
        "Kewajiban Seragam – Wajib memakai seragam dinas harian sesuai ketentuan jadwal mingguan (siklus 5 minggu) yang telah ditetapkan.",
        "Ekstrakurikuler Wajib – Wajib mendampingi dan mengikuti kegiatan ekstrakurikuler Gerakan Pramuka.",
        "Pemberitahuan Izin – Guru yang berhalangan hadir atau sakit wajib memberikan surat pemberitahuan / izin resmi kepada Kepala Sekolah.",
        "Presensi Akhir – Menandatangani daftar hadir resmi pada akhir kegiatan pembelajaran setiap hari kerja.",
        "Tanggung Jawab Guru Piket – Guru piket wajib mengisi buku piket harian, menyambut siswa di gerbang, dan bertanggung jawab penuh menjaga ketertiban selama jam pembelajaran berlangsung."
    ],
    "tata_tertib_siswa": [
        "Kehadiran Tepat Waktu – Peserta didik datang pukul 07.00 WIT sebelum pembelajaran berlangsung.",
        "Membudayakan 5S – Menerapkan salam, senyum, sapa, sopan, dan santun kepada guru, tenaga kependidikan, serta sesama teman.",
        "Kewajiban Upacara Bendera – Wajib mengikuti upacara bendera setiap hari Senin dengan mengenakan seragam lengkap (topi dan dasi).",
        "Budaya Lingkungan Bersih – Membudayakan lingkungan bersih, aktif memungut sampah, dan membuangnya pada tempat sampah yang tersedia.",
        "Tugas Piket Kelas – Peserta didik yang bertugas piket wajib hadir lebih awal untuk menyapu, membersihkan ruang kelas, lingkungan kelas, dan fasilitas MCK.",
        "Waktu Pembelajaran – Peserta didik masuk kelas mulai jam 07.30 WIT dan berakhir hingga jam 14.00 WIT sesuai jadwal rombel.",
        "Adab Berdoa – Membudayakan berdoa bersama dengan khusyuk sebelum memulai dan sesudah mengakhiri pembelajaran.",
        "Berbaris Tertib – Sebelum memasuki ruang kelas, peserta didik berbaris rapi di depan kelas dipimpin ketua kelas dan bersalaman dengan guru.",
        "Keamanan Lingkungan – Dilarang keluar pagar atau meninggalkan lingkungan sekolah tanpa izin guru piket atau wali kelas selama jam sekolah.",
        "Menjaga Fasilitas Sekolah – Menjaga ketertiban, kebersihan, serta merawat sarana dan prasarana sekolah dengan rasa tanggung jawab."
    ],
    "piket_guru": {
        "Senin": ["Elias Tabuni, S.Pd", "Flavianus Rainaldus, S.Ag"],
        "Selasa": ["Esther Tina Maria Panjaitan, S.Pd", "Cicik Mursidah, S.Pd"],
        "Rabu": ["Warno, S.Pd.SD", "Yuli Syetia Sari, S.Pd"],
        "Kamis": ["Rini Handayani, S.Pd", "Ferdinand, S.Pd"],
        "Jumat": ["Zainal Habiib Al Arif, S.Pd", "Umi Wildana Zulfa"]
    },
    "seragam_guru": [
        { "siklus": "Minggu Ke-1", "senin_selasa": "Seragam Keki (Khaki)", "rabu": "Putih - Hitam", "kamis": "Batik Papua Warna Hijau", "jumat": "Kaos Merah Maroon" },
        { "siklus": "Minggu Ke-2", "senin_selasa": "Seragam Keki (Khaki)", "rabu": "Putih - Hitam", "kamis": "Batik Papua Merah", "jumat": "Kaos Hitam" },
        { "siklus": "Minggu Ke-3", "senin_selasa": "Seragam Keki (Khaki)", "rabu": "Putih - Hitam", "kamis": "Batik Papua Cenderawasih", "jumat": "Kaos Biru Lengan Panjang" },
        { "siklus": "Minggu Ke-4", "senin_selasa": "Seragam Keki (Khaki)", "rabu": "Putih - Hitam", "kamis": "Batik Jawa Lengan Panjang", "jumat": "Kaos Merah Lengan Panjang" },
        { "siklus": "Minggu Ke-5", "senin_selasa": "Seragam Keki (Khaki)", "rabu": "Putih - Hitam", "kamis": "Batik Papua Bebas", "jumat": "Kaos Kuning Lengan Panjang" }
    ],
    "pramuka_pembina": {
        "jadwal": "Dilaksanakan 2 (dua) kali setiap bulan pada hari Jumat pukul 15.00 – 17.00 WIT di lingkungan sekolah.",
        "siaga": [
            "Yuli Syetia Sari, S.Pd",
            "Ferdinand, S.Pd",
            "Rita Paulina Wabiser, S.Pd",
            "Elias Tabuni, S.Pd",
            "Esther Tina Maria Panjaitan, S.Pd",
            "Flavianus Rainaldus, S.Ag"
        ],
        "penggalang": [
            "Warno, S.Pd.SD",
            "Cicik Mursidah, S.Pd",
            "Rini Handayani, S.Pd",
            "Zainal Habiib Al Arif, S.Pd",
            "Umi Wildana Zulfa"
        ]
    }
};

function getSOPData() {
    try {
        const raw = localStorage.getItem('sdn_sop_data');
        if (raw) return JSON.parse(raw);
    } catch (e) {}
    if (window.SDN_DATABASE && window.SDN_DATABASE.sop_data) {
        return window.SDN_DATABASE.sop_data;
    }
    return defaultSOPData;
}

function saveSOPData(data) {
    localStorage.setItem('sdn_sop_data', JSON.stringify(data));
    if (window.SDN_DATABASE) window.SDN_DATABASE.sop_data = data;
    syncToServer('sop_data', data);
}

function populateSOPTeacherDropdowns() {
    const teachers = (typeof getGuruData === 'function') ? getGuruData() : [];
    const teacherNames = teachers.map(g => (typeof g === 'object' && g.nama) ? g.nama : g).filter(Boolean);

    const piketSelectIds = [
        'sopPiket_senin_1', 'sopPiket_senin_2',
        'sopPiket_selasa_1', 'sopPiket_selasa_2',
        'sopPiket_rabu_1', 'sopPiket_rabu_2',
        'sopPiket_kamis_1', 'sopPiket_kamis_2',
        'sopPiket_jumat_1', 'sopPiket_jumat_2'
    ];

    piketSelectIds.forEach(id => {
        const sel = document.getElementById(id);
        if (!sel) return;
        const currentVal = sel.value;
        sel.innerHTML = '<option value="">-- Pilih Guru Piket --</option>';
        teacherNames.forEach(name => {
            const opt = document.createElement('option');
            opt.value = name;
            opt.textContent = name;
            sel.appendChild(opt);
        });
        if (currentVal) sel.value = currentVal;
    });

    const siagaAddSel = document.getElementById('sopPramukaSiagaAddGuru');
    if (siagaAddSel) {
        siagaAddSel.innerHTML = '<option value="">➕ Tambah Guru dari Database Dewan Guru...</option>';
        teacherNames.forEach(name => {
            const opt = document.createElement('option');
            opt.value = name;
            opt.textContent = name;
            siagaAddSel.appendChild(opt);
        });
    }

    const penggalangAddSel = document.getElementById('sopPramukaPenggalangAddGuru');
    if (penggalangAddSel) {
        penggalangAddSel.innerHTML = '<option value="">➕ Tambah Guru dari Database Dewan Guru...</option>';
        teacherNames.forEach(name => {
            const opt = document.createElement('option');
            opt.value = name;
            opt.textContent = name;
            penggalangAddSel.appendChild(opt);
        });
    }
}

function syncGuruWithSOP(oldNama, newNama) {
    if (!oldNama || !newNama || oldNama === newNama) return;
    const sopData = getSOPData();
    let changed = false;

    if (sopData.piket_guru && typeof sopData.piket_guru === 'object') {
        Object.keys(sopData.piket_guru).forEach(hari => {
            if (Array.isArray(sopData.piket_guru[hari])) {
                sopData.piket_guru[hari] = sopData.piket_guru[hari].map(t => {
                    if (t === oldNama || t.includes(oldNama)) {
                        changed = true;
                        return newNama;
                    }
                    return t;
                });
            }
        });
    }

    if (sopData.pramuka_pembina) {
        if (Array.isArray(sopData.pramuka_pembina.siaga)) {
            sopData.pramuka_pembina.siaga = sopData.pramuka_pembina.siaga.map(t => {
                if (t === oldNama || t.includes(oldNama)) {
                    changed = true;
                    return newNama;
                }
                return t;
            });
        }
        if (Array.isArray(sopData.pramuka_pembina.penggalang)) {
            sopData.pramuka_pembina.penggalang = sopData.pramuka_pembina.penggalang.map(t => {
                if (t === oldNama || t.includes(oldNama)) {
                    changed = true;
                    return newNama;
                }
                return t;
            });
        }
    }

    if (changed) {
        saveSOPData(sopData);
        if (typeof initSOPManager === 'function') initSOPManager();
    }
}

function initSOPManager() {
    populateSOPTeacherDropdowns();

    const sopData = getSOPData();

    // 1. TATA TERTIB
    const elTatibGuru = document.getElementById('sopTatibGuruInput');
    const elTatibSiswa = document.getElementById('sopTatibSiswaInput');
    const btnSimpanTatib = document.getElementById('btnSimpanSOPTatib');
    const btnResetTatib = document.getElementById('btnResetSOPTatib');

    if (elTatibGuru) elTatibGuru.value = (sopData.tata_tertib_guru || []).join('\\n');
    if (elTatibSiswa) elTatibSiswa.value = (sopData.tata_tertib_siswa || []).join('\\n');

    if (btnSimpanTatib) {
        btnSimpanTatib.onclick = function() {
            const data = getSOPData();
            if (elTatibGuru) data.tata_tertib_guru = elTatibGuru.value.split('\\n').map(l => l.trim()).filter(Boolean);
            if (elTatibSiswa) data.tata_tertib_siswa = elTatibSiswa.value.split('\\n').map(l => l.trim()).filter(Boolean);
            saveSOPData(data);
            showSyncToast('🎉 Poin Tata Tertib Guru & Siswa berhasil disimpan!');
            alert('✅ Tata Tertib Guru & Siswa berhasil disimpan!');
        };
    }

    if (btnResetTatib) {
        btnResetTatib.onclick = function() {
            if (confirm('Pulihkan poin-poin tata tertib guru & siswa ke setelan standar?')) {
                const data = getSOPData();
                data.tata_tertib_guru = JSON.parse(JSON.stringify(defaultSOPData.tata_tertib_guru));
                data.tata_tertib_siswa = JSON.parse(JSON.stringify(defaultSOPData.tata_tertib_siswa));
                saveSOPData(data);
                if (elTatibGuru) elTatibGuru.value = data.tata_tertib_guru.join('\\n');
                if (elTatibSiswa) elTatibSiswa.value = data.tata_tertib_siswa.join('\\n');
                showSyncToast('Tata Tertib dipulihkan ke default.');
                alert('Tata Tertib dipulihkan ke default.');
            }
        };
    }

    // 2. PIKET GURU
    const hariKeys = ['senin', 'selasa', 'rabu', 'kamis', 'jumat'];
    const hariDisplay = { senin: 'Senin', selasa: 'Selasa', rabu: 'Rabu', kamis: 'Kamis', jumat: 'Jumat' };
    const btnSimpanPiket = document.getElementById('btnSimpanSOPPiket');
    const btnResetPiket = document.getElementById('btnResetSOPPiket');

    function populatePiketDropdownsFromData() {
        const data = getSOPData();
        const piket = data.piket_guru || {};

        hariKeys.forEach(h => {
            const hariCap = hariDisplay[h];
            const pair = Array.isArray(piket[hariCap]) ? piket[hariCap] : [];
            const sel1 = document.getElementById(`sopPiket_${h}_1`);
            const sel2 = document.getElementById(`sopPiket_${h}_2`);

            if (sel1 && pair[0]) {
                let found = Array.from(sel1.options).some(o => o.value === pair[0]);
                if (!found && pair[0]) {
                    const opt = document.createElement('option');
                    opt.value = pair[0];
                    opt.textContent = pair[0];
                    sel1.appendChild(opt);
                }
                sel1.value = pair[0];
            }

            if (sel2 && pair[1]) {
                let found = Array.from(sel2.options).some(o => o.value === pair[1]);
                if (!found && pair[1]) {
                    const opt = document.createElement('option');
                    opt.value = pair[1];
                    opt.textContent = pair[1];
                    sel2.appendChild(opt);
                }
                sel2.value = pair[1];
            }
        });
    }

    populatePiketDropdownsFromData();

    if (btnSimpanPiket) {
        btnSimpanPiket.onclick = function() {
            const data = getSOPData();
            if (!data.piket_guru) data.piket_guru = {};

            hariKeys.forEach(h => {
                const hariCap = hariDisplay[h];
                const sel1 = document.getElementById(`sopPiket_${h}_1`);
                const sel2 = document.getElementById(`sopPiket_${h}_2`);
                const t1 = sel1 ? sel1.value.trim() : '';
                const t2 = sel2 ? sel2.value.trim() : '';
                data.piket_guru[hariCap] = [t1, t2].filter(Boolean);
            });

            saveSOPData(data);
            showSyncToast('🎉 Jadwal Piket Harian Guru berhasil disimpan!');
            alert('✅ Jadwal Piket Harian Guru berhasil disimpan!');
        };
    }

    if (btnResetPiket) {
        btnResetPiket.onclick = function() {
            if (confirm('Pulihkan jadwal piket harian guru ke setelan standar?')) {
                const data = getSOPData();
                data.piket_guru = JSON.parse(JSON.stringify(defaultSOPData.piket_guru));
                saveSOPData(data);
                populatePiketDropdownsFromData();
                showSyncToast('Jadwal piket guru dipulihkan.');
                alert('Jadwal piket harian guru dipulihkan.');
            }
        };
    }

    // 3. SERAGAM GURU (5 SIKLUS MINGGUAN)
    const btnSimpanSeragam = document.getElementById('btnSimpanSOPSeragam');
    const btnResetSeragam = document.getElementById('btnResetSOPSeragam');

    function populateSeragamInputsFromData() {
        const data = getSOPData();
        const seragamList = Array.isArray(data.seragam_guru) ? data.seragam_guru : [];

        for (let m = 1; m <= 5; m++) {
            const item = seragamList[m - 1] || {};
            const elSenin = document.getElementById(`sopSeragam_m${m}_senin`);
            const elRabu = document.getElementById(`sopSeragam_m${m}_rabu`);
            const elKamis = document.getElementById(`sopSeragam_m${m}_kamis`);
            const elJumat = document.getElementById(`sopSeragam_m${m}_jumat`);

            if (elSenin) elSenin.value = item.senin_selasa || '';
            if (elRabu) elRabu.value = item.rabu || '';
            if (elKamis) elKamis.value = item.kamis || '';
            if (elJumat) elJumat.value = item.jumat || '';
        }
    }

    populateSeragamInputsFromData();

    if (btnSimpanSeragam) {
        btnSimpanSeragam.onclick = function() {
            const data = getSOPData();
            const newSeragamList = [];

            for (let m = 1; m <= 5; m++) {
                const elSenin = document.getElementById(`sopSeragam_m${m}_senin`);
                const elRabu = document.getElementById(`sopSeragam_m${m}_rabu`);
                const elKamis = document.getElementById(`sopSeragam_m${m}_kamis`);
                const elJumat = document.getElementById(`sopSeragam_m${m}_jumat`);

                newSeragamList.push({
                    siklus: `Minggu Ke-${m}`,
                    senin_selasa: elSenin ? elSenin.value.trim() : '',
                    rabu: elRabu ? elRabu.value.trim() : '',
                    kamis: elKamis ? elKamis.value.trim() : '',
                    jumat: elJumat ? elJumat.value.trim() : ''
                });
            }

            data.seragam_guru = newSeragamList;
            saveSOPData(data);
            showSyncToast('🎉 Jadwal Seragam Guru (5 Siklus Mingguan) berhasil disimpan!');
            alert('✅ Jadwal Pemakaian Seragam Guru berhasil disimpan!');
        };
    }

    if (btnResetSeragam) {
        btnResetSeragam.onclick = function() {
            if (confirm('Pulihkan jadwal seragam guru 5 minggu ke setelan standar?')) {
                const data = getSOPData();
                data.seragam_guru = JSON.parse(JSON.stringify(defaultSOPData.seragam_guru));
                saveSOPData(data);
                populateSeragamInputsFromData();
                showSyncToast('Jadwal seragam dipulihkan.');
                alert('Jadwal pemakaian seragam dipulihkan.');
            }
        };
    }

    // 4. PEMBINA PRAMUKA (SIAGA & PENGGALANG)
    const elPramukaJadwal = document.getElementById('sopPramukaJadwalInput');
    const elSiagaInput = document.getElementById('sopPramukaSiagaInput');
    const elPenggalangInput = document.getElementById('sopPramukaPenggalangInput');
    const siagaAddSel = document.getElementById('sopPramukaSiagaAddGuru');
    const penggalangAddSel = document.getElementById('sopPramukaPenggalangAddGuru');
    const btnSimpanPramuka = document.getElementById('btnSimpanSOPPramuka');
    const btnResetPramuka = document.getElementById('btnResetSOPPramuka');

    function populatePramukaFieldsFromData() {
        const data = getSOPData();
        const p = data.pramuka_pembina || {};

        if (elPramukaJadwal) elPramukaJadwal.value = p.jadwal || '';
        if (elSiagaInput) elSiagaInput.value = (p.siaga || []).join('\\n');
        if (elPenggalangInput) elPenggalangInput.value = (p.penggalang || []).join('\\n');
    }

    populatePramukaFieldsFromData();

    if (siagaAddSel && elSiagaInput) {
        siagaAddSel.onchange = function() {
            const val = this.value;
            if (!val) return;
            const currentLines = elSiagaInput.value.split('\\n').map(l => l.trim()).filter(Boolean);
            if (!currentLines.includes(val)) {
                currentLines.push(val);
                elSiagaInput.value = currentLines.join('\\n');
            }
            this.value = '';
        };
    }

    if (penggalangAddSel && elPenggalangInput) {
        penggalangAddSel.onchange = function() {
            const val = this.value;
            if (!val) return;
            const currentLines = elPenggalangInput.value.split('\\n').map(l => l.trim()).filter(Boolean);
            if (!currentLines.includes(val)) {
                currentLines.push(val);
                elPenggalangInput.value = currentLines.join('\\n');
            }
            this.value = '';
        };
    }

    if (btnSimpanPramuka) {
        btnSimpanPramuka.onclick = function() {
            const data = getSOPData();
            if (!data.pramuka_pembina) data.pramuka_pembina = {};

            if (elPramukaJadwal) data.pramuka_pembina.jadwal = elPramukaJadwal.value.trim();
            if (elSiagaInput) data.pramuka_pembina.siaga = elSiagaInput.value.split('\\n').map(l => l.trim()).filter(Boolean);
            if (elPenggalangInput) data.pramuka_pembina.penggalang = elPenggalangInput.value.split('\\n').map(l => l.trim()).filter(Boolean);

            saveSOPData(data);
            showSyncToast('🎉 Tim Pembina Pramuka Siaga & Penggalang berhasil disimpan!');
            alert('✅ Tim Pembina Gerakan Pramuka berhasil disimpan!');
        };
    }

    if (btnResetPramuka) {
        btnResetPramuka.onclick = function() {
            if (confirm('Pulihkan data tim pembina pramuka ke setelan standar?')) {
                const data = getSOPData();
                data.pramuka_pembina = JSON.parse(JSON.stringify(defaultSOPData.pramuka_pembina));
                saveSOPData(data);
                populatePramukaFieldsFromData();
                showSyncToast('Tim pembina pramuka dipulihkan.');
                alert('Tim pembina pramuka dipulihkan.');
            }
        };
    }
}
"""

admin_js += "\n" + sop_manager_implementation

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(admin_js)

print("js/admin.js updated successfully with SOP Manager & KKG Profil Manager!")
