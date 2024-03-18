class Node:
    def __init__(self, kamera=None):
        self.kamera = kamera
        self.next = None

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
        self.head = None

        self.tambah_kamera("Canon", "1300D", 2016, 18, 5000000)
        self.tambah_kamera("Nikon", "D5300", 2016, 23, 7000000)
        self.tambah_kamera("Lumix", "GH5", 2019, 26, 15000000)
        self.tambah_kamera("Fujifilm", "XT3", 2020, 25, 15000000)

    def tambah_kamera(self, Brand, Model, Tahun, Resolusi, Harga):
        kamera = Kamera(Brand, Model, Tahun, Resolusi, Harga)
        node_kamera = Node(kamera)
        if not self.head:
            self.head = node_kamera
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_kamera
        print("Kamera berhasil ditambahkan")

    def tambah_kamera_di_awal(self, Brand, Model, Tahun, Resolusi, Harga):
        kamera = Kamera(Brand, Model, Tahun, Resolusi, Harga)
        node_kamera = Node(kamera)
        node_kamera.next = self.head
        self.head = node_kamera
        print("Kamera berhasil ditambahkan di awal")

    def tambah_kamera_di_akhir(self, Brand, Model, Tahun, Resolusi, Harga):
        kamera = Kamera(Brand, Model, Tahun, Resolusi, Harga)
        node_kamera = Node(kamera)
        if not self.head:
            self.head = node_kamera
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node_kamera
        print("Kamera berhasil ditambahkan di akhir")

    def tambah_kamera_di_antara(self, posisi, Brand, Model, Tahun, Resolusi, Harga):
        kamera = Kamera(Brand, Model, Tahun, Resolusi, Harga)
        node_kamera = Node(kamera)
        current = self.head
        while current:
            if current.kamera.kode == posisi:
                node_kamera.next = current.next
                current.next = node_kamera
                print("Kamera berhasil ditambahkan di antara")
                return
            current = current.next
        print("Posisi tidak ditemukan")

    def hapus_kamera(self, kode):
        current = self.head
        if current and current.kamera.kode == kode:
            self.head = current.next
            print("Kamera berhasil dihapus")
            return
        prev = None
        while current:
            if current.kamera.kode == kode:
                prev.next = current.next
                print("Kamera berhasil dihapus")
                return
            prev = current
            current = current.next
        print("Kamera tidak ditemukan")

    def hapus_kamera_di_awal(self):
        if not self.head:
            print("Linked list kosong")
            return
        self.head = self.head.next
        print("Kamera di awal berhasil dihapus")

    def hapus_kamera_di_akhir(self):
        if not self.head:
            print("Linked list kosong")
            return
        if not self.head.next:
            self.head = None
            print("Kamera di akhir berhasil dihapus")
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        print("Kamera di akhir berhasil dihapus")

    def hapus_kamera_di_antara(self, posisi):
        if not self.head:
            print("Linked list kosong")
            return
        current = self.head
        if current and current.kamera.kode == posisi:
            self.head = current.next
            print("Kamera di antara berhasil dihapus")
            return
        prev = None
        while current:
            if current.kamera.kode == posisi:
                prev.next = current.next
                print("Kamera di antara berhasil dihapus")
                return
            prev = current
            current = current.next
        print("Posisi tidak ditemukan")

    def edit_kamera(self, kode, Brand=None, Model=None, Tahun=None, Resolusi=None, Harga=None):
        current = self.head
        while current:
            if current.kamera.kode == kode:
                if Brand:
                    current.kamera.Brand = Brand
                if Model:
                    current.kamera.Model = Model 
                if Resolusi:
                    current.kamera.Resolusi = Resolusi
                if Tahun:
                    current.kamera.Tahun = Tahun 
                if Harga:
                    current.kamera.Harga = Harga
                print("Kamera berhasil diedit")
                return
            current = current.next
        print("Kamera tidak ditemukan")

    def list_kamera(self):
        if not self.head:
            print("Daftar kamera belum tersedia\n")
        else:
            print("Daftar Kamera:\n")
            current = self.head
            while current:
                kamera = current.kamera
                print(f"Kode: {kamera.kode}\nBrand: {kamera.Brand}\nModel: {kamera.Model}\nTahun: {kamera.Tahun}\nResolusi: {kamera.Resolusi} MP\nHarga: Rp {kamera.Harga:,}\n")
                current = current.next

    def quick_sort(self, arr, key, reverse=False):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0].kamera.__dict__[key]

            less = [node for node in arr[1:] if (node.kamera.__dict__[key] < pivot) or (node.kamera.__dict__[key] == pivot and node.kamera.kode < arr[0].kamera.kode)]
            greater = [node for node in arr[1:] if (node.kamera.__dict__[key] > pivot) or (node.kamera.__dict__[key] == pivot and node.kamera.kode >= arr[0].kamera.kode)]

            if reverse:
                return self.quick_sort(greater, key, reverse=True) + [arr[0]] + self.quick_sort(less, key, reverse=True)
            else:
                return self.quick_sort(less, key) + [arr[0]] + self.quick_sort(greater, key)

    def sort_kamera(self, key, order='asc'):
        kamera_list = []
        current = self.head
        while current:
            kamera_list.append(current)
            current = current.next

        if order == 'asc':
            sorted_list = self.quick_sort(kamera_list, key)
        else:
            sorted_list = self.quick_sort(kamera_list, key, reverse=True)

        self.head = sorted_list[0]
        current = self.head
        for node in sorted_list[1:]:
            current.next = node
            current = current.next
        current.next = None

    def jump_search(self, key, attr):
        current = self.head

        if attr == '2' or attr == 'kode':
            key = int(key)
            while current:
                if current.kamera.kode == key:
                    return current.kamera
                elif current.kamera.kode < key:
                    current = current.next
                else:
                    return None
        elif attr == '1' or attr == 'Brand':
            while current:
                if current.kamera.Brand == key:
                    return current.kamera
                elif current.kamera.Brand > key:
                    return None
                else:
                    current = current.next
        else:
            print("Atribut yang Anda masukkan tidak valid.")

        return None

    def search_kamera(self, key, attr):
        result = self.jump_search(key, attr)

        if result:
            print("\nKamera ditemukan:\n")
            print(f"Kode: {result.kode}\nBrand: {result.Brand}\nModel: {result.Model}\nTahun: {result.Tahun}\nResolusi: {result.Resolusi} MP\nHarga: Rp {result.Harga:,}\n")
        else:
            print("Kamera tidak ditemukan.")

