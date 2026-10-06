class PersegiPanjang:
    def__init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def__str__(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

input_panjang = int(input("Masukkan panjang (cm):"))
input_lebar = int(input("Masukkan lebar (cm): "))

pp = PersegiPanjang(input_panjang, input_lebar)




