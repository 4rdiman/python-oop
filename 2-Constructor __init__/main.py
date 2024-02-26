class Item:

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


item1 = Item("Smart Phone", 100, -2)
item2 = Item("Laptop", 1000, 3)


