with open('profil.html', 'r', encoding='utf-8') as f:
    p_html = f.read()

# Add IDs to profil.html
p_html = p_html.replace(
    '<td style="padding: 8px 0; font-weight: 700; color: var(--primary);">10.000 m² (1 Hektar)</td>',
    '<td id="profilLuasTanah" style="padding: 8px 0; font-weight: 700; color: var(--primary);">10.000 m² (1 Hektar)</td>'
)
p_html = p_html.replace(
    '<tr><td style="padding: 8px 0; color: var(--dark-muted);">Daya Listrik</td><td style="padding: 8px 0; font-weight: 600;">2.200 Watt</td></tr>',
    '<tr><td style="padding: 8px 0; color: var(--dark-muted);">Daya Listrik</td><td id="profilDayaListrik" style="padding: 8px 0; font-weight: 600;">2.200 Watt</td></tr>'
)
p_html = p_html.replace(
    '<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 0; color: var(--dark-muted); width: 45%;">Alamat Lengkap</td><td style="padding: 8px 0; font-weight: 600;">Jalan Sulawesi</td></tr>',
    '<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 0; color: var(--dark-muted); width: 45%;">Alamat Lengkap</td><td id="profilAlamat" style="padding: 8px 0; font-weight: 600;">Jalan Sulawesi</td></tr>'
)
p_html = p_html.replace(
    '<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 0; color: var(--dark-muted); width: 45%;">SK Izin Operasional</td><td style="padding: 8px 0; font-weight: 600; font-size: 13px;">0005/OPS.SD/DPM-PTSP/VII/2026</td></tr>',
    '<tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 8px 0; color: var(--dark-muted); width: 45%;">SK Izin Operasional</td><td id="profilSKOperasional" style="padding: 8px 0; font-weight: 600; font-size: 13px;">0005/OPS.SD/DPM-PTSP/VII/2026</td></tr>'
)
p_html = p_html.replace(
    '<div style="color: #475569; font-size: 15px; line-height: 1.8;">',
    '<div id="profilSejarahText" style="color: #475569; font-size: 15px; line-height: 1.8;">'
)

with open('profil.html', 'w', encoding='utf-8') as f:
    f.write(p_html)
print("Updated profil.html with IDs!")

# Now update loadDynamicProfil in js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    m_js = f.read()

old_load_profil_start = "function loadDynamicProfil() {"
p_start = m_js.find(old_load_profil_start)
p_end = m_js.find("function loadDynamicKontak() {", p_start)

if p_start != -1 and p_end != -1:
    new_load_profil = """function loadDynamicProfil() {
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
        const items = Array.isArray(profilData.misi) ? profilData.misi : String(profilData.misi).split('\\n').filter(m => m.trim());
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
        const items = Array.isArray(profilData.tujuan) ? profilData.tujuan : String(profilData.tujuan).split('\\n').filter(t => t.trim());
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
        const paras = String(profilData.sejarah).split(/\\n\\s*\\n/).map(p => p.trim()).filter(p => p.length > 0);
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

"""
    m_js = m_js[:p_start] + new_load_profil + m_js[p_end:]
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(m_js)
    print("Updated loadDynamicProfil in js/main.js successfully!")
else:
    print("Could not find loadDynamicProfil markers in js/main.js")
