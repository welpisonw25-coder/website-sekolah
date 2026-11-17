# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace gerbang-sekolah.jpg in slide 5 with kegiatan-rapat-dewan-guru.jpg
target = '<img src="images/gerbang-sekolah.jpg" alt="Rapat Koordinasi Dewan Guru & Kepala Sekolah Tingkatkan Kualitas Belajar"'
replacement = '<img src="images/kegiatan-rapat-dewan-guru.jpg" alt="Rapat Koordinasi Dewan Guru & Kepala Sekolah Tingkatkan Kualitas Belajar"'

if target in html:
    html = html.replace(target, replacement)
    print("Replaced slide 5 image in index.html")

target_btn = "window.openLightboxWith('images/gerbang-sekolah.jpg', 'Rapat Koordinasi"
replacement_btn = "window.openLightboxWith('images/kegiatan-rapat-dewan-guru.jpg', 'Rapat Koordinasi"
if target_btn in html:
    html = html.replace(target_btn, replacement_btn)
    print("Replaced slide 5 lightbox target in index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
