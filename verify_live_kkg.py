import urllib.request

url = 'https://sdninpresarso8.sch.id/pengembangan-guru.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8')
    print("HTTP Status:", resp.status)
    print("Has kkgShowcaseSliderWrapper:", 'kkgShowcaseSliderWrapper' in html)
    print("Has v=20261115_v47:", 'v=20261115_v47' in html)
    print("Has kkgShowcaseDotsBar:", 'kkgShowcaseDotsBar' in html)
