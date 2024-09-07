# Daftar test case
test_cases = [
    {"jam_kerja": 40, "pengeluaran": 600000, "expected_gaji": 600000, "expected_tabungan": "Tidak bisa menabung"},
    {"jam_kerja": 52, "pengeluaran": 600000, "expected_gaji": 840000, "expected_tabungan": "Bisa menabung", "expected_saving": 240000},
    {"jam_kerja": 30, "pengeluaran": 600000, "expected_gaji": 450000, "expected_tabungan": "Cari tambahan"},
    {"jam_kerja": 40, "pengeluaran": 600000, "expected_gaji": 600000, "expected_tabungan": "Tidak bisa menabung"},
    {"jam_kerja": 35, "pengeluaran": 600000, "expected_gaji": 525000, "expected_tabungan": "Cari tambahan"}
]
# Fungsi untuk menghitung gaji
def hitung_gaji(jam_kerja, gaji_per_jam=15000, jam_normal_per_minggu=40):
    if jam_kerja <= jam_normal_per_minggu:
        gaji = jam_kerja * gaji_per_jam
    else:
        gaji_normal = jam_normal_per_minggu * gaji_per_jam
        lembur = (jam_kerja - jam_normal_per_minggu) * (gaji_per_jam * 1.5)
        gaji = gaji_normal + lembur
    return gaji

# Fungsi untuk menjalankan test case
def run_tests():
    for idx, case in enumerate(test_cases):
        gaji = hitung_gaji(case["jam_kerja"])
        print(f"Test Case {idx+1}:")
        print(f"  Expected Gaji: {case['expected_gaji']}, Actual Gaji: {gaji}")
        if gaji == case['expected_gaji']:
            print("  Gaji Test: Passed")
        else:
            print("  Gaji Test: Failed")
        
        if gaji > case["pengeluaran"]:
            print("  Expected Tabungan: Bisa menabung")
            print(f"  Tabungan Test: Passed, Expected Saving: {case['expected_saving']}")
        elif gaji == case["pengeluaran"]:
            print(f"  Expected Tabungan: Tidak bisa menabung")
            print("  Tabungan Test: Failed")
        else:
            print(f"  Expected Tabungan: Cari tambahan")
            print("  Tabungan Test: Failed")
        print()

# Menjalankan test case
run_tests()
