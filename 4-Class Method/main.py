import csv

class Item:
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

    # classmethod hanya bisa diakses pada tingkat kelas
    @classmethod
    def baca_csv(cls):
        with open("items.csv", 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in  items:
            Item(
                nama=item["name"],
                harga=float(item["price"]),
                kuantitas=int(item["quantity"])
            )


    # __repr__ untuk menampilkan apa ketika class Item diprint
    def __repr__(self):
        return f"Item('{self.nama}', {self.harga}, {self.kuantitas})"
    

Item.baca_csv()
print(Item.all)
