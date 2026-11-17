import os
import glob

print("ZIP files in workspace:")
for z in glob.glob('*.zip'):
    print(f"- {z}: {os.path.getsize(z)} bytes")

downloads_dir = r'c:\Users\acer\Downloads'
print("\nZIP files in Downloads:")
for z in glob.glob(os.path.join(downloads_dir, '*.zip')):
    if 'arso' in z.lower() or 'paket' in z.lower() or 'website' in z.lower():
        print(f"- {z}: {os.path.getsize(z)} bytes")
