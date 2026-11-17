# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

target_ann = "if (!items || items.length === 0) items = defaultPengumuman;"
replace_ann = """if (!items || items.length === 0) items = defaultPengumuman;
        // Filter konten draft agar tidak tampil pada pengunjung publik
        items = (items || []).filter(item => item && item.status !== 'draft');"""

if target_ann in main_js:
    main_js = main_js.replace(target_ann, replace_ann)
    print("Patched draft filter in loadDynamicAnnouncements")

target_gal = "if (items) {\n        window._allPublicGallery = items;"
replace_gal = """if (items) {
        // Filter konten draft agar tidak tampil pada pengunjung publik
        items = (items || []).filter(item => item && item.status !== 'draft');
        window._allPublicGallery = items;"""

if target_gal in main_js:
    main_js = main_js.replace(target_gal, replace_gal)
    print("Patched draft filter in loadDynamicGallery")

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(main_js)
