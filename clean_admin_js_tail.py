with open('js/admin.js', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "/* -------------------------------------------------------------------\n   17. KELOLA PENGUMUMAN BERJALAN & KONTEN KHUSUS BERANDA"
if start_marker not in text:
    # Look for alternative
    start_marker = "/* -------------------------------------------------------------------\n   18. PENGELOLA PENGGUNA & HAK AKSES SISTEM (MULTI-ROLE)"

p_start = text.find("/* -------------------------------------------------------------------\n   17. KELOLA PENGUMUMAN BERJALAN")
if p_start == -1:
    p_start = text.find("/* -------------------------------------------------------------------\n   18. PENGELOLA PENGGUNA")

clean_tail = """
// INJEKSI PADA REFRESH ADMIN MANAGERS
const _prevRefresh = window.refreshAdminManagers;
window.refreshAdminManagers = function() {
    if (typeof _prevRefresh === 'function') {
        try { _prevRefresh(); } catch (e) {}
    }
    try { if (typeof populateProfilForm === 'function') populateProfilForm(); } catch (e) {}
    try { if (typeof populateKontakForm === 'function') populateKontakForm(); } catch (e) {}
    try { if (typeof renderActivityLogs === 'function') renderActivityLogs(); } catch (e) {}
};

// INITIALIZATION DI AKHIR DOM READY
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        if (typeof populateProfilForm === 'function') populateProfilForm();
        if (typeof populateKontakForm === 'function') populateKontakForm();
        if (typeof renderActivityLogs === 'function') renderActivityLogs();
    }, 300);
});
"""

if p_start != -1:
    text = text[:p_start] + clean_tail
    with open('js/admin.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully cleaned up tail of js/admin.js!")
else:
    print("Marker not found in js/admin.js")
