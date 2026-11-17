with open('js/admin.js', 'r', encoding='utf-8') as f:
    admin_js = f.read()

lines = admin_js.splitlines()
for i, l in enumerate(lines):
    if 'initbackuprestoremanager' in l.lower() or 'sdn_backup_' in l.lower() or 'btnexportbackup' in l.lower():
        for j in range(max(0, i-5), min(i+45, len(lines))):
            print(f"{j+1}: {lines[j]}")
        break
