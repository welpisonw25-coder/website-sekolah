# -*- coding: utf-8 -*-
with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

# 1. Update renderBerita row to show status badge and toggle button
target_berita_row = '''                            <span class="badge" style="background: #e0f2fe; color: #0369a1; font-size: 11px; padding: 3px 8px; border-radius: 4px; font-weight: 700; display: inline-block; margin-bottom: 4px;">
                                ${escapeHTML(item.kategori || 'Kegiatan')}
                            </span>
                            <div style="font-size: 11.5px; color: #64748b;">📅 ${escapeHTML(item.tanggal)}</div>
                            <div style="font-size: 11px; color: #94a3b8;">✍️ ${escapeHTML(item.penulis || 'Humas')}</div>
                        </td>
                        <td style="text-align: center; white-space: nowrap;">
                            <button type="button" class="btn-edit-berita" data-id="${item.id}" title="Edit Berita Ini" style="background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; padding: 6px 11px; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 700; margin-right: 4px;">
                                ✏️ Edit
                            </button>'''

replacement_berita_row = '''                            <span class="badge" style="background: #e0f2fe; color: #0369a1; font-size: 11px; padding: 3px 8px; border-radius: 4px; font-weight: 700; display: inline-block; margin-bottom: 4px;">
                                ${escapeHTML(item.kategori || 'Kegiatan')}
                            </span>
                            <div style="margin-bottom: 4px;">
                                ${item.status === 'draft' ? '<span style="background: #fef3c7; color: #92400e; font-size: 10.5px; font-weight: 800; padding: 2px 7px; border-radius: 4px; border: 1px solid #fcd34d;">🟡 Draft</span>' : '<span style="background: #dcfce7; color: #166534; font-size: 10.5px; font-weight: 800; padding: 2px 7px; border-radius: 4px; border: 1px solid #86efac;">🟢 Terbit</span>'}
                            </div>
                            <div style="font-size: 11.5px; color: #64748b;">📅 ${escapeHTML(item.tanggal)}</div>
                            <div style="font-size: 11px; color: #94a3b8;">✍️ ${escapeHTML(item.penulis || 'Humas')}</div>
                        </td>
                        <td style="text-align: center; white-space: nowrap;">
                            <button type="button" class="btn-toggle-status-berita" data-id="${item.id}" title="Ubah Status Publikasi" style="background: ${item.status === 'draft' ? '#fef3c7' : '#f1f5f9'}; border: 1px solid ${item.status === 'draft' ? '#fcd34d' : '#cbd5e1'}; color: ${item.status === 'draft' ? '#b45309' : '#334155'}; padding: 5px 9px; border-radius: 6px; cursor: pointer; font-size: 11.5px; font-weight: 700; margin-right: 4px;">
                                ${item.status === 'draft' ? '🚀 Terbitkan' : '💾 Jadikan Draft'}
                            </button>
                            <button type="button" class="btn-edit-berita" data-id="${item.id}" title="Edit Berita Ini" style="background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; padding: 6px 11px; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 700; margin-right: 4px;">
                                ✏️ Edit
                            </button>'''

if target_berita_row in admin_js:
    admin_js = admin_js.replace(target_berita_row, replacement_berita_row, 1)
    print("Patched status badge in renderBerita")

# Bind btn-toggle-status-berita
target_berita_bind = "tableBody.querySelectorAll('.btn-edit-berita').forEach(btn => {"
replacement_berita_bind = """tableBody.querySelectorAll('.btn-toggle-status-berita').forEach(btn => {
                    btn.addEventListener('click', function() {
                        const id = parseInt(this.getAttribute('data-id'), 10);
                        const all = getBeritaData();
                        const item = all.find(b => b.id === id);
                        if (!item) return;
                        item.status = (item.status === 'draft') ? 'published' : 'draft';
                        saveBeritaData(all);
                        renderBerita();
                        logAdminActivity('Ubah Status Berita', `Mengubah status "${(item.judul || '').slice(0, 30)}..." menjadi ${item.status}`);
                        showSyncToast(item.status === 'published' ? '🚀 Berita berhasil diterbitkan!' : '💾 Berita diubah menjadi draft.');
                    });
                });

                tableBody.querySelectorAll('.btn-edit-berita').forEach(btn => {"""

