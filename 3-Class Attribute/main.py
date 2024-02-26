class Item:
    # class attribute
    """class attribute ini bisa diakses dimanapun di dalam kelas,
    yang mana sangat bagus untuk membuat sesuatu yang akan dipake semua instance
    di dalam kelas"""
    pay_rate = 0.8 # discount 20%
    def __init__(self, nama: str, harga: float, kuantitas=0):
        # validation to recieve argument that we want
        assert harga >= 0, f"harga: {harga}, harus lebih dari atau sama dengan 0"
        assert kuantitas >=0, f"kuantitas: {kuantitas}, harus lebih dari atau sama dengan 0"

        # asign to self project
        self.nama = nama
        self.harga = harga
        self.kuantitas = kuantitas

    def hitung_harga(self):
        return self.harga * self.kuantitas
    
    def apply_discount(self):
        # akses class attribute menggunakan self
        self.harga = self.harga * self.pay_rate


item1 = Item("Smart Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Smart Watch", 100, 2)

item1.apply_discount()
print(item1.harga)

# bisa diubah juga kayak instance attribute
# untuk spesifik gunakan item2 saja instead of Item
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.harga)

item3.apply_discount()
print(item3.harga)


