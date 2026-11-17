import os

print("Files in images/:")
files = os.listdir('images')
for f in files:
    size = os.path.getsize(os.path.join('images', f))
    print(f"- {f} ({size:,} bytes)")
