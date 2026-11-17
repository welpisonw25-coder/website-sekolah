import os
import sys
import tarfile
import base64
import subprocess
import requests

TOKEN = "72f16e6af0b452667d066e97227ab450"
TARGET_DOMAINS = ["sdninpresarso8.sch.id", "www.sdninpresarso8.sch.id", "sdninpresarso8.surge.sh"]

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TAR_OUTPUT = os.path.join(CURRENT_DIR, "website_deploy.tar.gz")

print("=" * 60)
print("  MEMPERBARUI WEBSITE RESMI SDN INPRES ARSO VIII KE INTERNET")
print("=" * 60)
print("\n[1/3] Mengompresi file website...")

EXCLUDE_DIRS = {".git", ".vscode", "__pycache__", "scratch", ".gemini"}
EXCLUDE_FILES = {
    "website_deploy.tar.gz", "website_deploy.zip", "deploy_online.py",
    "KLIK_UNTUK_UPDATE_ONLINE.bat", "auto_sync_online.py", "server_otomatis.py",
    "WEBSITE-SDN-INPRES-ARSO-8.zip"
}

file_count = 0
with tarfile.open(TAR_OUTPUT, "w:gz", format=tarfile.PAX_FORMAT) as tar:
    for root, dirs, files in os.walk(CURRENT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file in EXCLUDE_FILES or file.endswith(".tar.gz") or file.endswith(".zip"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, CURRENT_DIR).replace("\\", "/")
            tar.add(full_path, arcname=f"dist/{rel_path}")
            file_count += 1

tar_size = os.path.getsize(TAR_OUTPUT)
print(f" -> Berhasil mengemas {file_count} file ({tar_size:,} bytes).")

print("\n[2/3] Mengunggah pembaruan ke server domain resmi...")

success_count = 0
auth = base64.b64encode(f"token:{TOKEN}".encode("utf-8")).decode("utf-8")
headers = {
    "Authorization": f"Basic {auth}",
    "Content-Type": "application/gzip",
    "Accept": "application/x-ndjson",
    "User-Agent": "Surge/0.23.1"
}

for dom in TARGET_DOMAINS:
    uploaded = False
    # Coba via curl.exe (sangat cepat dan andal)
    try:
        cmd = [
            'curl.exe', '-s', '-S', '-X', 'PUT',
            f'https://surge.surge.sh/{dom}',
            '-u', f'token:{TOKEN}',
            '-H', 'Content-Type: application/gzip',
            '-H', 'Accept: application/x-ndjson',
            '--data-binary', f'@{os.path.basename(TAR_OUTPUT)}'
        ]
        res = subprocess.run(cmd, cwd=CURRENT_DIR, capture_output=True, text=True, timeout=120)
        if res.returncode == 0 and ('available' in res.stdout or 'progress' in res.stdout or 'cdn' in res.stdout):
            uploaded = True
            print(f" -> Berhasil diunggah ke: {dom}")
    except Exception:
        pass

    # Fallback requests jika curl tidak merespons
    if not uploaded:
        for attempt in range(1, 3):
            try:
                with open(TAR_OUTPUT, "rb") as f:
                    resp = requests.put(f"https://surge.surge.sh/{dom}", data=f, headers=headers, timeout=120)
                if resp.status_code == 200:
                    uploaded = True
                    print(f" -> Berhasil diunggah ke: {dom}")
                    break
            except Exception:
                pass

    if uploaded:
        success_count += 1

if os.path.exists(TAR_OUTPUT):
    try:
        os.remove(TAR_OUTPUT)
    except OSError:
        pass

if success_count > 0:
    print("\n[3/3] SELESAI DENGAN SUKSES! 🎉")
    print("=" * 60)
    print("Website resmi SDN Inpres Arso VIII sudah aktif live di internet:")
    print("👉 https://sdninpresarso8.sch.id (Domain Utama Resmi)")
    print("👉 https://www.sdninpresarso8.sch.id (Subdomain www)")
    print("=" * 60)
else:
    print("\n❌ Gagal mengunggah ke server. Silakan periksa koneksi internet.")
    sys.exit(1)
