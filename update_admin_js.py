with open('js/admin.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add safeAdminSet at top level if not already defined at the top
safe_admin_set_code = """
// ===================================================================
// GLOBAL SAFE STORAGE HELPER (SDN INPRES ARSO VIII)
// ===================================================================
window.safeAdminSet = function(k, v) {
    if (!v) return;
    try {
        localStorage.setItem(k, typeof v === 'string' ? v : JSON.stringify(v));
    } catch (e) {}
};
function safeAdminSet(k, v) {
    return window.safeAdminSet(k, v);
}
"""

if "window.safeAdminSet =" not in code:
    code = safe_admin_set_code + "\n" + code

# 2. Add 'profil': 'tab-profil' to hashToTab in initAdminTabs
code = code.replace(
    "'sambutan': 'tab-sambutan',",
    "'sambutan': 'tab-sambutan',\n            'profil': 'tab-profil',"
)

# 3. Add populateProfilForm in switchAdminTab
code = code.replace(
    "    if (targetPanel && window.innerWidth <= 900) {\n        targetPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });\n    }\n};",
    """    if (targetPanel && window.innerWidth <= 900) {
        targetPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Panggil populate form saat tab dibuka
    if (tabId === 'tab-profil' && typeof window.populateProfilForm === 'function') {
        window.populateProfilForm();
    } else if (tabId === 'tab-kontak' && typeof window.populateKontakForm === 'function') {
        window.populateKontakForm();
    }
};"""
)

# 4. Replace saveProfilData and populateProfilForm with robust versions
old_profil_marker = "/* -------------------------------------------------------------------\n   15. PENGELOLA PROFIL SEKOLAH (Visi, Misi, Tujuan, Sejarah, Identitas)"
old_kontak_marker = "/* -------------------------------------------------------------------\n   16. PENGELOLA KONTAK RESMI & KOTAK MASUK PESAN TAMU"

p_prof = code.find(old_profil_marker)
p_kontak = code.find(old_kontak_marker)

if p_prof != -1 and p_kontak != -1:
    new_profil_section = """/* -------------------------------------------------------------------
   15. PENGELOLA PROFIL SEKOLAH (Visi, Misi, Tujuan, Sejarah, Identitas)
   ------------------------------------------------------------------- */
window.getProfilData = function() {
    if (window.SDN_DATABASE && window.SDN_DATABASE.profil && typeof window.SDN_DATABASE.profil === 'object') {
        return window.SDN_DATABASE.profil;
    }
    try {
        const raw = localStorage.getItem('sdn_profil_data');
        if (raw) return JSON.parse(raw);
    } catch (e) {}
    return {
        visi: "MEWUJUDKAN PESERTA DIDIK YANG BERPRESTASI DALAM BIDANG KEIMANAN (BERTAQWA), BERKARAKTER, MAMPU BERKOLABORASI, SEHAT JASMANI, UNGGUL DALAM ILMU PENGETAHUAN DAN TEKNOLOGI (IPTEK), SERTA MENCINTAI LINGKUNGAN.",
        misi: [
            "Mengembangkan potensi peserta didik agar bertaqwa kepada Tuhan Yang Maha Esa.",
            "Menyelenggarakan pendidikan yang demokratis, menjunjung tinggi hak asasi, nilai keagamaan, dan nilai kultural bangsa.",
            "Menyelenggarakan pendidikan yang beraspirasi dari seluruh warga sekolah dan masyarakat sekitar.",
            "Melaksanakan evaluasi pendidikan dalam penjaminan mutu yang bertanggung jawab dan transparan.",
            "Menjalin hubungan erat dengan komite sekolah, tokoh masyarakat, dan berperan aktif dalam pelaksanaan pendidikan."
        ],
        tujuan: [
            "Siswa beriman dan berakhlak mulia kepada Tuhan Yang Maha Esa.",
            "Siswa senantiasa sehat jasmani dan rohani.",
            "Siswa memiliki dasar-dasar pengetahuan dan ketrampilan untuk melanjutkan pendidikan ke jenjang yang lebih tinggi (SMP).",
            "Siswa mengenal dan mencintai bangsa, masyarakat, dan ragam budaya Nusantara, khususnya budaya lokal Papua.",
            "Siswa kreatif, terampil, bekerja keras, serta mampu mengembangkan diri secara terus-menerus."
        ],
        sejarah: "SD Negeri Inpres Arso VIII didirikan sebagai bagian dari program pemerataan akses pendidikan nasional di kawasan pemukiman transmigrasi dan masyarakat lokal Arso, Kabupaten Keerom. Beralamat di Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, sekolah ini menjadi sentra pendidikan bagi warga sekitar yang majemuk.\\n\\nDengan luas area mencapai 10.000 m² milik pemerintah, sekolah ini memiliki potensi lingkungan yang sangat luas, sejuk, dan asri. Meskipun kondisi sarana prasarana fisik bangunan seperti ruang kelas, ruang TIK, dan ruang kantor saat ini berstatus rusak sedang dan masih memerlukan perhatian serta renovasi berkala dari pemerintah daerah, semangat 12 tenaga pendidik dan 157 siswa tetap menyala tinggi.\\n\\nKehadiran jaringan satelit berkecepatan tinggi Starlink menjadi lompatan bersejarah bagi SDN Inpres Arso VIII, membuktikan bahwa keterbatasan geografis bukan halangan bagi anak-anak di tanah Keerom Papua untuk bersaing menguasai ilmu pengetahuan dan teknologi modern.",
        identitas: {
            npsn: "60301140",
            nss: "101250302008",
            akreditasi: "A (Unggul - BAN-SM 2023)",
            status_kepemilikan: "Pemerintah Daerah",
            sk_pendirian: "01/SK/PDK/1984",
            sk_izin_operasional: "0005/OPS.SD/DPM-PTSP/VII/2026",
            luas_tanah: "10.000 m²",
            daya_listrik: "2.200 Watt",
            alamat: "Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua 99473"
        }
    };
};
function getProfilData() { return window.getProfilData(); }

window.populateProfilForm = function() {
    const data = window.getProfilData();
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
    if (akredEl) akredEl.value = id.akreditasi || 'A (Unggul - BAN-SM 2023)';
    if (kepemilikanEl) kepemilikanEl.value = id.status_kepemilikan || 'Pemerintah Daerah';
    if (skPendirianEl) skPendirianEl.value = id.sk_pendirian || '01/SK/PDK/1984';
    if (skOperasionalEl) skOperasionalEl.value = id.sk_izin_operasional || '0005/OPS.SD/DPM-PTSP/VII/2026';
    if (luasEl) luasEl.value = id.luas_tanah || '10.000 m²';
    if (dayaEl) dayaEl.value = id.daya_listrik || '2.200 Watt';
    if (alamatEl) alamatEl.value = id.alamat || 'Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua 99473';
};
function populateProfilForm() { return window.populateProfilForm(); }

window.saveProfilData = function() {
    const data = {
        visi: document.getElementById('profilVisiInput')?.value.trim() || '',
        misi: (document.getElementById('profilMisiInput')?.value || '').split('\\n').map(m => m.trim()).filter(m => m.length > 0),
        tujuan: (document.getElementById('profilTujuanInput')?.value || '').split('\\n').map(m => m.trim()).filter(m => m.length > 0),
        sejarah: document.getElementById('profilSejarahInput')?.value.trim() || '',
        identitas: {
            npsn: document.getElementById('identitasNPSN')?.value.trim() || '60301140',
            nss: document.getElementById('identitasNSS')?.value.trim() || '101250302008',
            akreditasi: document.getElementById('identitasAkreditasi')?.value.trim() || 'A (Unggul - BAN-SM 2023)',
            status_kepemilikan: document.getElementById('identitasKepemilikan')?.value.trim() || 'Pemerintah Daerah',
            sk_pendirian: document.getElementById('identitasSKPendirian')?.value.trim() || '01/SK/PDK/1984',
            sk_izin_operasional: document.getElementById('identitasSKOperasional')?.value.trim() || '0005/OPS.SD/DPM-PTSP/VII/2026',
            luas_tanah: document.getElementById('identitasLuasTanah')?.value.trim() || '10.000 m²',
            daya_listrik: document.getElementById('identitasDayaListrik')?.value.trim() || '2.200 Watt',
            alamat: document.getElementById('identitasAlamat')?.value.trim() || 'Jalan Sulawesi, Kampung Dukwia, Distrik Arso Barat, Kabupaten Keerom, Papua 99473'
        }
    };

    if (window.SDN_DATABASE) window.SDN_DATABASE.profil = data;
    safeAdminSet('sdn_profil_data', data);
    syncToServer('profil', data);
    try {
        logAdminActivity('Pembaruan Profil Sekolah', 'Memperbarui Visi, Misi, Tujuan, Sejarah, dan Data Pokok Legalitas');
    } catch(e) {}
    showSyncToast('🎉 Profil Sekolah berhasil diperbarui dan aktif di internet!');
    alert('✅ Profil Sekolah berhasil disimpan dan langsung aktif di website publik!');
};
function saveProfilData() { return window.saveProfilData(); }

"""
    code = code[:p_prof] + new_profil_section + code[p_kontak:]
    print("Replaced profil section successfully!")

# 5. Remove multi-user code from end of js/admin.js (lines after renderPesanKontakTable)
multi_user_comment = "/* -------------------------------------------------------------------\n   18. KELOLA PENGGUNA & HAK AKSES BERJENJANG (MULTI-USER ROLE)"
p_mu = code.find(multi_user_comment)
if p_mu != -1:
    clean_tail = """
// INJEKSI PADA REFRESH ADMIN MANAGERS
const _prevRefresh = window.refreshAdminManagers;
window.refreshAdminManagers = function() {
    if (typeof _prevRefresh === 'function') {
        try { _prevRefresh(); } catch (e) {}
    }
    try { populateProfilForm(); } catch (e) {}
    try { populateKontakForm(); } catch (e) {}
    try { renderActivityLogs(); } catch (e) {}
};

// INITIALIZATION DI AKHIR DOM READY
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        if (typeof populateProfilForm === 'function') populateProfilForm();
        if (typeof populateKontakForm === 'function') populateKontakForm();
        if (typeof renderActivityLogs === 'function') renderActivityLogs();
    }, 400);
});
"""
    code = code[:p_mu] + clean_tail
    print("Multi-user functions removed cleanly from js/admin.js!")

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("Finished updating js/admin.js!")
