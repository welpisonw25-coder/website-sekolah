with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

lines_admin = admin_js.splitlines()
print(f"Total lines in js/admin.js: {len(lines_admin)}")

# check KKG functions and SOP functions
for i, l in enumerate(lines_admin):
    if 'kkg' in l.lower() or 'sop' in l.lower() or 'syncguruwithsiswa' in l.lower() or 'populatewalidropdowns' in l.lower():
        print(f"Line {i+1}: {l.strip()[:100]}")
