# -*- coding: utf-8 -*-
import urllib.request
import time

def check(url, expected, should_not_contain=None):
    t_url = url + ('&' if '?' in url else '?') + 't=' + str(int(time.time()))
    req = urllib.request.Request(t_url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            ok = True
            if expected and expected not in content:
                ok = False
                print(f"[FAIL] {url} did not contain '{expected[:40]}'")
            if should_not_contain and should_not_contain in content:
                ok = False
                print(f"[FAIL] {url} unexpectedly contained '{should_not_contain[:40]}'")
            if ok:
                print(f"[PASS] {url}")
    except Exception as e:
        print(f"[ERROR] {url}: {e}")

check('https://sdninpresarso8.sch.id/index.html', 'v=20261115_v38')
check('https://sdninpresarso8.sch.id/index.html', 'Pemanfaatan Jaringan Starlink')
check('https://sdninpresarso8.sch.id/js/main.js', 'v=20261115_v38', '_baseSlide0Html')
check('https://sdninpresarso8.sch.id/images/kegiatan-anbk-komputer.jpg', '')
