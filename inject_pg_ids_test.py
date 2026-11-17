import re

with open('pengembangan-guru.html', 'r', encoding='utf-8') as f:
    pg = f.read()

# 1. Deskripsi Gugus
pg = re.sub(
    r'(<p style="font-size: 14px; color: #475569; line-height: 1\.7; margin-bottom: 18px;">)',
    r'<p id="pgGusekDeskripsi" style="font-size: 14px; color: #475569; line-height: 1.7; margin-bottom: 18px;">',
    pg, count=1
)

# 2. Sekretariat, Ketua, Waktu, Dasar SK
pg = pg.replace(
    '<div>📍 <strong>Sekretariat:</strong> Jalan Melati Barat Arso I, Kampung Sanggaria, Distrik Arso Barat 99473</div>',
    '<div>📍 <strong>Sekretariat:</strong> <span id="pgGusekSekretariat">Jalan Melati Barat Arso I, Kampung Sanggaria, Distrik Arso Barat 99473</span></div>'
)
pg = pg.replace(
    '<div>👤 <strong>Ketua Pengelola:</strong> Robi Ulludin, S.Pd.SD. (NIP 196906201992031018)</div>',
    '<div>👤 <strong>Ketua Pengelola:</strong> <span id="pgGusekKetua">Robi Ulludin, S.Pd.SD. (NIP 196906201992031018)</span></div>'
)
pg = pg.replace(
    '<div>⏱️ <strong>Waktu Pertemuan:</strong> Hari Rabu Bergilir (Semester Gasal TP 2026/2027)</div>',
    '<div>⏱️ <strong>Waktu Pertemuan:</strong> <span id="pgGusekWaktu">Hari Rabu Bergilir (Semester Gasal TP 2026/2027)</span></div>'
)
pg = pg.replace(
    '<div>📜 <strong>Dasar Penetapan:</strong> SK Resmi Gusek 1 Arso Barat, 23 Juli 2026</div>',
    '<div>📜 <strong>Dasar Penetapan:</strong> <span id="pgGusekDasarSK">SK Resmi Gusek 1 Arso Barat, 23 Juli 2026</span></div>'
)

# 3. K3S Programs List & Ketua Box
pg = re.sub(
    r'(<span>📋</span> <span>Uraian Kerja & Program Strategis K3S:</span>[\s\S]*?</h4>\s*<ul style="margin: 0; padding-left: 20px; font-size: 13\.5px; color: #334155; line-height: 1\.8;")',
    r'\1 id="pgK3SProgramsList"',
    pg, count=1
)
pg = re.sub(
    r'(<div style="font-size: 13px; color: #64748b;">\s*👤 Ketua Pengelola KKKS Gusek 1:)',
    r'<div id="pgK3SKetuaBox" style="font-size: 13px; color: #64748b;">\n                    👤 Ketua Pengelola KKKS Gusek 1:',
    pg, count=1
)

# 4. Kelompok A
pg = re.sub(
    r'(<!-- KELOMPOK A -->[\s\S]*?<h3 style="font-size: 19px; font-weight: 800; color: #0f172a; margin-bottom: 8px;">)',
    r'<!-- KELOMPOK A -->\n                <div class="card" style="padding: 26px; border-top: 5px solid #10b981; box-shadow: 0 4px 14px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between;">\n                    <div>\n                        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; margin-bottom: 12px;">\n                            <span class="badge-tag" style="background: #d1fae5; color: #065f46; font-size: 11px; font-weight: 700;">KELOMPOK A (KELAS RENDAH & AGAMA)</span>\n                            <span style="background: #f1f5f9; color: #475569; font-size: 11.5px; font-weight: 700; padding: 3px 10px; border-radius: 999px;">1 Bulan Sekali</span>\n                        </div>\n                        <h3 id="pgKelompokAJudul" style="font-size: 19px; font-weight: 800; color: #0f172a; margin-bottom: 8px;">',
    pg, count=1
)
# Note: make sure replace doesn't duplicate card tags. Let's do more direct replacements.
