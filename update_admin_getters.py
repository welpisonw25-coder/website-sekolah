# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. getSambutanData
old_sambutan = """function getSambutanData() {
    const d = localStorage.getItem('sdn_sambutan_data');
    if (d) {
        try {
            const p = JSON.parse(d);
            if (p && p.nama) return p;
        } catch (e) {}
    }
    const fallback = (window.SDN_DATABASE && window.SDN_DATABASE.sambutan) ? window.SDN_DATABASE.sambutan : defaultSambutan;
    return fallback;
}"""

new_sambutan = """function getSambutanData() {
    if (window.SDN_DATABASE && window.SDN_DATABASE.sambutan && typeof window.SDN_DATABASE.sambutan === 'object' && (window.SDN_DATABASE.sambutan.nama || window.SDN_DATABASE.sambutan.isi)) {
        return window.SDN_DATABASE.sambutan;
    }
    const d = localStorage.getItem('sdn_sambutan_data');
    if (d) {
        try {
            const p = JSON.parse(d);
            if (p && p.nama) return p;
        } catch (e) {}
    }
    return defaultSambutan;
}"""

if old_sambutan in text:
    text = text.replace(old_sambutan, new_sambutan)
    print("Updated getSambutanData")

# 2. getGaleriData
old_galeri = """function getGaleriData() {
    const raw = localStorage.getItem('sdn_galeri_data');
    if (raw && !raw.includes('unsplash')) {
        try {
            const parsed = JSON.parse(raw);
            return Array.isArray(parsed) ? parsed : defaultGaleri;
        } catch (e) {
            return defaultGaleri;
        }
    }
    saveGaleriData(defaultGaleri);
    return defaultGaleri;
}"""

new_galeri = """function getGaleriData() {
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.galeri) && window.SDN_DATABASE.galeri.length > 0) {
        return window.SDN_DATABASE.galeri;
    }
    const raw = localStorage.getItem('sdn_galeri_data');
    if (raw && !raw.includes('unsplash')) {
        try {
            const parsed = JSON.parse(raw);
            return Array.isArray(parsed) ? parsed : defaultGaleri;
        } catch (e) {
            return defaultGaleri;
        }
    }
    return defaultGaleri;
}"""

if old_galeri in text:
    text = text.replace(old_galeri, new_galeri)
    print("Updated getGaleriData")

# 3. getGuruData
old_guru = """function getGuruData() {
    const d = localStorage.getItem('sdn_guru_data');
    if (d) {
        try {
            const parsed = JSON.parse(d);
            if (Array.isArray(parsed) && parsed.length > 0) return parsed;
        } catch (e) {}
    }
    const fallback = (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.guru) && window.SDN_DATABASE.guru.length > 0) ? window.SDN_DATABASE.guru : defaultGuruList;
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
    return defaultGuruList;
}"""

if old_guru in text:
    text = text.replace(old_guru, new_guru)
    print("Updated getGuruData")

# 4. getSiswaData
old_siswa = """function getSiswaData() {
    let d = null;
    try {
        const raw = localStorage.getItem('sdn_siswa_counts') || localStorage.getItem('sdn_siswa_kelas');
        if (raw) d = JSON.parse(raw);
    } catch (e) {}
    if (!d && window.SDN_DATABASE && window.SDN_DATABASE.siswa) {
        d = window.SDN_DATABASE.siswa;
    }
    return d || defaultSiswaData;
}"""

new_siswa = """function getSiswaData() {
    if (window.SDN_DATABASE && window.SDN_DATABASE.siswa && typeof window.SDN_DATABASE.siswa === 'object') {
        return window.SDN_DATABASE.siswa;
    }
    let d = null;
    try {
        const raw = localStorage.getItem('sdn_siswa_counts') || localStorage.getItem('sdn_siswa_kelas');
        if (raw) d = JSON.parse(raw);
    } catch (e) {}
    return d || defaultSiswaData;
}"""

