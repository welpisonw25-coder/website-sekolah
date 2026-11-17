# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

checks = [
    # Admin tabs
    ('admin.html', 'tab-ringkasan' in admin_html, 'tab-ringkasan exists'),
    ('admin.html', 'tab-sambutan' in admin_html, 'tab-sambutan exists'),
    ('admin.html', 'tab-profil' in admin_html, 'tab-profil exists'),
    ('admin.html', 'tab-berita' in admin_html, 'tab-berita exists'),
    ('admin.html', 'tab-pengumuman' in admin_html, 'tab-pengumuman exists'),
    ('admin.html', 'tab-galeri' in admin_html, 'tab-galeri exists'),
    ('admin.html', 'tab-siswa' in admin_html, 'tab-siswa exists'),
    ('admin.html', 'tab-guru' in admin_html, 'tab-guru exists'),
    ('admin.html', 'tab-ppdb' in admin_html, 'tab-ppdb exists'),
    ('admin.html', 'tab-sarpras' in admin_html, 'tab-sarpras exists'),
    ('admin.html', 'tab-kolaborasi' in admin_html, 'tab-kolaborasi exists'),
    ('admin.html', 'tab-kkg' in admin_html, 'tab-kkg exists'),
    ('admin.html', 'tab-kontak' in admin_html, 'tab-kontak exists'),
    ('admin.html', 'tab-sop' in admin_html, 'tab-sop exists'),
    ('admin.html', 'tab-pengaturan' in admin_html, 'tab-pengaturan exists'),
    # Status selectors
    ('admin.html', 'id="beritaStatus"' in admin_html, 'beritaStatus selector exists'),
    ('admin.html', 'id="pengumumanStatus"' in admin_html, 'pengumumanStatus selector exists'),
    ('admin.html', 'id="galeriStatus"' in admin_html, 'galeriStatus selector exists'),
    # Profil inputs
    ('admin.html', 'id="profilVisiInput"' in admin_html, 'profilVisiInput exists'),
    ('admin.html', 'id="identitasNPSN"' in admin_html, 'identitasNPSN exists'),
    # Kontak inputs
    ('admin.html', 'id="kontakInputTelepon"' in admin_html, 'kontakInputTelepon exists'),
    ('admin.html', 'id="pesanKontakTableBody"' in admin_html, 'pesanKontakTableBody exists'),
    # User management
    ('admin.html', 'id="adminUsersTableBody"' in admin_html, 'adminUsersTableBody exists'),
    ('admin.html', 'id="adminLogsTableBody"' in admin_html, 'adminLogsTableBody exists'),
    # JS Admin functions
    ('js/admin.js', 'function getProfilData' in admin_js, 'getProfilData function exists'),
    ('js/admin.js', 'function saveProfilData' in admin_js, 'saveProfilData function exists'),
    ('js/admin.js', 'function getKontakData' in admin_js, 'getKontakData function exists'),
    ('js/admin.js', 'function saveKontakData' in admin_js, 'saveKontakData function exists'),
    ('js/admin.js', 'function renderPesanKontakTable' in admin_js, 'renderPesanKontakTable function exists'),
    ('js/admin.js', 'function logAdminActivity' in admin_js, 'logAdminActivity function exists'),
    ('js/admin.js', 'function renderUserTable' in admin_js, 'renderUserTable function exists'),
    ('js/admin.js', 'function renderActivityLogs' in admin_js, 'renderActivityLogs function exists'),
    # JS Main functions
    ('js/main.js', 'function loadDynamicProfil' in main_js, 'loadDynamicProfil function exists'),
    ('js/main.js', 'function loadDynamicKontak' in main_js, 'loadDynamicKontak function exists'),
    ('js/main.js', 'item.status !== \'draft\'' in main_js, 'draft filtering in main.js exists'),
]

all_passed = True
for target, passed, desc in checks:
    status = 'PASS' if passed else 'FAIL'
    if not passed: all_passed = False
    print(f"[{status}] ({target}) {desc}")

print(f"\nTotal verification: {'ALL PASSED!' if all_passed else 'SOME FAILED!'}")
