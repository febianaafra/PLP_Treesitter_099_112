class Mobil:
    def __init__(self, merk, warna, tahun):
        self.merk = merk    
        self.warna = warna
        self.tahun = tahun
        self.kecepatan = 0

    def info(self):
        return f"{self.merk} ({self.tahun}) berwarna {self.warna}"

    def gas(self, tambah_kecepatan):
        self.kecepatan += tambah_kecepatan
        print(f"{self.merk} melaju dengan kecepatan {self.kecepatan} km/jam.")

mobil1 = Mobil("Toyota Avanza", "Hitam", 2023)
mobil2 = Mobil("Honda Civic", "Putih", 2024)

print(mobil1.info())  
mobil1.gas(60)       