with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Add syncBaganStrukturOrganisasi function right before loadDynamicTeachers
sync_fn = '''/* -------------------------------------------------------------------
   SINKRONISASI CERDAS BAGAN STRUKTUR ORGANISASI SEKOLAH DENGAN DATA GURU
   Mendukung: 1) Upload Gambar Bagan Baru & 2) Konek Otomatis Susunan Guru
   ------------------------------------------------------------------- */
function syncBaganStrukturOrganisasi(teachers) {
    const customContainer = document.getElementById('baganCustomImageContainer');
    const customImg = document.getElementById('baganCustomImg');
    const svgContainer = document.getElementById('baganSvgContainer');

    // 1. Periksa apakah ada berkas gambar bagan kustom yang diunggah dari Halaman Admin
    let customBagan = '';
    if (window.SDN_DATABASE && window.SDN_DATABASE.bagan_struktur) {
        customBagan = window.SDN_DATABASE.bagan_struktur;
    } else {
        try {
            customBagan = localStorage.getItem('sdn_bagan_struktur') || '';
        } catch (e) {}
    }

    if (customBagan && customBagan.length > 50) {
        if (customContainer) customContainer.style.display = 'block';
        if (customImg) customImg.src = customBagan;
        if (svgContainer) svgContainer.style.display = 'none';
        window._currentActiveBaganSrc = customBagan;
        return;
    } else {
        if (customContainer) customContainer.style.display = 'none';
        if (svgContainer) svgContainer.style.display = 'block';
        window._currentActiveBaganSrc = 'images/bagan-struktur-organisasi.svg';
    }

    // 2. Jika mode Bagan Vektor Interaktif: Sinkronkan nama-nama guru secara otomatis dari database
    if (!Array.isArray(teachers) || teachers.length === 0) return;

    function findTeacher(pattern) {
        const regex = new RegExp(pattern, 'i');
        return teachers.find(t => regex.test(t.jabatan || '')) || null;
    }

    function formatSvgName(fullName, centerX, isSmallBox) {
        if (!fullName) return '';
        const name = fullName.trim();
        const threshold = isSmallBox ? 16 : 19;
        if (name.length > threshold && name.includes(' ')) {
            const spaces = [];
            for (let i = 0; i < name.length; i++) {
                if (name[i] === ' ') spaces.push(i);
            }
            if (spaces.length > 0) {
                const mid = name.length / 2.0;
                let bestIdx = spaces[0];
                let minDiff = Math.abs(bestIdx - mid);
                for (let j = 1; j < spaces.length; j++) {
                    const diff = Math.abs(spaces[j] - mid);
                    if (diff < minDiff) {
                        minDiff = diff;
                        bestIdx = spaces[j];
                    }
                }
                const s1 = name.slice(0, bestIdx);
                const s2 = name.slice(bestIdx + 1);
                return `<tspan x="${centerX}" y="27">${escapeHTML(s1)}</tspan><tspan x="${centerX}" y="43">${escapeHTML(s2)}</tspan>`;
            }
        }
        const y = isSmallBox ? '33' : '32';
        return `<tspan x="${centerX}" y="${y}">${escapeHTML(name)}</tspan>`;
    }

    function updateTextEl(id, teacher, centerX, isSmallBox) {
        const el = document.getElementById(id);
        if (el && teacher && teacher.nama) {
            el.innerHTML = formatSvgName(teacher.nama, centerX, isSmallBox);
        }
    }

    const tKepsek = findTeacher('kepala\\\\s*sekolah') || teachers.find(t => t.id === 1);
    const tKelas1 = findTeacher('kelas\\\\s*1|kelas\\\\s*i\\\\b');
    const tKelas2 = findTeacher('kelas\\\\s*2|kelas\\\\s*ii\\\\b');
    const tKelas3 = findTeacher('kelas\\\\s*3|kelas\\\\s*iii\\\\b');
    const tKelas4 = findTeacher('kelas\\\\s*4|kelas\\\\s*iv\\\\b');
    const tKelas5 = findTeacher('kelas\\\\s*5|kelas\\\\s*v\\\\b');
    const tKelas6 = findTeacher('kelas\\\\s*6|kelas\\\\s*vi\\\\b');
    const tPenjas = findTeacher('penjas|pjok|olahraga');
    const tAgIslam = findTeacher('islam');
    const tAgKristen = findTeacher('protestan|kristen');
    const tAgKatolik = findTeacher('katolik');

    updateTextEl('baganSvgNamaKepsek', tKepsek, 130, false);
    updateTextEl('baganSvgNamaKelas1', tKelas1, 125, false);
    updateTextEl('baganSvgNamaKelas2', tKelas2, 125, false);
    updateTextEl('baganSvgNamaKelas3', tKelas3, 125, false);
    updateTextEl('baganSvgNamaKelas4', tKelas4, 125, false);
    updateTextEl('baganSvgNamaKelas5', tKelas5, 125, false);
    updateTextEl('baganSvgNamaKelas6', tKelas6, 125, false);
    updateTextEl('baganSvgNamaPenjas', tPenjas, 107.5, true);
    updateTextEl('baganSvgNamaAgIslam', tAgIslam, 107.5, true);
    updateTextEl('baganSvgNamaAgKristen', tAgKristen, 107.5, true);
    updateTextEl('baganSvgNamaAgKatolik', tAgKatolik, 107.5, true);
}

'''

target_load = 'function loadDynamicTeachers() {'
if target_load in js:
    js = js.replace(target_load, sync_fn + target_load, 1)
    print("Inserted syncBaganStrukturOrganisasi function successfully!")
else:
    print("target_load not found in js/main.js!")

# 2. Call syncBaganStrukturOrganisasi(teachers) inside loadDynamicTeachers
target_teachers = 'if (!teachers) teachers = defaultMainGuruList;'
replacement_teachers = '''if (!teachers) teachers = defaultMainGuruList;

    // Sinkronkan data guru ke dalam Bagan Struktur Organisasi Sekolah secara otomatis
    syncBaganStrukturOrganisasi(teachers);'''

if target_teachers in js:
    js = js.replace(target_teachers, replacement_teachers, 1)
    print("Added syncBaganStrukturOrganisasi call in loadDynamicTeachers successfully!")
else:
    print("target_teachers not found in js/main.js!")

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated js/main.js successfully!")
