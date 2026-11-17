# -*- coding: utf-8 -*-
import os
import json
import threading
import time
from auto_sync_online import deploy_to_internet

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(CURRENT_DIR, "data_sekolah.json")
JS_DATA_FILE = os.path.join(CURRENT_DIR, "js", "data_sekolah.js")

_deploy_lock = threading.Lock()
_deploy_pending = False
_deploy_timer = None

def load_all_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[SYNC] Gagal membaca data_sekolah.json: {e}")
    return {}

def _trigger_background_deploy():
    global _deploy_pending
    with _deploy_lock:
        if _deploy_pending:
            return
        _deploy_pending = True

    def run_deploy():
        global _deploy_pending
        time.sleep(1.0) # Debounce 1 detik agar hemat bandwidth & tidak bentrok jika multi-save
        print("\n" + "=" * 60)
        print("🚀 [AUTO-SYNC] Mengunggah pembaruan terbaru ke https://sdninpresarso8.sch.id...")
        print("=" * 60)
        ok, msg = deploy_to_internet()
        if ok:
            print("✅ [AUTO-SYNC SUKSES] Perubahan sudah aktif LIVE di internet!")
            print("👉 https://sdninpresarso8.sch.id (Bisa langsung dibuka di HP)")
        else:
            print(f"❌ [AUTO-SYNC GAGAL] {msg}")
        print("=" * 60 + "\n")
        with _deploy_lock:
            _deploy_pending = False

    t = threading.Thread(target=run_deploy, daemon=True)
    t.start()

def save_data_payload(category, data):
    all_data = load_all_data()
    
    if category == 'all' and isinstance(data, dict):
        all_data.update(data)
    else:
        all_data[category] = data

    # 1. Tulis ke data_sekolah.json
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[SYNC] Error writing JSON: {e}")
        return False

    # 2. Tulis ke js/data_sekolah.js (agar langsung terbaca sinkron di HP tanpa fetch delay)
    try:
        with open(JS_DATA_FILE, "w", encoding="utf-8") as f:
            f.write("// DATABASE TERPUSAT SDN INPRES ARSO VIII (OTOMATIS TERSINKRONISASI)\n")
            f.write("window.SDN_DATABASE = " + json.dumps(all_data, ensure_ascii=False, indent=2) + ";\n")
    except Exception as e:
        print(f"[SYNC] Error writing JS: {e}")

    # 3. Trigger pengunggahan otomatis ke Surge
    _trigger_background_deploy()
    return True
