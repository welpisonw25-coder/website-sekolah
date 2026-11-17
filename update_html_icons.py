import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f"Updating icons in {len(html_files)} HTML files...")

icon_block = """    <!-- Favicon & Mobile Touch Icons Resmi SDN Inpres Arso VIII -->
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="192x192" href="images/logo-keerom-192.png">
    <link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon-180.png">
    <link rel="apple-touch-icon" href="apple-touch-icon.png">
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#0d5c3a">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-title" content="SDN Arso VIII">"""

for fname in html_files:
    if fname.startswith('google') or fname.startswith('surat'):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove existing rel="icon" or rel="manifest" or rel="apple-touch-icon"
    content = re.sub(r'\s*<!-- Favicon.*?-->', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<link rel="icon"[^>]*>', '', content)
    content = re.sub(r'\s*<link rel="apple-touch-icon"[^>]*>', '', content)
    content = re.sub(r'\s*<link rel="manifest"[^>]*>', '', content)

    # Insert icon block right before </head> or after <meta name="viewport"...>
    if '</head>' in content:
        content = content.replace('</head>', f"{icon_block}\n</head>", 1)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated icons in {fname}")

print("All HTML files updated with official touch icons!")
