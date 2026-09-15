buku = {
    "judul" : "laut bercerita",
    "penulis" : "leila s.chudori",
    "tahun_terbit" : "2017"
}

while True:
    print("---- Menu Buku  ----")
    print("1. Tampilkan Data Buku")
    print("2. Tambahkan Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        print("Data buku")
        print (buku)

    elif pilih == "2":
        penerbit = input("masukkan nama penerbit: ")
        buku["penerbit"] = penerbit
        print("penerbit berhasil ditambahkan")

    elif pilih == "3":
        penulis = input("masukkan nama penulis: ")
        buku["penulis"] = penulis
        print("penulis berhasil diubah")

    elif pilih == "4":
        del buku["penerbit"] 
        print("penerbit berhasil dihapus")

    elif pilih == "5":
        print("penyimpanan dan pengelolaan buku telah selesai")
        break
