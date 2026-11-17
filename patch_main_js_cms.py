# -*- coding: utf-8 -*-
with open('js/main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# 1. Update refreshDataFromCloud to save and load profil & kontak & beranda
old_refresh = "loadDynamicSOP();\n                renderPPDBPublicInfo();"
new_refresh = """loadDynamicSOP();
                loadDynamicProfil();
                loadDynamicKontak();
                loadDynamicBeranda();
                renderPPDBPublicInfo();"""
assert old_refresh in main_js, "old_refresh not found"
main_js = main_js.replace(old_refresh, new_refresh)

# Also in the fallback offline branch
old_fallback = "loadDynamicTeachers();\n            "
# Let's find DOMContentLoaded loaders
old_dom_loaders = "loadDynamicSOP();\n\n    // Eksekusi pembaruan realtime"
new_dom_loaders = """loadDynamicSOP();
    loadDynamicProfil();
    loadDynamicKontak();
    loadDynamicBeranda();

    // Eksekusi pembaruan realtime"""
if old_dom_loaders in main_js:
    main_js = main_js.replace(old_dom_loaders, new_dom_loaders)

# 2. Draft filtering in loadDynamicNews
old_news_filter = "if (!newsData) newsData = defaultMainNewsList;\n    window._allPublicNews = newsData;"
new_news_filter = """if (!newsData) newsData = defaultMainNewsList;
    // Filter konten draft agar tidak tampil di publik
    newsData = (newsData || []).filter(item => item && item.status !== 'draft');
    window._allPublicNews = newsData;"""
assert old_news_filter in main_js, "old_news_filter not found"
main_js = main_js.replace(old_news_filter, new_news_filter)

# 3. Draft filtering in loadDynamicAnnouncements
old_ann_slice = "announcements = window.SDN_DATABASE.pengumuman;\n    }"
new_ann_slice = """announcements = window.SDN_DATABASE.pengumuman;
    }
    // Filter draft pengumuman
    announcements = (announcements || []).filter(item => item && item.status !== 'draft');"""
assert old_ann_slice in main_js, "old_ann_slice not found"
main_js = main_js.replace(old_ann_slice, new_ann_slice)

# 4. Draft filtering in loadDynamicGallery
old_gal_filter = "function loadDynamicGallery() {"
new_gal_filter = """function loadDynamicGallery() {
    let galleryData = null;
    if (window.SDN_DATABASE && Array.isArray(window.SDN_DATABASE.galeri)) {
        galleryData = window.SDN_DATABASE.galeri.filter(item => item && item.status !== 'draft');
    }"""
# Let's check how loadDynamicGallery begins
print("Check loadDynamicGallery snippet:")
idx_gal = main_js.find('function loadDynamicGallery()')
print(main_js[idx_gal:idx_gal+300])
