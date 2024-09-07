# Fungsi untuk menghitung gaji
def hitung_gaji(jam_kerja, gaji_per_jam=15000, jam_normal_per_minggu=40):
    if jam_kerja <= jam_normal_per_minggu:
        gaji = jam_kerja * gaji_per_jam
    else:
        gaji_normal = jam_normal_per_minggu * gaji_per_jam
        lembur = (jam_kerja - jam_normal_per_minggu) * (gaji_per_jam * 1.5)
        gaji = gaji_normal + lembur
    return gaji

# Fungsi untuk mengevaluasi tabungan
def evaluasi_tabungan(gaji, pengeluaran):
    if gaji > pengeluaran:
        print("Bisa menabung")
        tabungan = gaji - pengeluaran
        print(f"Tabungan: Rp. {tabungan}")
    elif gaji == pengeluaran:
        print("Tidak bisa menabung")
    else:
        print("Cari tambahan")

# Input variatif
jam_kerja = 52  # Mr. John bekerja 52 jam minggu ini
pengeluaran = 600000  # Pengeluaran Mr. John

# Menghitung gaji
gaji = hitung_gaji(jam_kerja)

# Mencetak gaji
print(f"Gaji minggu ini: Rp. {gaji}")

# Mengevaluasi apakah bisa menabung atau tidak
evaluasi_tabungan(gaji, pengeluaran)

