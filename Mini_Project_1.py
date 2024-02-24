class Kamera:
    kode_kamera = 0
    def __init__(self, Brand, Model, Tahun, Resolusi, Harga):
        Kamera.kode_kamera += 1
        self.kode = Kamera.kode_kamera
        self.Brand = Brand
        self.Model = Model 
        self.Tahun = Tahun 
        self.Resolusi = Resolusi
        self.Harga = Harga

class SistemRekomendasiKamera:
    def __init__(self):
        self.kamera = []

        self.tambah_kamera("Canon", "1300D", 2016, 18, 5000000)

    def tambah_kamera(self, Brand, Model, Tahun, Resolusi, Harga):
        kamera = Kamera(Brand, Model, Tahun, Resolusi, Harga)
        self.kamera.append(kamera)
        print("Kamera telah berhasil ditambahkan")

    def hapus_kamera(self, kode):
        for kamera in self.kamera:
            if kamera.kode == kode:
                self.kamera.remove(kamera)
                print("Kamera berhasil dihapus")
                return
        print("Kamera tidak ditemukan")

    def edit_kamera(self,kode, Brand, Model, Tahun, Resolusi, Harga):
        for kamera in self.kamera:
            if kamera.kode == kode:
                if Brand:
                    kamera.Brand = Brand
                if Model:
                    kamera.Model = Model 
                if Resolusi:
                    kamera.Resolusi = Resolusi
                if Tahun:
                    kamera.Tahun = Tahun 
                if Harga:
                    kamera.Harga = Harga
                print("Kamera berhasil diedit")
                return
        print("Kamera tidak ditemukan")

    def list_kamera(self):
        if not self.kamera:
            print("Daftar kamera belum tersedia\n")
        else:
            print("Daftar Kamera:\n")
            for kamera in self.kamera:
                print(f"Kode: {kamera.kode}\nBrand: {kamera.Brand}\nModel: {kamera.Model}\nTahun: {kamera.Tahun}\nResolusi: {kamera.Resolusi} MP\nHarga: Rp {kamera.Harga:,}\n")

if __name__ == "__main__":
    sistem_rekomendasi = SistemRekomendasiKamera()

    while True:
        print("[===---Rekomendasi Kamera 2024---===]\n")
        print("1. Lihat Rekomendasi Kamera")
        print("2. Tambah Kamera")
        print("3. Edit Kamera")
        print("4. Hapus Kamera")
        print("5. Tutup Program\n")
    
        pilih = input("Pilih Menu : ")
        if pilih == "1":
            print()
            sistem_rekomendasi.list_kamera()
        elif pilih == "2":
            Brand = input("Masukkan Brand : ")
            Model = input("Masukkan Model : ")
            Tahun = int(input("Masukkan Tahun : "))
            Resolusi = int(input("Masukkan Resolusi (MP) : "))
            Harga = int(input("Masukkan Harga : "))
            sistem_rekomendasi.tambah_kamera(Brand, Model, Tahun, Resolusi, Harga)
        elif pilih == "3":
            sistem_rekomendasi.list_kamera()
            kode = int(input("Masukkan kode kamera yang ingin di update : "))
            Brand = input("Masukkan Brand (klik enter skip): ")
            Model = input("Masukkan Model (klik enter untuk skip): ")
            Resolusi = int(input("Masukkan Resolusi (klik enter untuk skip): ") or 0)
            Tahun = int(input("Masukkan Tahun (klik enter untuk skip): ") or 0)
            Harga = int(input("Masukkan Harga (klik enter untuk skip): ") or 0)
            sistem_rekomendasi.edit_kamera(kode, Brand, Model, Tahun, Resolusi, Harga)
        elif pilih == "4":
            sistem_rekomendasi.list_kamera()
            kode = int(input("Masukkan kode kamera yang ingin dihapus : "))
            sistem_rekomendasi.hapus_kamera(kode)
        elif pilih == "5":
            print("Terima Kasih")
            break
        else:
            print("Pilihan tidak tersedia, Silakan pilih menu kembali.")
