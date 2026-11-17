import os
import zipfile
import shutil

workspace = r'c:\Users\acer\Documents\WEBSITE-SEKOLAH-SD INPRES ARSO 8'
out_zip_workspace = os.path.join(workspace, 'WEBSITE-SDN-INPRES-ARSO-8.zip')
out_zip_downloads = r'c:\Users\acer\Downloads\PAKET-WEBSITE-SDN-INPRES-ARSO-8-RESMI.zip'

exclude_dirs = {'.git', '.gemini', 'scratch', '__pycache__', '.pytest_cache'}
exclude_exts = {'.zip', '.tar', '.gz'}

def make_zip(dest_path):
    print(f"Creating ZIP at {dest_path}...")
    with zipfile.ZipFile(dest_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(workspace):
            # filter dirs in-place
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in exclude_exts:
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, workspace)
                zf.write(full_path, rel_path)
    size_mb = os.path.getsize(dest_path) / (1024 * 1024)
    print(f"Finished {dest_path}: {size_mb:.2f} MB")

# Remove old workspace zip before archiving
if os.path.exists(out_zip_workspace):
    try:
        os.remove(out_zip_workspace)
    except Exception as e:
        print("Note removing old zip:", e)

make_zip(out_zip_workspace)

# Copy to downloads
shutil.copy2(out_zip_workspace, out_zip_downloads)
print(f"Copied to {out_zip_downloads} successfully!")
