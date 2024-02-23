class Item:

    def __init__(self, nama, harga, kuantitas):
        # $ini gunanya supaya bisa passing attribute
        self.nama = nama
        self.harga = harga
        self.kuantitas = kuantitas

    def hitung_harga(self):
        # kan kita sudah punya akses ke self atau object itu sendiri
        # maka kita tidak perlu lagi parameter tambahan
        return self.harga * self.kuantitas

# inilah gunanya __init__
item1 = Item("Smart Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

# $kayak gini
print(item1.nama)
print(item2.nama)
print(item1.harga)
print(item2.harga)
print(item1.kuantitas)
print(item2.kuantitas)

# the problem is we hard code the atrribute
# what if we can use it dinamicly?
# datanglah yang namanya contructor init
# item1.nama = "Smart Phone"
# item1.harga = 100
# item1.kuantitas = 5

