with open('js/admin.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'admin_users|renderUserTable|showAddUserModal|deleteUser', text)]
print('Matches for user management:', len(matches))
for idx in matches[:6]:
    print(text[max(0, idx-50):min(len(text), idx+250)].replace('\n', ' '))
    print("-" * 50)
