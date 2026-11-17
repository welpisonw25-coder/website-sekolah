import os
import sys
import time
import tarfile
import base64
import subprocess
import requests

TOKEN = "72f16e6af0b452667d066e97227ab450"
DOMAINS = ["sdninpresarso8.sch.id", "www.sdninpresarso8.sch.id", "sdninpresarso8.surge.sh"]

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
WATCH_EXTS = {'.html', '.css', '.js', '.json', '.txt', '.png', '.jpg', '.jpeg', '.svg'}
EXCLUDE_DIRS = {'.git', '.vscode', '__pycache__'}
EXCLUDE_FILES = {'website_deploy.tar.gz', 'website_deploy.zip', 'deploy_online.py', 'auto_sync_online.py', 'server_otomatis.py', 'WEBSITE-SDN-INPRES-ARSO-8.zip', 'temp_sync.tar.gz'}

def get_latest_state():
    latest_mtime = 0
    latest_file = ""
    for root, dirs, files in os.walk(CURRENT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            if f in EXCLUDE_FILES:
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext in WATCH_EXTS:
                fp = os.path.join(root, f)
                try:
                    mt = os.path.getmtime(fp)
                    if mt > latest_mtime:
                        latest_mtime = mt
                        latest_file = os.path.relpath(fp, CURRENT_DIR)
                except OSError:
                    pass
    return latest_mtime, latest_file

def deploy_to_internet():
    tar_output = os.path.join(CURRENT_DIR, "temp_sync.tar.gz")
    try:
        with tarfile.open(tar_output, "w:gz", format=tarfile.PAX_FORMAT) as tar:
            for root, dirs, files in os.walk(CURRENT_DIR):
                dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
                for file in files:
                    if file in EXCLUDE_FILES:
                        continue
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, CURRENT_DIR).replace("\\", "/")
                    tar.add(full_path, arcname=f"dist/{rel_path}")

        # Unggah ke semua domain resmi
        success_list = []
        for dom in DOMAINS:
            ok = False
            # Coba via curl.exe
            cmd = [
                'curl.exe', '-s', '-X', 'PUT',
                f'https://surge.surge.sh/{dom}',
                '-u', f'token:{TOKEN}',
                '-H', 'Content-Type: application/gzip',
                '-H', 'Accept: application/x-ndjson',
                '--data-binary', f'@{os.path.basename(tar_output)}'
            ]
            try:
                res = subprocess.run(cmd, cwd=CURRENT_DIR, capture_output=True, text=True, timeout=90)
                if res.returncode == 0 and 'error' not in res.stdout.lower() and 'failed' not in res.stdout.lower():
                    ok = True
            except Exception:
                pass

            if not ok:
                # Fallback requests
                try:
                    auth = base64.b64encode(f"token:{TOKEN}".encode("utf-8")).decode("utf-8")
                    headers = {
                        "Authorization": f"Basic {auth}",
                        "Content-Type": "application/gzip",
                        "Accept": "application/x-ndjson",
                        "User-Agent": "Surge/0.23.1"
                    }
                    with open(tar_output, "rb") as f:
                        resp = requests.put(f"https://surge.surge.sh/{dom}", data=f, headers=headers, timeout=60)
                    if resp.status_code == 200:
                        ok = True
                except Exception:
                    pass

            if ok:
                success_list.append(dom)

        if success_list:
            return True, f"Berhasil diunggah ke: {', '.join(success_list)}"
        return False, "Gagal mengunggah ke semua domain"
    except Exception as e:
        return False, str(e)
    finally:
        if os.path.exists(tar_output):
            try:
                os.remove(tar_output)
            except OSError:
                pass

def main():
    print("=" * 65)
    print("    PEMANTAU & PENGUNGGAH OTOMATIS KE INTERNET (SDN ARSO 8)")
    print("=" * 65)
    print(f"Domain Tujuan: https://sdninpresarso8.sch.id (dan seluruh domain resmi)")
    print("Status       : AKTIF MEMANTAU FOLDER...")
    print("\n⚡ CARA KERJA:")
    print("   Setiap kali Anda mengedit dan menyimpan file di Notepad atau editor lain,")
    print("   program akan OTOMATIS mengunggah perubahan ke domain resmi tanpa")
    print("   perlu Anda menekan tombol apa pun lagi!")
    print("=" * 65)
    print("💡 Biarkan jendela hitam ini tetap terbuka saat Anda sedang mengedit.")
    print("   Tekan Ctrl + C atau tutup jendela jika sudah selesai.\n")

    last_mtime, _ = get_latest_state()

    while True:
        try:
            time.sleep(1.5)
            curr_mtime, curr_file = get_latest_state()
            if curr_mtime > last_mtime:
                time.sleep(2.0)
                last_mtime, curr_file = get_latest_state()

                waktu = time.strftime("%H:%M:%S")
                print(f"[{waktu}] 📝 Perubahan terdeteksi pada '{curr_file}'...")
                print(f"[{waktu}] 🚀 Sedang mengunggah otomatis ke domain resmi...")

                success, msg = deploy_to_internet()
                waktu_selesai = time.strftime("%H:%M:%S")
                if success:
                    print(f"[{waktu_selesai}] 🎉 BERHASIL! Website online sudah terupdate otomatis!")
                    print(f"👉 https://sdninpresarso8.sch.id\n")
                else:
                    print(f"[{waktu_selesai}] ⚠️ Status: {msg}\n")
        except KeyboardInterrupt:
            print("\nPemantauan otomatis dihentikan.")
            break

if __name__ == '__main__':
    main()
