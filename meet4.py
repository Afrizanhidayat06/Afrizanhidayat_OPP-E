# TUGAS MULTI-INHERITANCE & MULTILEVEL
# ===== CLASS PARENT =====
class Mhs_alumni:
    lulus = 2028  # atribut: tahun lulus


# class Mhs_aktif mewakili mahasiswa yang masih aktif
class Mhs_aktif:
    masuk = 2024  # atribut: tahun masuk


# ===== CLASS CHILD (MULTIPLE INHERITANCE

class DataMahasiswa(Mhs_alumni, Mhs_aktif):
    nama = "Afrizan"  # atribut tambahan khusus anak

    def tampil_data(self):
        # method untuk menampilkan data lengkap mahasiswa
        print(f"Nama: {self.nama}")
        print(f"Masuk tahun: {self.masuk}")
        print(f"Lulus tahun: {self.lulus}")


# ===== CLASS CHILD LAINNYA =====
# Semua class di bawah ini mewarisi dari DataMahasiswa

# class KTM mewakili kartu tanda mahasiswa
class KTM(DataMahasiswa):
    def tampil_ktm(self):
        print(f"KTM atas nama {self.nama} telah dicetak.")


# class Ijazah mewakili dokumen kelulusan
class Ijazah(DataMahasiswa):
    def tampil_ijazah(self):
        print(f"Ijazah {self.nama} telah diterbitkan pada tahun {self.lulus}.")


# class Beasiswa mewakili mahasiswa yang mendapat beasiswa
class Beasiswa(DataMahasiswa):
    def tampil_beasiswa(self):
        print(f"{self.nama} mendapatkan beasiswa prestasi dari kampus.")


# ===== CLASS MULTILEVEL INHERITANCE =====
# class MahasiswaSukses mewarisi dari Beasiswa
# Ini contoh pewarisan bertingkat (multilevel inheritance)
class MahasiswaSukses(Beasiswa):
    def tampil_sukses(self):
        print(f"{self.nama} sukses kuliah dan lulus pada tahun {self.lulus}!")


# ===== BAGIAN UTAMA PROGRAM =====
# Menjalankan semua class untuk menampilkan hasil pewarisan
print("=== DATA MAHASISWA ===")
mhs = DataMahasiswa()
mhs.tampil_data()

print("\n=== KTM ===")
k = KTM()
k.tampil_ktm()

print("\n=== IJAZAH ===")
i = Ijazah()
i.tampil_ijazah()

print("\n=== BEASISWA ===")
b = Beasiswa()
b.tampil_beasiswa()

print("\n=== MULTILEVEL INHERITANCE ===")
s = MahasiswaSukses()
s.tampil_sukses()
