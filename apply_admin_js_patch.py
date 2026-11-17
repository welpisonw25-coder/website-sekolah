with open('js/admin.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = '''    const penggalangAddSel = document.getElementById('sopPramukaPenggalangAddGuru');
    if (penggalangAddSel) {
        penggalangAddSel.innerHTML = '<option value="">➕ Tambah Guru dari Database Dewan Guru...</option>';
        teacherNames.forEach(name => {
            const opt = document.createElement('option');
            opt.value = name;
            opt.textContent = name;
            penggalangAddSel.appendChild(opt);
        });
    }
}'''

patch = '''    const penggalangAddSel = document.getElementById('sopPramukaPenggalangAddGuru');
    if (penggalangAddSel) {
        penggalangAddSel.innerHTML = '<option value="">➕ Tambah Guru dari Database Dewan Guru...</option>';
        teacherNames.forEach(name => {
            const opt = document.createElement('option');
            opt.value = name;
            opt.textContent = name;
            penggalangAddSel.appendChild(opt);
        });
    }

    // ===================================================================
    // PENGELOLAAN BAGAN STRUKTUR ORGANISASI GURU (UPLOAD GAMBAR & RESET)
    // ===================================================================
    const inputCustomBaganFile = document.getElementById('inputCustomBaganFile');
    const btnUploadCustomBagan = document.getElementById('btnUploadCustomBagan');
    const btnResetBaganToSvg = document.getElementById('btnResetBaganToSvg');
    const btnHapusCustomBagan = document.getElementById('btnHapusCustomBagan');
    const adminBaganPreviewContainer = document.getElementById('adminBaganPreviewContainer');
    const adminBaganPreviewImg = document.getElementById('adminBaganPreviewImg');
    const baganStatusBadge = document.getElementById('baganStatusBadge');

    function refreshAdminBaganState() {
        let customBagan = '';
        if (window.SDN_DATABASE && window.SDN_DATABASE.bagan_struktur) {
            customBagan = window.SDN_DATABASE.bagan_struktur;
        } else {
            try {
                customBagan = localStorage.getItem('sdn_bagan_struktur') || '';
            } catch (e) {}
        }

        if (customBagan && customBagan.length > 50) {
            if (adminBaganPreviewContainer) adminBaganPreviewContainer.style.display = 'block';
            if (adminBaganPreviewImg) adminBaganPreviewImg.src = customBagan;
            if (baganStatusBadge) {
                baganStatusBadge.textContent = '🖼️ Mode: Menggunakan Gambar Bagan Kustom';
                baganStatusBadge.style.background = '#fef3c7';
                baganStatusBadge.style.color = '#92400e';
                baganStatusBadge.style.border = '1px solid #fde68a';
            }
        } else {
            if (adminBaganPreviewContainer) adminBaganPreviewContainer.style.display = 'none';
            if (adminBaganPreviewImg) adminBaganPreviewImg.src = '';
            if (baganStatusBadge) {
                baganStatusBadge.textContent = '✨ Mode: Terkoneksi Otomatis dengan Data Guru';
                baganStatusBadge.style.background = '#e0f2fe';
                baganStatusBadge.style.color = '#0369a1';
                baganStatusBadge.style.border = '1px solid #bae6fd';
            }
        }
    }

    if (btnUploadCustomBagan && inputCustomBaganFile) {
        btnUploadCustomBagan.addEventListener('click', function() {
            const file = inputCustomBaganFile.files[0];
            if (!file) {
                alert('Silakan pilih berkas gambar/foto bagan baru terlebih dahulu.');
                return;
            }

            const reader = new FileReader();
            reader.onload = function(evt) {
                const img = new Image();
                img.onload = function() {
                    const canvas = document.createElement('canvas');
                    let w = img.width;
                    let h = img.height;
                    const maxW = 1600;
                    if (w > maxW) {
                        h = Math.round((h * maxW) / w);
                        w = maxW;
                    }
                    canvas.width = w;
                    canvas.height = h;
                    const ctx = canvas.getContext('2d');
                    ctx.drawImage(img, 0, 0, w, h);
                    const compressedUrl = canvas.toDataURL('image/jpeg', 0.88);

                    try {
                        localStorage.setItem('sdn_bagan_struktur', compressedUrl);
                    } catch (e) {
                        console.warn('Gagal simpan ke localStorage:', e);
                    }
                    if (window.SDN_DATABASE) {
                        window.SDN_DATABASE.bagan_struktur = compressedUrl;
                    }
                    syncToServer('bagan_struktur', compressedUrl);

                    refreshAdminBaganState();
                    inputCustomBaganFile.value = '';
                    showSyncToast('🎉 Gambar bagan struktur organisasi baru berhasil dipasang!');
                    alert('✅ Gambar bagan struktur organisasi baru berhasil dipasang!\\nBagan ini sekarang langsung tampil di halaman Dewan Guru publik.');
                };
                img.src = evt.target.result;
            };
            reader.readAsDataURL(file);
        });
    }

    function resetBaganToAutomatic() {
        if (!confirm('Kembalikan bagan struktur ke Bagan Interaktif Otomatis?\\nNama-nama guru di bagan akan kembali terkoneksi langsung dengan database guru.')) {
            return;
        }
        try {
            localStorage.removeItem('sdn_bagan_struktur');
        } catch (e) {}
        if (window.SDN_DATABASE) {
            delete window.SDN_DATABASE.bagan_struktur;
        }
        syncToServer('bagan_struktur', '');
        refreshAdminBaganState();
        showSyncToast('✨ Bagan dikembalikan ke mode interaktif otomatis.');
        alert('✅ Bagan struktur organisasi berhasil dikembalikan ke Bagan Interaktif Otomatis!\\nSusunan guru di bagan langsung sinkron dengan daftar guru di bawah.');
    }

    if (btnResetBaganToSvg) btnResetBaganToSvg.addEventListener('click', resetBaganToAutomatic);
    if (btnHapusCustomBagan) btnHapusCustomBagan.addEventListener('click', resetBaganToAutomatic);

    refreshAdminBaganState();
}'''

if target in js:
    js = js.replace(target, patch, 1)
    with open('js/admin.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Patched js/admin.js with Bagan manager successfully!")
else:
    print("Target not found in js/admin.js!")
