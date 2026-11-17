import os
import sys
import time
import json
import webbrowser
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from sync_engine import save_data_payload, _trigger_background_deploy

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
WATCH_EXTS = {'.html', '.css', '.js', '.json', '.txt', '.png', '.jpg', '.jpeg', '.svg'}
EXCLUDE_DIRS = {'.git', '.vscode', '__pycache__'}
EXCLUDE_SYNC_FILES = {'data_sekolah.json', 'data_sekolah.js', 'temp_sync.tar.gz', 'website_deploy.tar.gz'}

def get_latest_mtime():
    latest_mtime = 0
    latest_file = ""
    for root, dirs, files in os.walk(CURRENT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
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

LIVE_RELOAD_SCRIPT = """
<!-- LIVE AUTO-RELOAD INJECTION -->
<script id="__live_reload_script">
(function() {
    let lastMTime = null;
    function checkChanges() {
        fetch('/__poll_changes?last=' + (lastMTime || 0))
            .then(res => res.json())
            .then(data => {
                if (lastMTime !== null && data.modified) {
                    console.log('[LiveReload] Perubahan terdeteksi pada:', data.file, 'Memuat ulang...');
                    window.location.reload();
                } else {
                    lastMTime = data.latest_mtime;
                    setTimeout(checkChanges, 700);
                }
            })
            .catch(() => {
                setTimeout(checkChanges, 1500);
            });
    }
    checkChanges();
})();
</script>
</body>
"""

class LiveReloadHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=CURRENT_DIR, **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path.startswith('/api/sync_data'):
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                payload = json.loads(post_data.decode('utf-8'))
                cat = payload.get('category', 'all')
                data = payload.get('data')

                save_data_payload(cat, data)

                res = json.dumps({
                    "success": True,
                    "message": "Perubahan berhasil disimpan & otomatis dikirim ke internet https://sdninpresarso8.sch.id"
                }).encode('utf-8')

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(res)
                return
            except Exception as e:
                res = json.dumps({"success": False, "error": str(e)}).encode('utf-8')
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(res)
                return

        self.send_response(404)
        self.end_headers()

    def do_GET(self):
        # Handle live reload polling
        if self.path.startswith('/__poll_changes'):
            query = self.path.split('?', 1)
            client_time = 0.0
            if len(query) > 1:
                params = dict(p.split('=', 1) for p in query[1].split('&') if '=' in p)
                try:
                    client_time = float(params.get('last', 0))
                except ValueError:
                    client_time = 0.0

            latest_mtime, latest_file = get_latest_mtime()
            modified = (client_time > 0 and (latest_mtime - client_time) > 0.5)

            data = json.dumps({
                "modified": modified,
                "latest_mtime": latest_mtime,
                "file": latest_file
            }).encode('utf-8')

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        # Serve files normally, but if HTML, inject live reload script
        path_clean = self.path.split('?')[0].split('#')[0]
        if path_clean == '/' or path_clean.endswith('.html'):
            target_file = 'index.html' if path_clean == '/' else path_clean.lstrip('/')
            full_path = os.path.join(CURRENT_DIR, target_file)
            if os.path.exists(full_path) and os.path.isfile(full_path):
                try:
                    with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                        html_content = f.read()

                    # Inject script before </body>
                    if '</body>' in html_content:
                        html_content = html_content.replace('</body>', LIVE_RELOAD_SCRIPT, 1)
                    else:
                        html_content += LIVE_RELOAD_SCRIPT

                    encoded = html_content.encode('utf-8')
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                    self.send_header('Content-Length', str(len(encoded)))
                    self.end_headers()
                    self.wfile.write(encoded)
                    return
                except Exception:
                    pass

        # Standard file serving for css, js, images, etc.
        super().do_GET()

    def log_message(self, format, *args):
        # Mute normal poll request logs to keep console clean
        if '/__poll_changes' not in (args[0] if args else ''):
            sys.stdout.write(f"[{time.strftime('%H:%M:%S')}] {args[0]}\n")

def background_file_watcher():
    """Memantau jika ada file HTML/CSS/Gambar diubah langsung di folder, lalu auto-upload ke Surge"""
    last_mtime, _ = get_latest_mtime()
    while True:
        try:
            time.sleep(2.5)
            curr_mtime, curr_file = get_latest_mtime()
            if curr_mtime > last_mtime:
                last_mtime = curr_mtime
                fname = os.path.basename(curr_file)
                # Lewati jika file sinkronisasi internal (sudah ditangani langsung oleh sync_engine)
                if fname not in EXCLUDE_SYNC_FILES:
                    print(f"[{time.strftime('%H:%M:%S')}] 📝 Perubahan file '{curr_file}' terdeteksi...")
                    _trigger_background_deploy()
        except Exception:
            pass

def start_server():
    port = 8001
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, LiveReloadHandler)
    url = f"http://localhost:{port}"

    print("=" * 65)
    print("      SERVER OTOMATIS WEBSITE SDN INPRES ARSO VIII")
    print("=" * 65)
    print(f"\n🌐 Website aktif dibuka di browser:")
    print(f"👉 {url}")
    print("\n⚡ FITUR AUTO-SYNC KE INTERNET & AUTO-RELOAD AKTIF:")
    print("   Setiap kali Anda mengedit berita, foto, atau pengumuman")
    print("   di halaman admin, sistem akan OTOMATIS mengunggahnya")
    print("   ke internet resmi (https://sdninpresarso8.sch.id)!")
    print("   Perubahan seketika langsung terlihat di HP dan semua pengunjung.")
    print("=" * 65)
    print("💡 Biarkan jendela ini terbuka saat Anda mengelola website.")
    print("=" * 65 + "\n")

    # Jalankan watcher di background
    watcher_thread = threading.Thread(target=background_file_watcher, daemon=True)
    watcher_thread.start()

    # Buka browser otomatis
    threading.Timer(1.2, lambda: webbrowser.open(url)).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer otomatis dihentikan.")
        httpd.server_close()

if __name__ == '__main__':
    start_server()
