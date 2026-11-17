html_files = [
    'index.html', 'profil.html', 'guru.html', 'siswa.html', 'sapras.html',
    'sop.html', 'kolaborasi.html', 'pengembangan-guru.html', 'berita.html',
    'pengumuman.html', 'galeri.html', 'kontak.html', 'panduan.html'
]

all_pass = True
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        txt = f.read()
    start_pos = txt.find('<div class="top-bar">')
    end_pos = txt.find('<header class="site-header">')
    tb = txt[start_pos:end_pos]
    akr = 'badge-tag akreditasi' in tb
    net = 'badge-tag internet' in tb
    adm = 'top-bar-admin-btn' in tb
    clk = 'topBarClock' in tb
    ok = (not akr) and (not net) and adm and clk
    status = '[PASS]' if ok else '[FAIL]'
    print(f"{status} {hf:22} | Akreditasi in TopBar: {akr!s:5} | Starlink in TopBar: {net!s:5} | AdminBtn: {adm!s:5} | Clock: {clk}")
    if not ok:
        all_pass = False

print('\nFINAL RESULT: ' + ('ALL 13 PAGES 100% UNIFORM & VERIFIED!' if all_pass else 'SOME PAGES FAILED'))
