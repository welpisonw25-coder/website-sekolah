# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

# 1. In formBerita: Add beritaStatus
target_b_kat = '<label class="form-label">Kategori Berita *</label>'
replace_b_kat = '''<label class="form-label">Status Publikasi *</label>
                                <select id="beritaStatus" class="form-input" style="font-weight: 700; margin-bottom: 12px;">
                                    <option value="published" selected>🚀 Terbitkan Langsung (Publik)</option>
                                    <option value="draft">💾 Simpan Sebagai Draft</option>
                                </select>
                            </div>
                            <div class="form-group" style="flex: 1;">
                                <label class="form-label">Kategori Berita *</label>'''

if target_b_kat in admin_html:
    admin_html = admin_html.replace(target_b_kat, replace_b_kat, 1)
    print("Patched beritaStatus in admin.html")

# 2. In formPengumuman: Add pengumumanStatus
target_p_kat = '<label class="form-label">Kategori *</label>'
replace_p_kat = '''<label class="form-label">Status Publikasi *</label>
                                <select id="pengumumanStatus" class="form-control" style="font-weight: 700; margin-bottom: 12px;">
                                    <option value="published" selected>🚀 Terbitkan Langsung (Publik)</option>
                                    <option value="draft">💾 Simpan Sebagai Draft</option>
                                </select>
                            </div>
                            <div class="form-group" style="flex: 1;">
                                <label class="form-label">Kategori *</label>'''

if target_p_kat in admin_html:
    admin_html = admin_html.replace(target_p_kat, replace_p_kat, 1)
    print("Patched pengumumanStatus in admin.html")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)

# 3. In js/main.js: Append loadDynamicProfil, loadDynamicKontak, loadDynamicBeranda
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

profil_functions = '''
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

    // Visi
    const visiEl = document.getElementById('profilVisiQuote');
    if (visiEl && profilData.visi) {
        visiEl.textContent = `"${profilData.visi}"`;
    }

    // Misi
    const misiEl = document.getElementById('profilMisiList');
    if (misiEl && Array.isArray(profilData.misi) && profilData.misi.length > 0) {
        misiEl.innerHTML = '';
        profilData.misi.forEach(m => {
            const li = document.createElement('li');
            li.textContent = m;
            misiEl.appendChild(li);
        });
    }

    // Tujuan
    const tujuanEl = document.getElementById('profilTujuanList');
    if (tujuanEl && profilData.tujuan) {
        tujuanEl.innerHTML = '';
        const items = Array.isArray(profilData.tujuan) ? profilData.tujuan : profilData.tujuan.split('\\n').filter(t => t.trim());
        items.forEach(t => {
            const li = document.createElement('li');
            li.textContent = t.trim();
            tujuanEl.appendChild(li);
        });
    }

    // Identitas
    if (profilData.identitas) {
        const id = profilData.identitas;
        const npsn = document.getElementById('profilNPSN');
        if (npsn && id.npsn) npsn.textContent = id.npsn;
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
'''

main_js += profil_functions

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(main_js)

print("Successfully appended loadDynamicProfil, loadDynamicKontak, loadDynamicBeranda to main.js!")
