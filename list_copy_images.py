import os

copy_images = r'c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8 - Copy\images'
if os.path.exists(copy_images):
    for f in os.listdir(copy_images):
        full = os.path.join(copy_images, f)
        size = os.path.getsize(full)
        print(f"Copy image: {f} ({size:,} bytes)")
else:
    print("Folder does not exist")
