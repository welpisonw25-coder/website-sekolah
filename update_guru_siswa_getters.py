# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Update getGuruData
old_guru = """function getGuruData() {
    const d = localStorage.getItem('sdn_guru_data');
    if (d) {
        try {
            const parsed = JSON.parse(d);
            if (Array.isArray(parsed) && parsed.length > 0) return parsed;
        } catch (e) {}
    }
    const fallback = (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.guru) && window.SDN_DATABASE.guru.length > 0) ? window.SDN_DATABASE.guru : defaultGuru;
    localStorage.setItem('sdn_guru_data', JSON.stringify(fallback));
    return fallback;
}"""

new_guru = """function getGuruData() {
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.guru) && window.SDN_DATABASE.guru.length > 0) {
        return window.SDN_DATABASE.guru;
    }
    const d = localStorage.getItem('sdn_guru_data');
    if (d) {
        try {
            const parsed = JSON.parse(d);
            if (Array.isArray(parsed) && parsed.length > 0) return parsed;
        } catch (e) {}
    }
    return defaultGuru;
}"""

if old_guru in text:
    text = text.replace(old_guru, new_guru)
    print("Updated getGuruData!")

# Update getSiswaData
old_siswa = """function getSiswaData() {
    let d = null;
    try {
        const raw = localStorage.getItem('sdn_siswa_counts') || localStorage.getItem('sdn_siswa_kelas');
        if (raw) d = JSON.parse(raw);
    } catch (e) {}

    if (!d && window.SDN_DATABASE && window.SDN_DATABASE.siswa) {
        d = window.SDN_DATABASE.siswa;
    }"""

new_siswa = """function getSiswaData() {
    if (window.SDN_DATABASE && window.SDN_DATABASE.siswa && typeof window.SDN_DATABASE.siswa === 'object') {
        return window.SDN_DATABASE.siswa;
    }
    let d = null;
    try {
        const raw = localStorage.getItem('sdn_siswa_counts') || localStorage.getItem('sdn_siswa_kelas');
        if (raw) d = JSON.parse(raw);
    } catch (e) {}"""

if old_siswa in text:
    text = text.replace(old_siswa, new_siswa)
    print("Updated getSiswaData!")

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(text)
