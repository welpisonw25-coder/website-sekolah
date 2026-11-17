# -*- coding: utf-8 -*-
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

target_g_kat = '<label class="form-label">Kategori Kegiatan *</label>'
replace_g_kat = '''<label class="form-label">Status Publikasi Foto *</label>
                                <select id="galeriStatus" class="form-input" style="font-weight: 700; margin-bottom: 12px;">
                                    <option value="published" selected>🚀 Terbitkan Langsung (Galeri Publik)</option>
                                    <option value="draft">💾 Simpan Sebagai Draft</option>
                                </select>
                            </div>
                            <div class="form-group" style="flex: 1;">
                                <label class="form-label">Kategori Kegiatan *</label>'''

if target_g_kat in admin_html:
    admin_html = admin_html.replace(target_g_kat, replace_g_kat, 1)
    print("Patched galeriStatus in admin.html")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)
