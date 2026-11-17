import requests
import json
import time

# 1. Fetch current Firebase berita
url_fb = 'https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah/berita.json'
r = requests.get(url_fb, timeout=10)
current_berita = r.json()
print("Current berita count in Firebase:", len(current_berita))

# 2. Add a test berita to Firebase
test_item = {
    "id": int(time.time()),
    "judul": "Uji Coba Publikasi Berita Otomatis Realtime Tanpa File Bat",
    "kategori": "Teknologi & ANBK",
    "penulis": "Admin Otomatis",
    "tanggal": "15 November 2026",
    "foto": "images/gapura-kehormatan.jpg",
    "snippet": "Berita ini membuktikan sistem publikasi berita online otomatis langsung tayang seketika.",
    "isi": "Isi lengkap berita uji coba otomatis langsung tayang ke publik."
}

updated_berita = [test_item] + current_berita
print("Pushing updated berita to Firebase...")
r_put = requests.put(url_fb, json=updated_berita, timeout=10)
print("PUT status:", r_put.status_code)

# 3. Now simulate a public visitor fetching data_sekolah.json from Firebase (which main.js does!)
r_get_all = requests.get('https://arso8-a2bcf-default-rtdb.firebaseio.com/data_sekolah.json?t=' + str(int(time.time())), timeout=10)
cloud_db = r_get_all.json()
news_in_cloud = cloud_db.get('berita', [])
print("News in cloud now:", len(news_in_cloud))
print("First item in cloud:", news_in_cloud[0].get('judul'))

# 4. Clean up test item
print("Cleaning up test item...")
requests.put(url_fb, json=current_berita, timeout=10)
print("Cleaned up successfully!")
