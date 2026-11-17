import subprocess, os, tarfile

TOKEN = "72f16e6af0b452667d066e97227ab450"
TAR_OUTPUT = "website_deploy.tar.gz"

EXCLUDE_DIRS = {".git", ".vscode", "__pycache__", "scratch", ".gemini"}
EXCLUDE_FILES = {
    "website_deploy.tar.gz", "website_deploy.zip", "deploy_online.py",
    "KLIK_UNTUK_UPDATE_ONLINE.bat", "auto_sync_online.py", "server_otomatis.py",
    "WEBSITE-SDN-INPRES-ARSO-8.zip"
}

with tarfile.open(TAR_OUTPUT, "w:gz", format=tarfile.PAX_FORMAT) as tar:
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file in EXCLUDE_FILES or file.endswith(".tar.gz") or file.endswith(".zip"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
            tar.add(full_path, arcname=f"dist/{rel_path}")

print("Tar created, size:", os.path.getsize(TAR_OUTPUT))

for dom in ["sdninpresarso8.sch.id", "www.sdninpresarso8.sch.id", "sdninpresarso8.surge.sh"]:
    cmd = [
        'curl.exe', '-s', '-S', '-X', 'PUT',
        f'https://surge.surge.sh/{dom}',
        '-u', f'token:{TOKEN}',
        '-H', 'Content-Type: application/gzip',
        '-H', 'Accept: application/x-ndjson',
        '--data-binary', f'@{TAR_OUTPUT}'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    print(f"Uploaded to {dom}: exit code {res.returncode}")
    if res.stdout:
        print(f"  Output: {res.stdout.strip()[:100]}")

if os.path.exists(TAR_OUTPUT):
    os.remove(TAR_OUTPUT)

print("All done!")
