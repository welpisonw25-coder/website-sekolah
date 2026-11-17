import subprocess, os, requests, base64

TOKEN = "72f16e6af0b452667d066e97227ab450"
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Check if website_deploy.tar.gz was deleted; if so recreate it
import tarfile
tar_path = "website_deploy.tar.gz"

EXCLUDE_DIRS = {".git", ".vscode", "__pycache__", "scratch", ".gemini"}
EXCLUDE_FILES = {
    "website_deploy.tar.gz", "website_deploy.zip", "deploy_online.py",
    "KLIK_UNTUK_UPDATE_ONLINE.bat", "auto_sync_online.py", "server_otomatis.py",
    "WEBSITE-SDN-INPRES-ARSO-8.zip"
}

with tarfile.open(tar_path, "w:gz", format=tarfile.PAX_FORMAT) as tar:
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file in EXCLUDE_FILES or file.endswith(".tar.gz") or file.endswith(".zip"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
            tar.add(full_path, arcname=f"dist/{rel_path}")

print("Tar created, size:", os.path.getsize(tar_path))

domains = ["sdninpresarso8.sch.id", "www.sdninpresarso8.sch.id", "sdninpresarso8.surge.sh"]
auth = base64.b64encode(f"token:{TOKEN}".encode("utf-8")).decode("utf-8")
headers = {
    "Authorization": f"Basic {auth}",
    "Content-Type": "application/gzip",
    "Accept": "application/x-ndjson",
    "User-Agent": "Surge/0.23.1"
}

for dom in domains:
    print(f"Uploading to {dom}...")
    try:
        with open(tar_path, "rb") as f:
            resp = requests.put(f"https://surge.surge.sh/{dom}", data=f, headers=headers, timeout=60)
        print(f" -> {dom}: HTTP {resp.status_code}")
    except Exception as e:
        print(f" -> {dom} error: {e}")

if os.path.exists(tar_path):
    os.remove(tar_path)
