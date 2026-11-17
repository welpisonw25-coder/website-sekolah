import os
import glob
import zipfile

search_dirs = [
    r'c:\Users\acer\Documents',
    r'c:\Users\acer\Downloads',
    r'C:\Users\acer\.gemini\antigravity\brain'
]

print("Searching for logo-keerom or logo files...")
for d in search_dirs:
    for root, dirs, files in os.walk(d):
        for f in files:
            if any(k in f.lower() for k in ['logo-keerom', 'keerom', 'tutwuri']):
                full = os.path.join(root, f)
                try:
                    size = os.path.getsize(full)
                    print(f"Found: {full} ({size} bytes)")
                except:
                    pass

print("\nSearching inside ZIP files in Downloads...")
for zpath in glob.glob(r'c:\Users\acer\Downloads\*.zip'):
    try:
        with zipfile.ZipFile(zpath, 'r') as zf:
            for name in zf.namelist():
                if any(k in name.lower() for k in ['logo-keerom', 'keerom', 'tutwuri', 'logo']):
                    print(f"Inside {os.path.basename(zpath)}: {name}")
    except:
        pass
