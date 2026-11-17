import shutil
import os

mappings = {
    'images/kegiatan-literasi-komputer.jpg': 'images/kegiatan-anbk-komputer.jpg',
    'images/kegiatan-belajar-kelas.jpg': 'images/kegiatan-anbk-komputer.jpg',
    'images/kegiatan-evaluasi-guru.jpg': 'images/kegiatan-rapat-dewan-guru.jpg',
    'images/kegiatan-pramuka-kelas.jpg': 'images/kegiatan-pramuka-budaya.jpg',
    'images/kegiatan-kebersamaan-guru.jpg': 'images/dewan-guru.jpg',
    'images/kegiatan-kerja-bakti.jpg': 'images/kegiatan-senam-bersama.jpg'
}

for dest, src in mappings.items():
    if os.path.exists(src) and not os.path.exists(dest):
        shutil.copyfile(src, dest)
        print(f"Copied {src} -> {dest}")
    elif os.path.exists(dest):
        print(f"{dest} already exists")
    else:
        print(f"Source {src} not found!")

print("All missing image aliases fixed!")
