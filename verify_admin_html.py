with open('admin.html', 'r', encoding='utf-8') as f:
    c = f.read()

checks = [
    'cardKKGProfilManager',
    'kkgSekretariatInput',
    'kkgKetuaInput',
    'kkgNIPKetuaInput',
    'kkgWaktuInput',
    'kkgDasarSKInput',
    'k3sProgramsInput',
    'kkgKelAJudul',
    'kkgKelACakupan',
    'kkgKelAPrograms',
    'kkgKelBJudul',
    'kkgKelBCakupan',
    'kkgKelBPrograms',
    'btnSimpanKKGProfil',
    'btnResetKKGProfil',
    'sopTatibGuruInput',
    'sopTatibSiswaInput',
    'btnSimpanSOPTatib',
    'sopPiket_senin_1',
    'sopPiket_jumat_2',
    'btnSimpanSOPPiket',
    'sopSeragam_m1_senin',
    'sopSeragam_m5_jumat',
    'btnSimpanSOPSeragam',
    'sopPramukaJadwalInput',
    'sopPramukaSiagaInput',
    'sopPramukaPenggalangInput',
    'btnSimpanSOPPramuka'
]

missing = [x for x in checks if x not in c]
print("Missing checks in admin.html:", missing if missing else "None! All elements found!")
