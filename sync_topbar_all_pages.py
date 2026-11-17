import re
import glob

new_top_bar = '''    <div class="top-bar">
        <div class="container">
            <div class="top-bar-left">
                <div class="top-bar-item">
                    <span>📍 Jln. Sulawesi, Kampung Dukwia, Distrik Arso Barat, Kab. Keerom - Papua</span>
                </div>
                <div class="top-bar-item top-bar-contact-hide">
                    <span>📞 0812-4821-9125</span>
                </div>
                <div class="top-bar-item top-bar-contact-hide">
                    <span>✉️ sdninpresarso8@gmail.com</span>
                </div>
            </div>
            <div class="top-bar-right">
                <div class="top-bar-clock" id="topBarClock" title="Waktu Indonesia Timur">
                    <span class="clock-icon">🕒</span> <span class="live-wit-clock">WIT</span>
                </div>
                <a href="login.html" class="top-bar-admin-btn" title="Masuk ke Portal Admin SDN Inpres Arso VIII">
                    <svg class="admin-user-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                    <span>Admin</span>
                </a>
            </div>
        </div>
    </div>'''

top_bar_regex = re.compile(r'^[ \t]*<div class="top-bar">[\s\S]*?</div>\s*</div>\s*</div>', re.MULTILINE)

target_files = [
    'berita.html',
    'galeri.html',
    'guru.html',
    'kolaborasi.html',
    'kontak.html',
    'panduan.html',
    'pengembangan-guru.html',
    'pengumuman.html',
    'profil.html',
    'sapras.html',
    'siswa.html',
    'sop.html'
]

updated_count = 0
for tf in target_files:
    with open(tf, 'r', encoding='utf-8') as f:
        content = f.read()

    match = top_bar_regex.search(content)
    if match:
        content = top_bar_regex.sub(new_top_bar, content, count=1)
        with open(tf, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1
        print(f'[OK] Replaced top-bar in {tf}')
    else:
        print(f'[WARN] Regex did not match in {tf}')

print(f'\nTotal files updated with new top bar: {updated_count} of {len(target_files)}')
