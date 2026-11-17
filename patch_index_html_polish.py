import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Top Bar
top_bar_pattern = re.compile(r'<div class="top-bar">[\s\S]*?<!-- ==========================================\s+HEADER & NAVIGASI', re.MULTILINE)

new_top_bar = '''<div class="top-bar">
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
    </div>

    <!-- ==========================================
         HEADER & NAVIGASI'''

match_top = top_bar_pattern.search(content)
assert match_top, 'top_bar_pattern not matched'
content = top_bar_pattern.sub(new_top_bar, content, count=1)
print('Top bar successfully matched and replaced!')

# 2. Update Hero Section (Remove marquee ticker, add hero-welcome-stage before hero-glass-card)
hero_pattern = re.compile(r'<section class="hero-section" id="heroSection">[\s\S]*?<div class="hero-glass-card" id="heroGlassCard">', re.MULTILINE)

new_hero_intro = '''<section class="hero-section" id="heroSection">
        <div class="container hero-container">
            <div class="hero-content-wrapper">
                <!-- ==========================================
                     ANIMASI SAMBUTAN ELEGAN (3 TAHAP BERKESINAMBUNGAN)
                     Tahap 1: SELAMAT DATANG (Putih, Bold, Slide-Up Halus)
                     Tahap 2: PORTAL RESMI • KAMPUNG DUKWIA, KEEROM, PAPUA (Emas/Kuning, Bold)
                     Tahap 3: SDN INPRES ARSO VIII (Identitas Sekolah)
                     ========================================== -->
                <div class="hero-welcome-stage" id="heroWelcomeStage" aria-live="polite">
                    <div class="welcome-sequence-track">
                        <!-- TAHAP 1: SELAMAT DATANG -->
                        <div class="welcome-phase phase-1 active" id="welcomePhase1">
                            <span class="welcome-text-white">SELAMAT DATANG</span>
                        </div>
                        <!-- TAHAP 2: PORTAL RESMI -->
                        <div class="welcome-phase phase-2" id="welcomePhase2">
                            <span class="welcome-text-gold">✨ PORTAL RESMI • KAMPUNG DUKWIA, KEEROM, PAPUA ✨</span>
                        </div>
                        <!-- TAHAP 3: IDENTITAS SEKOLAH -->
                        <div class="welcome-phase phase-3" id="welcomePhase3">
                            <span class="welcome-text-identity">SDN INPRES ARSO VIII</span>
                        </div>
                    </div>
                </div>

                <!-- Kartu Portal Resmi Sekolah (Latar Hijau Tua, Emas & Putih) -->
                <div class="hero-glass-card" id="heroGlassCard">'''

match_hero = hero_pattern.search(content)
assert match_hero, 'hero_pattern not matched'
content = hero_pattern.sub(new_hero_intro, content, count=1)
print('Hero intro and welcome animation successfully matched and replaced!')

# 3. Clean up heroGateShowcaseBadge
content = re.sub(r'<!-- Indikator Halus Saat Foto Gapura Terbuka Penuh -->\s*<div class="hero-gate-showcase-badge" id="heroGateShowcaseBadge">[\s\S]*?</div>', '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('SUCCESS: index.html patched successfully!')
