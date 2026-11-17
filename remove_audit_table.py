with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

audit_marker = '<!-- 3. CATATAN RIWAYAT AKTIVITAS PENGELOLA (AUDIT LOGS) -->'
p1 = html.find(audit_marker)
if p1 != -1:
    # Find the closing </main> after p1
    p_main = html.find('</main>', p1)
    # The last </div> before </main> is the closing of tab-pengaturan
    p_tab_close = html.rfind('</div>', p1, p_main)
    # The div before that was the closing of the card
    p_card_close = html.rfind('</div>', p1, p_tab_close)
    
    # We remove from p1 to the end of the card (p_card_close + 6)
    card_to_remove = html[p1:p_card_close+6]
    print("Found card to remove:\n", card_to_remove[:100], "...\n", card_to_remove[-50:])
    html = html[:p1] + html[p_card_close+6:]
    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully removed audit table card from admin.html!")
else:
    print("audit_marker not found in admin.html!")

# Now clean up js/admin.js
with open('js/admin.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace logAdminActivity and renderActivityLogs
p_log_start = js.find('/* -------------------------------------------------------------------\n   14. SISTEM LOG AKTIVITAS PENGELOLA (AUDIT TRAIL)')
p_prof_start = js.find('/* -------------------------------------------------------------------\n   15. PENGELOLA PROFIL SEKOLAH')

if p_log_start != -1 and p_prof_start != -1:
    safe_stub = """/* -------------------------------------------------------------------
   14. SISTEM LOG AKTIVITAS PENGELOLA (AUDIT TRAIL - DINONAKTIFKAN SESUAI ARAHAN)
   ------------------------------------------------------------------- */
function logAdminActivity(aksi, keterangan) {}
window.logAdminActivity = logAdminActivity;
function renderActivityLogs() {}
window.renderActivityLogs = renderActivityLogs;

"""
    js = js[:p_log_start] + safe_stub + js[p_prof_start:]
    print("Replaced logAdminActivity and renderActivityLogs with safe stubs in js/admin.js!")

# Remove any remaining calls to renderActivityLogs
js = js.replace("try { if (typeof renderActivityLogs === 'function') renderActivityLogs(); } catch (e) {}\n", "")
js = js.replace("if (typeof renderActivityLogs === 'function') renderActivityLogs();\n", "")

with open('js/admin.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Finished updating admin.html and js/admin.js!")
