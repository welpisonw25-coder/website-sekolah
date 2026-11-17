with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update style block with modern admin header classes
header_css = """
        /* MODERN & TIDY ADMIN HEADER */
        .admin-topbar {
            background: #ffffff;
            border-bottom: 1px solid var(--border-color);
            min-height: 64px;
            padding: 10px 0;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(15,23,42,0.04);
        }
        .admin-topbar-inner {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }
        .admin-brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .admin-brand-logo {
            width: 42px;
            height: 42px;
            object-fit: contain;
        }
        .admin-brand-title {
            font-size: 16px;
            font-weight: 800;
            color: var(--primary);
            margin: 0;
            line-height: 1.2;
        }
        .admin-brand-subtitle {
            font-size: 11.5px;
            color: var(--dark-muted);
            font-weight: 600;
        }
        .admin-topbar-actions {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .admin-status-capsule {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 12px;
            font-weight: 700;
            color: #334155;
        }
        .status-indicator-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #10b981;
            box-shadow: 0 0 6px #10b981;
            display: inline-block;
        }
        .status-indicator-text {
            color: #047857;
        }
        .status-separator {
            color: #cbd5e1;
            margin: 0 2px;
        }
        .status-clock-text {
            color: #475569;
        }
        .admin-btn-group {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }
        .admin-header-btn {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 7px 14px;
            font-size: 12.5px;
            font-weight: 700;
            border-radius: 8px;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s ease;
            white-space: nowrap;
        }
        .btn-view-public {
            background: #f0fdf4;
            color: var(--primary);
            border: 1px solid #bbf7d0;
        }
        .btn-view-public:hover {
            background: #dcfce7;
            border-color: #86efac;
            transform: translateY(-1px);
        }
        .btn-sync-cloud {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #ffffff;
            border: none;
            box-shadow: 0 2px 8px rgba(16,185,129,0.25);
        }
        .btn-sync-cloud:hover {
            filter: brightness(1.05);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(16,185,129,0.35);
        }
        .btn-logout {
            background: #fee2e2;
            color: #b91c1c;
            border: 1px solid #fecaca;
        }
        .btn-logout:hover {
            background: #fca5a5;
            color: #7f1d1d;
            border-color: #f87171;
            transform: translateY(-1px);
        }
        @media (max-width: 600px) {
            .admin-header-btn {
                padding: 6px 10px;
                font-size: 11.5px;
            }
            .admin-status-capsule {
                font-size: 11px;
                padding: 4px 10px;
            }
        }
"""

if ".admin-topbar {" not in html:
    html = html.replace("</style>", header_css + "\n    </style>")

# 2. Replace old header with clean header
old_header_start = "<!-- TOP BAR ADMIN -->"
old_header_end = "<!-- BANNER PERINGATAN BILA DIBUKA DARI FILE OFFLINE LAPTOP (file:///) -->"

p1 = html.find(old_header_start)
p2 = html.find(old_header_end)

if p1 != -1 and p2 != -1:
    new_header = """<!-- TOP BAR ADMIN RAPI & MODERN -->
    <header class="admin-topbar">
        <div class="container admin-topbar-inner">
            <div class="admin-brand">
                <img src="images/logo-keerom.png" alt="Logo Keerom" class="admin-brand-logo" decoding="async" loading="lazy">
                <div>
                    <h1 class="admin-brand-title">SDN INPRES ARSO VIII</h1>
                    <span class="admin-brand-subtitle">Panel Pengelola Resmi (Admin Dashboard)</span>
                </div>
            </div>

            <div class="admin-topbar-actions">
                <div class="admin-status-capsule" title="Koneksi Cloud Realtime & Waktu Operasional">
                    <span class="status-indicator-dot"></span>
                    <span class="status-indicator-text">Cloud Live</span>
                    <span class="status-separator">|</span>
                    <span>🕒</span>
                    <span id="witClock" class="status-clock-text">Memuat waktu...</span>
                </div>
                
                <div class="admin-btn-group">
                    <a href="index.html" target="_blank" class="admin-header-btn btn-view-public" title="Buka Website Publik (Tab Baru)">
                        🌐 <span>Buka Website</span> ↗
                    </a>
                    <button onclick="publishAllToOnline(); return false;" class="admin-header-btn btn-sync-cloud" title="Simpan dan sinkronkan semua perubahan ke database Google Cloud">
                        🚀 <span>Sinkronkan ke Cloud</span>
                    </button>
                    <button id="adminLogoutBtn" class="admin-header-btn btn-logout" title="Keluar dari Panel Admin">
                        🚪 <span>Keluar</span>
                    </button>
                </div>
            </div>
        </div>
    </header>

    """
    html = html[:p1] + new_header + html[p2:]
    print("Header replaced successfully!")

# 3. Add clean logout link to sidebar bottom
sidebar_marker = "<!-- KONTEN UTAMA DASHBOARD -->"
p_sidebar = html.find(sidebar_marker)
if p_sidebar != -1 and "Keluar dari Admin" not in html:
    # Find the closing </aside> before p_sidebar
    p_aside_close = html.rfind("</aside>", 0, p_sidebar)
    if p_aside_close != -1:
        sidebar_logout_snippet = """
            <div style="margin-top: 24px; padding-top: 14px; border-top: 1px solid #e2e8f0;">
                <a href="#" class="admin-nav-item" onclick="if(confirm('Apakah Anda yakin ingin keluar dari panel admin?')) { localStorage.removeItem('sdn_admin_session'); window.location.href='login.html'; } return false;" style="color: #b91c1c; background: #fff1f2; border: 1px solid #fecdd3; border-radius: 8px;">
                    <span>🚪</span> <span>Keluar dari Admin</span>
                </a>
            </div>
        """
        html = html[:p_aside_close] + sidebar_logout_snippet + html[p_aside_close:]
        print("Sidebar logout link added!")

# 4. Remove Marquee box from tab-profil
marquee_start = "<!-- KELOLA MARQUEE / TEKS BERJALAN BERANDA -->"
p_mq_start = html.find(marquee_start)
if p_mq_start != -1:
    # Find closing </div> of tab-profil
    p_mq_end = html.find("</div>\n            </div>\n\n            <!-- ==============================================\n                 TAB KELOLA BERITA SEKOLAH", p_mq_start)
    if p_mq_end != -1:
        html = html[:p_mq_start] + html[p_mq_end+7:] # keep the closing </div> of tab-profil
        print("Marquee box removed from tab-profil!")
    else:
        # Alternative search
        p_mq_end2 = html.find("<!-- ==============================================\n                 TAB KELOLA BERITA SEKOLAH", p_mq_start)
        # Find last </div> before tab kelola berita
        p_last_div = html.rfind("</div>", p_mq_start, p_mq_end2)
        html = html[:p_mq_start] + html[p_last_div:]
        print("Marquee box removed (alt path)!")

# 5. Remove multi-user table from tab-pengaturan
multi_user_start = "<!-- 2. KELOLA PENGGUNA & HAK AKSES BERJENJANG (MULTI-ROLE) -->"
p_mu_start = html.find(multi_user_start)
if p_mu_start != -1:
    audit_start = "<!-- 3. CATATAN RIWAYAT AKTIVITAS PENGELOLA (AUDIT LOGS) -->"
    p_audit = html.find(audit_start, p_mu_start)
    if p_audit != -1:
        html = html[:p_mu_start] + html[p_audit:]
        print("Multi-user table removed from tab-pengaturan!")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished updating admin.html!")