if __name__ == "__main__":
    sistem_rekomendasi = SistemRekomendasiKamera()

    while True:
        print("\n[===---Rekomendasi Kamera 2024---===]\n")
        print("1. Lihat Rekomendasi Kamera")
        print("2. Tambah Kamera di Awal")
        print("3. Tambah Kamera di Akhir")
        print("4. Tambah Kamera di Antara")
        print("5. Edit Kamera")
        print("6. Hapus Kamera di Awal")
        print("7. Hapus Kamera di Akhir")
        print("8. Hapus Kamera di Antara")
        print("9. Cari Kamera")
        print("10. Tutup Program\n")
    
        pilih = input("Pilih Menu : ")
        if pilih == "1":
            print()
            sistem_rekomendasi.list_kamera()
            print("\n1. Ascending")
            print("2. Descending")
            sort_choice = input("Pilih jenis pengurutan: ")
            if sort_choice == "1":
                key = input("Urut Berdasarkan (kode,Brand,Tahun,Harga): ")
                sistem_rekomendasi.sort_kamera(key)
                print("Kamera berhasil diurutkan secara ascending berdasarkan", key)
                print()
                sistem_rekomendasi.list_kamera()
            elif sort_choice == "2":
                key = input("Urut Berdasarkan (kode,Brand,Tahun,Harga): ")
                sistem_rekomendasi.sort_kamera(key, order='desc')
                print("Kamera berhasil diurutkan secara descending berdasarkan", key)
                print()
                sistem_rekomendasi.list_kamera()
            else:
                print("Pilihan tidak valid.")
        elif pilih == "2":
            Brand = input("Masukkan Brand : ")
            Model = input("Masukkan Model : ")
            Tahun = int(input("Masukkan Tahun : "))
            Resolusi = int(input("Masukkan Resolusi (MP) : "))
            Harga = int(input("Masukkan Harga : "))
            sistem_rekomendasi.tambah_kamera_di_awal(Brand, Model, Tahun, Resolusi, Harga)
        elif pilih == "3":
            Brand = input("Masukkan Brand : ")
            Model = input("Masukkan Model : ")
            Tahun = int(input("Masukkan Tahun : "))
            Resolusi = int(input("Masukkan Resolusi (MP) : "))
            Harga = int(input("Masukkan Harga : "))
            sistem_rekomendasi.tambah_kamera_di_akhir(Brand, Model, Tahun, Resolusi, Harga)
        elif pilih == "4":
            posisi = int(input("Masukkan kode kamera yang menjadi posisi : "))
            Brand = input("Masukkan Brand : ")
            Model = input("Masukkan Model : ")
            Tahun = int(input("Masukkan Tahun : "))
            Resolusi = int(input("Masukkan Resolusi (MP) : "))
            Harga = int(input("Masukkan Harga : "))
            sistem_rekomendasi.tambah_kamera_di_antara(posisi, Brand, Model, Tahun, Resolusi, Harga)
        elif pilih == "5":
            sistem_rekomendasi.list_kamera()
            kode = int(input("Masukkan kode kamera yang ingin di update : "))
            Brand = input("Masukkan Brand (klik enter skip): ")
            Model = input("Masukkan Model (klik enter untuk skip): ")
            Resolusi = int(input("Masukkan Resolusi (klik enter untuk skip): ") or 0)
            Tahun = int(input("Masukkan Tahun (klik enter untuk skip): ") or 0)
            Harga = int(input("Masukkan Harga (klik enter untuk skip): ") or 0)
            sistem_rekomendasi.edit_kamera(kode, Brand, Model, Tahun, Resolusi, Harga)
        elif pilih == "6":
            sistem_rekomendasi.hapus_kamera_di_awal()
        elif pilih == "7":
            sistem_rekomendasi.hapus_kamera_di_akhir()
        elif pilih == "8":
            kode = int(input("Masukkan kode kamera yang ingin dihapus : "))
            sistem_rekomendasi.hapus_kamera_di_antara(kode)
        elif pilih =="9":
            attr = input("Pencarian berdasarkan \n1.Brand\n2.kode\n: ")
            if attr == "1" or "Brand":
                key = input("Masukkan nilai untuk pencarian: ")
                sistem_rekomendasi.search_kamera(key, attr)
            elif attr == "2" or "kode":
                key = int(input("Masukkan nilai untuk pencarian: "))
                sistem_rekomendasi.search_kamera(key, attr)
        elif pilih == "10":
            print("Terima Kasih")
            break
        else:
            print("Pilihan tidak tersedia, Silakan pilih menu kembali.")
