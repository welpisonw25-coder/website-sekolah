with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Has formProfilSekolah:", 'formProfilSekolah' in text)
print("Has berandaMarqueeInput:", 'berandaMarqueeInput' in text)
print("Has adminUsersTableBody:", 'adminUsersTableBody' in text)
print("Has adminLogoutBtn:", 'adminLogoutBtn' in text)
print("Has displayActivePass:", 'displayActivePass' in text)

# Check closing tags around tab-profil
p = text.find('id="tab-profil"')
print("tab-profil to tab-berita slice:")
p_end = text.find('id="tab-berita"', p)
print(text[p_end-150:p_end+50])
