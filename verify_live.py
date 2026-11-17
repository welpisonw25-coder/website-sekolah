# -*- coding: utf-8 -*-
import urllib.request
import time

def check_url(url, needle):
    req = urllib.request.Request(url + '?t=' + str(int(time.time())), headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        found = needle in content
        print(f"Checking {url}: {'[OK] FOUND' if found else '[FAIL] NOT FOUND'}")

check_url('https://sdninpresarso8.sch.id/js/main.js', 'window.refreshDataFromCloud')
check_url('https://sdninpresarso8.sch.id/js/admin.js', 'rootPayload')
check_url('https://sdninpresarso8.sch.id/admin.html', 'fileProtocolWarning')
check_url('https://sdninpresarso8.sch.id/index.html', 'v=20261115_v35')
