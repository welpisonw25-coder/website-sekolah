import os
import shutil

copy_dir = r'c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8 - Copy'
dest_dir = r'c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8'

copy_images_dir = os.path.join(copy_dir, 'images')
dest_images_dir = os.path.join(dest_dir, 'images')

print("Syncing missing images from Copy to active workspace...")
for f in os.listdir(copy_images_dir):
    src_file = os.path.join(copy_images_dir, f)
    dst_file = os.path.join(dest_images_dir, f)
    if not os.path.exists(dst_file):
        shutil.copy2(src_file, dst_file)
        print(f"Copied missing: images/{f}")
    else:
        # Check if dst is smaller or empty
        if os.path.getsize(dst_file) == 0:
            shutil.copy2(src_file, dst_file)
            print(f"Replaced empty: images/{f}")

print("\nCurrent files in active images/:")
for f in sorted(os.listdir(dest_images_dir)):
    size = os.path.getsize(os.path.join(dest_images_dir, f))
    print(f"- {f} ({size:,} bytes)")