if old_siswa in text:
    text = text.replace(old_siswa, new_siswa)
    print("Updated getSiswaData")

# 5. getSarprasData
old_sarpras = """function getSarprasData() {
    const raw = localStorage.getItem('sdn_sarpras_data');
    return raw ? JSON.parse(raw) : defaultSarprasData;
}"""

new_sarpras = """function getSarprasData() {
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.sarpras) && window.SDN_DATABASE.sarpras.length > 0) {
        return window.SDN_DATABASE.sarpras;
    }
    const raw = localStorage.getItem('sdn_sarpras_data');
    return raw ? JSON.parse(raw) : defaultSarprasData;
}"""

if old_sarpras in text:
    text = text.replace(old_sarpras, new_sarpras)
    print("Updated getSarprasData")

# 6. getKolaborasiData
old_kolaborasi = """function getKolaborasiData() {
    try {
        const raw = localStorage.getItem('sdn_kolaborasi_data');
        if (raw) {
            const parsed = JSON.parse(raw);
            if (Array.isArray(parsed) && parsed.length > 0) return parsed;
        }
    } catch (e) {}
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.kolaborasi) && window.SDN_DATABASE.kolaborasi.length > 0) {
        return window.SDN_DATABASE.kolaborasi;
    }
    return defaultKolaborasiList;
}"""

new_kolaborasi = """function getKolaborasiData() {
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.kolaborasi) && window.SDN_DATABASE.kolaborasi.length > 0) {
        return window.SDN_DATABASE.kolaborasi;
    }
    try {
        const raw = localStorage.getItem('sdn_kolaborasi_data');
        if (raw) {
            const parsed = JSON.parse(raw);
            if (Array.isArray(parsed) && parsed.length > 0) return parsed;
        }
    } catch (e) {}
    return defaultKolaborasiList;
}"""

if old_kolaborasi in text:
    text = text.replace(old_kolaborasi, new_kolaborasi)
    print("Updated getKolaborasiData")

# 7. getKKGData
old_kkg = """function getKKGData() {
    try {
        const raw = localStorage.getItem('sdn_kkg_data');
        if (raw) {
            const parsed = JSON.parse(raw);
            if (parsed && typeof parsed === 'object') return parsed;
        }
    } catch (e) {}
    if (window.SDN_DATABASE && window.SDN_DATABASE.kkg) {
        return window.SDN_DATABASE.kkg;
    }
    return defaultKKGData;
}"""

new_kkg = """function getKKGData() {
    if (window.SDN_DATABASE && window.SDN_DATABASE.kkg && typeof window.SDN_DATABASE.kkg === 'object') {
        return window.SDN_DATABASE.kkg;
    }
    try {
        const raw = localStorage.getItem('sdn_kkg_data');
        if (raw) {
            const parsed = JSON.parse(raw);
            if (parsed && typeof parsed === 'object') return parsed;
        }
    } catch (e) {}
    return defaultKKGData;
}"""

if old_kkg in text:
    text = text.replace(old_kkg, new_kkg)
    print("Updated getKKGData")

# 8. getSOPData
old_sop = """function getSOPData() {
    try {
        const raw = localStorage.getItem('sdn_sop_data');
        if (raw) return JSON.parse(raw);
    } catch (e) {}
    if (window.SDN_DATABASE && window.SDN_DATABASE.sop_data) {
        return window.SDN_DATABASE.sop_data;
    }
    return defaultSOPData;
}"""

new_sop = """function getSOPData() {
    if (window.SDN_DATABASE && window.SDN_DATABASE.sop_data && typeof window.SDN_DATABASE.sop_data === 'object') {
        return window.SDN_DATABASE.sop_data;
    }
    try {
        const raw = localStorage.getItem('sdn_sop_data');
        if (raw) return JSON.parse(raw);
    } catch (e) {}
    return defaultSOPData;
}"""

if old_sop in text:
    text = text.replace(old_sop, new_sop)
    print("Updated getSOPData")

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: All admin getters updated!")
