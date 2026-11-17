with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'id=[\"\']([^\"\']*kolaborasi[^\"]*)[\"\']', text, re.IGNORECASE)
print('Kolaborasi IDs:', matches)

matches_mitra = re.findall(r'id=[\"\']([^\"\']*mitra[^\"]*)[\"\']', text, re.IGNORECASE)
print('Mitra IDs:', matches_mitra)