if target_berita_bind in admin_js:
    admin_js = admin_js.replace(target_berita_bind, replacement_berita_bind, 1)
    print("Bound btn-toggle-status-berita in renderBerita")

# 2. Update renderTable in pengumuman
target_peng_row = "<td><span class=\"badge-tag akreditasi\" style=\"font-size: 11px;\">${escapeHTML(item.kategori || 'UMUM')}</span></td>"
replacement_peng_row = """<td>
                        <span class="badge-tag akreditasi" style="font-size: 11px;">${escapeHTML(item.kategori || 'UMUM')}</span>
                        <div style="margin-top: 4px;">
                            ${item.status === 'draft' ? '<span style="background: #fef3c7; color: #92400e; font-size: 10.5px; font-weight: 800; padding: 2px 7px; border-radius: 4px; border: 1px solid #fcd34d;">🟡 Draft</span>' : '<span style="background: #dcfce7; color: #166534; font-size: 10.5px; font-weight: 800; padding: 2px 7px; border-radius: 4px; border: 1px solid #86efac;">🟢 Terbit</span>'}
                        </div>
                    </td>"""

if target_peng_row in admin_js:
    admin_js = admin_js.replace(target_peng_row, replacement_peng_row, 1)
    print("Patched status badge in renderPengumuman")

target_peng_btn = '<button type="button" class="btn-action-edit-pengumuman"'
replacement_peng_btn = """<button type="button" class="btn-toggle-status-pengumuman" data-id="${item.id}" style="background: ${item.status === 'draft' ? '#fef3c7' : '#f1f5f9'}; border: 1px solid ${item.status === 'draft' ? '#fcd34d' : '#cbd5e1'}; color: ${item.status === 'draft' ? '#b45309' : '#334155'}; padding: 5px 8px; border-radius: 6px; cursor: pointer; font-size: 11px; font-weight: 700; margin-right: 4px;">
                            ${item.status === 'draft' ? '🚀 Terbitkan' : '💾 Draft'}
                        </button>
                        <button type="button" class="btn-action-edit-pengumuman\""""

if target_peng_btn in admin_js:
    admin_js = admin_js.replace(target_peng_btn, replacement_peng_btn, 1)
    print("Added toggle button in renderPengumuman")

target_peng_bind = "tableBody.querySelectorAll('.btn-action-edit-pengumuman').forEach(btn => {"
replacement_peng_bind = """tableBody.querySelectorAll('.btn-toggle-status-pengumuman').forEach(btn => {
                btn.addEventListener('click', function() {
                    const id = parseInt(this.getAttribute('data-id'), 10);
                    const all = getPengumumanData();
                    const item = all.find(p => p.id === id);
                    if (!item) return;
                    item.status = (item.status === 'draft') ? 'published' : 'draft';
                    savePengumumanData(all);
                    renderTable();
                    logAdminActivity('Ubah Status Pengumuman', `Mengubah status "${(item.judul || '').slice(0, 30)}..." menjadi ${item.status}`);
                    showSyncToast(item.status === 'published' ? '🚀 Pengumuman berhasil diterbitkan!' : '💾 Pengumuman diubah menjadi draft.');
                });
            });

            tableBody.querySelectorAll('.btn-action-edit-pengumuman').forEach(btn => {"""

if target_peng_bind in admin_js:
    admin_js = admin_js.replace(target_peng_bind, replacement_peng_bind, 1)
    print("Bound btn-toggle-status-pengumuman")

# 3. Update formGaleri submit to capture status
target_galeri_submit = "const judul = document.getElementById('galeriJudul').value.trim();"
replace_galeri_submit = """const statusEl = document.getElementById('galeriStatus');
        const statusVal = statusEl ? statusEl.value : 'published';
        const judul = document.getElementById('galeriJudul').value.trim();"""
if target_galeri_submit in admin_js:
    admin_js = admin_js.replace(target_galeri_submit, replace_galeri_submit, 1)
    print("Patched formGaleri submit")

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(admin_js)

print("Finished updating status toggle functionality in js/admin.js!")
