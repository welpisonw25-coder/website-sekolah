# -*- coding: utf-8 -*-
import urllib.request
import time

def check_live(url, needle):
    req = urllib.request.Request(url + '?t=' + str(int(time.time())), headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        found = needle in content
        print(f"[{'PASS' if found else 'FAIL'}] {url} -> '{needle[:30]}'")

check_live('https://sdninpresarso8.sch.id/index.html', 'homePengumumanGrid')
check_live('https://sdninpresarso8.sch.id/index.html', 'v=20261115_v36')
check_live('https://sdninpresarso8.sch.id/pengumuman.html', 'pengumumanList')
check_live('https://sdninpresarso8.sch.id/js/main.js', 'renderShowcaseSlides')
check_live('https://sdninpresarso8.sch.id/js/main.js', 'homePengumumanGrid')
check_live('https://sdninpresarso8.sch.id/js/admin.js', 'window.SDN_DATABASE.pengumuman')
