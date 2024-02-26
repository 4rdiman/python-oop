class Item:
    # class attribute
    """class attribute ini bisa diakses dimanapun di dalam kelas,
    yang mana sangat bagus untuk membuat sesuatu yang akan dipake semua instance
    di dalam kelas"""
    pay_rate = 0.8 # discount 20%
    all = []
    def __init__(self, nama: str, harga: float, kuantitas=0):
        # validation to recieve argument that we want
        assert harga >= 0, f"harga: {harga}, harus lebih dari atau sama dengan 0"
        assert kuantitas >=0, f"kuantitas: {kuantitas}, harus lebih dari atau sama dengan 0"

        # asign to self project
        self.nama = nama
        self.harga = harga
        self.kuantitas = kuantitas

        # untuk mengambil semua instance attribute
        Item.all.append(self)

    def hitung_harga(self):
        return self.harga * self.kuantitas
    
    def apply_discount(self):
        # akses class attribute menggunakan self
        self.harga = self.harga * self.pay_rate

    # __repr__ untuk menampilkan apa ketika class Item diprint
    def __repr__(self):
        return f"Item('{self.nama}', {self.harga}, {self.kuantitas})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

# print spesifik
# for instance in Item.all:
#     print(instance.nama)

