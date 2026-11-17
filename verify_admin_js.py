with open('js/admin.js', 'r', encoding='utf-8') as f:
    code = f.read()

checks = [
    'defaultSOPData',
    'getSOPData',
    'saveSOPData',
    'initSOPManager',
    'populateSOPTeacherDropdowns',
    'syncGuruWithSOP',
    'btnSimpanKKGProfil',
    'btnResetKKGProfil',
    'btnSimpanSOPTatib',
    'btnSimpanSOPPiket',
    'btnSimpanSOPSeragam',
    'btnSimpanSOPPramuka'
]

for chk in checks:
    print(f"{chk}: {chk in code}")

print(f"Total lines in js/admin.js: {len(code.splitlines())}")
