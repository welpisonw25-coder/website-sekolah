with open('profil.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Has profilVisiQuote:", 'profilVisiQuote' in text)
print("Has profilMisiList:", 'profilMisiList' in text)
print("Has profilTujuanList:", 'profilTujuanList' in text)
print("Has profilNPSN:", 'profilNPSN' in text)
print("Has loadDynamicProfil:", 'loadDynamicProfil' in text)

# Let's inspect elements with id in profil.html
ids = re.findall(r'id=["\']([^"\']+)["\']', text)
print("IDs in profil.html:", ids)
