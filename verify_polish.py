with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

top_bar_chunk = html[:html.find('site-header')]

# Checks
checks = [
    ('heroMarqueeBar not in index.html', 'heroMarqueeBar' not in html),
    ('heroWelcomeStage in index.html', 'heroWelcomeStage' in html),
    ('welcomePhase1 in index.html', 'welcomePhase1' in html),
    ('welcomePhase2 in index.html', 'welcomePhase2' in html),
    ('welcomePhase3 in index.html', 'welcomePhase3' in html),
    ('topBarClock in index.html', 'topBarClock' in html),
    ('top-bar-admin-btn in index.html', 'top-bar-admin-btn' in html),
    ('admin-user-icon in index.html', 'admin-user-icon' in html),
    ('badge-tag akreditasi not in top-bar', 'badge-tag akreditasi' not in top_bar_chunk),
    ('badge-tag internet not in top-bar', 'badge-tag internet' not in top_bar_chunk),
    ('hero-welcome-stage in css', '.hero-welcome-stage' in css),
    ('welcome-text-white in css', '.welcome-text-white' in css),
    ('welcome-text-gold in css', '.welcome-text-gold' in css),
    ('welcome-text-identity in css', '.welcome-text-identity' in css),
    ('top-bar-admin-btn in css', '.top-bar-admin-btn' in css),
    ('initHeroInteractions in js', 'function initHeroInteractions' in js),
    ('PHASE_DURATION in js', 'PHASE_DURATION' in js)
]

all_ok = True
for name, ok in checks:
    status = '[PASS]' if ok else '[FAIL]'
    print(f'{status} {name}')
    if not ok:
        all_ok = False

if all_ok:
    print('\nALL 17 VERIFICATION CHECKS PASSED!')
else:
    print('\nSOME CHECKS FAILED!')
