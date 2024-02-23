class Item:
    # method
    """mengapa harus ada self terus? karena dipython dengan memanggil method
    itu sendiri, itu adalah sebuah parameter untuk method"""
    def hitung_harga(self, satuan, kuantitas):
        return satuan * kuantitas

item1 = Item()

# attribute
item1.nama = "Smart Phone"
item1.harga = 100
item1.kuantitas = 5

"""dalam hal ini item1 adalah parameter self, kemuadian seterusnya"""
print(item1.hitung_harga(item1.harga, item1.kuantitas))
