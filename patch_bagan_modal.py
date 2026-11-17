with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = '''<div id="baganCanvasCard" style="background: #ffffff; border-radius: 12px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.55); padding: 16px; width: 1060px; height: 710px; box-sizing: content-box; transform-origin: 0 0; transition: transform 0.12s ease-out;">
                        <img src="images/bagan-struktur-organisasi.svg" alt="Bagan Struktur Organisasi SDN Inpres Arso VIII" style="display: block; width: 1060px; height: 710px; pointer-events: none;" draggable="false">
                    </div>'''

replacement = '''<div id="baganCanvasCard" style="background: #ffffff; border-radius: 12px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.55); padding: 16px; width: 1060px; height: 710px; box-sizing: content-box; transform-origin: 0 0; transition: transform 0.12s ease-out;">
                        <div id="baganModalContentHolder" style="width: 1060px; height: 710px;">
                            <img src="images/bagan-struktur-organisasi.svg" alt="Bagan Struktur Organisasi SDN Inpres Arso VIII" style="display: block; width: 1060px; height: 710px; pointer-events: none;" draggable="false">
                        </div>
                    </div>'''

if target in js:
    js = js.replace(target, replacement, 1)
    print("Replaced baganCanvasCard inside modal template!")
else:
    print("Target baganCanvasCard not found!")

target_open = "modal.style.display = 'flex';"
replacement_open = '''modal.style.display = 'flex';

    // Perbarui isi modal sesuai bagan aktif saat ini (Gambar Kustom atau SVG Vektor Sinkron)
    const modalHolder = document.getElementById('baganModalContentHolder');
    if (modalHolder) {
        if (window._currentActiveBaganSrc && window._currentActiveBaganSrc.startsWith('data:')) {
            modalHolder.innerHTML = `<img src="${window._currentActiveBaganSrc}" alt="Bagan Struktur Organisasi SDN Inpres Arso VIII" style="display: block; width: 1060px; height: 710px; object-fit: contain; pointer-events: none;" draggable="false">`;
        } else {
            const liveSvg = document.getElementById('baganSvgContainer');
            if (liveSvg && liveSvg.querySelector('svg')) {
                modalHolder.innerHTML = liveSvg.innerHTML;
            } else {
                modalHolder.innerHTML = `<img src="images/bagan-struktur-organisasi.svg" alt="Bagan Struktur Organisasi SDN Inpres Arso VIII" style="display: block; width: 1060px; height: 710px; pointer-events: none;" draggable="false">`;
            }
        }
    }'''

if target_open in js:
    js = js.replace(target_open, replacement_open, 1)
    print("Added dynamic modal content update to openBaganModal!")
else:
    print("Target target_open not found!")

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated js/main.js successfully!")
