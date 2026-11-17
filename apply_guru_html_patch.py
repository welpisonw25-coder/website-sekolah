with open('guru.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update text tags in SVG with dynamic IDs
replacements = [
    # Kepsek
    ('<text x="130" y="32" text-anchor="middle" font-size="14.5" font-weight="800" fill="#0f172a">ADI PUSPITO,S.Pd.SD</text>',
     '<text x="130" y="32" text-anchor="middle" font-size="14.5" font-weight="800" fill="#0f172a" id="baganSvgNamaKepsek">ADI PUSPITO,S.Pd.SD</text>'),
    # Kelas 1
    ('<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a">YULI SYETIA SARI,S.Pd</text>',
     '<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a" id="baganSvgNamaKelas1">YULI SYETIA SARI,S.Pd</text>'),
    # Kelas 2
    ('<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a">ELIAS TABUNI,S.Pd</text>',
     '<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a" id="baganSvgNamaKelas2">ELIAS TABUNI,S.Pd</text>'),
    # Kelas 3
    ('<text x="125" y="27" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">RITA PAULINA</text>\n    <text x="125" y="43" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">WABISER,S.Pd</text>',
     '<text x="125" y="27" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" id="baganSvgNamaKelas3"><tspan x="125" y="27">RITA PAULINA</tspan><tspan x="125" y="43">WABISER,S.Pd</tspan></text>'),
    # Kelas 4
    ('<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a">WARNO,S.Pd.SD</text>',
     '<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a" id="baganSvgNamaKelas4">WARNO,S.Pd.SD</text>'),
    # Kelas 5
    ('<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a">RINI HANDAYANI,S.Pd</text>',
     '<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a" id="baganSvgNamaKelas5">RINI HANDAYANI,S.Pd</text>'),
    # Kelas 6
    ('<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a">CICIK MURSIDAH,S.Pd</text>',
     '<text x="125" y="32" text-anchor="middle" font-size="13.5" font-weight="700" fill="#0f172a" id="baganSvgNamaKelas6">CICIK MURSIDAH,S.Pd</text>'),
    # Penjas
    ('<text x="107.5" y="33" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">FERDINAND,S.Pd</text>',
     '<text x="107.5" y="33" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" id="baganSvgNamaPenjas">FERDINAND,S.Pd</text>'),
    # Agama Islam
    ('<text x="107.5" y="27" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Zainal Habib Al</text>\n    <text x="107.5" y="43" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Arif,S.Pd</text>',
     '<text x="107.5" y="27" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" id="baganSvgNamaAgIslam"><tspan x="107.5" y="27">Zainal Habiib Al</tspan><tspan x="107.5" y="43">Arif,S.Pd</tspan></text>'),
    # Agama Protestan
    ('<text x="107.5" y="27" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a">Ester Tina Maria</text>\n    <text x="107.5" y="43" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a">Panjaitan,S.Pd</text>',
     '<text x="107.5" y="27" text-anchor="middle" font-size="11.5" font-weight="700" fill="#0f172a" id="baganSvgNamaAgKristen"><tspan x="107.5" y="27">Esther Tina Maria</tspan><tspan x="107.5" y="43">Panjaitan,S.Pd</tspan></text>'),
    # Agama Katolik
    ('<text x="107.5" y="27" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Flavianus</text>\n    <text x="107.5" y="43" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Renaldus,S.Ag</text>',
     '<text x="107.5" y="27" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" id="baganSvgNamaAgKatolik"><tspan x="107.5" y="27">Flavianus</tspan><tspan x="107.5" y="43">Rainaldus,S.Ag</tspan></text>')
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1
    else:
        print("Not found:", old[:40])

print(f"Replaced {count} text tags in SVG")

# 2. Add containers around SVG: baganStrukturWrapper, baganCustomImageContainer, baganSvgContainer
target_wrapper = '<div class="org-diagram-wrapper" style="width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; padding: 15px 10px; border: 1px solid #e2e8f0; border-radius: 12px; background: #ffffff; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">'
new_wrapper = '''<div class="org-diagram-wrapper" id="baganStrukturWrapper" style="width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; padding: 15px 10px; border: 1px solid #e2e8f0; border-radius: 12px; background: #ffffff; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);">
                    <!-- Wadah Gambar Bagan Kustom (Jika diunggah lewat Admin) -->
                    <div id="baganCustomImageContainer" style="display: none; text-align: center; padding: 10px 0;">
                        <img id="baganCustomImg" src="" alt="Bagan Struktur Organisasi Resmi SDN Inpres Arso VIII" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); cursor: pointer;" onclick="if(window.openBaganModal){ window.openBaganModal(); }" title="Klik untuk memperbesar bagan layar penuh">
                    </div>

                    <!-- Wadah Bagan Vektor Interaktif (Otomatis Terkoneksi dengan Database Guru) -->
                    <div id="baganSvgContainer">'''

if target_wrapper in html:
    html = html.replace(target_wrapper, new_wrapper, 1)
    # Close baganSvgContainer right after </svg>
    svg_close = '</svg>'
    svg_pos = html.find(svg_close, html.find('id="baganSvgContainer"'))
    if svg_pos != -1:
        html = html[:svg_pos+len(svg_close)] + '\n                    </div>' + html[svg_pos+len(svg_close):]
        print("Wrapped SVG inside baganSvgContainer successfully!")

with open('guru.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated guru.html successfully!")
