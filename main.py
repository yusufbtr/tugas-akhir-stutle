import sys

namaObat = {"Paramex": [0, 0], "Panadol": [0, 0], "Bodrexin": [0, 0], "Procold": [0, 0]}
tagihan = 0
gudang = {
    "Paramex": {
        "harga": 1000,
        "stok": 5
    },
    "Panadol": {
        "harga": 2000,
        "stok": 6
    },
    "Bodrexin": {
        "harga": 3000,
        "stok": 7
    },
    "Procold": {
        "harga": 4000,
        "stok": 8
    }
}

while True:
    print()
    print('Selamat Datang di Toko Obat Stutle\n'
          'Ketik perintah untuk membuka menu\n'
          '1. List Obat\n'
          '-perintah: list-obat\n'
          '2. Beli Obat\n'
          '-perintah: beli-<namaobat>\n'
          '3. Hapus Obat\n'
          '-perintah: hapus-<namaobat>\n'
          '4. Melihat Daftar Keranjang\n'
          '-perintah: keranjang\n'
          '5. Transaksi Pembelian\n'
          '-perintah: checkout\n'
          '6. Exit\n'
          '-perintah: exit\n'
          )

    choice = input("Silahkan ketik perintah yang anda inginkan: ")

    if choice == "list-obat":
        for j in gudang:
            print(j, gudang[j])

    elif choice == "beli-paramex":
        print("Pembelian Obat Paramex")
        qty = int(input("Jumlah obat yang ingin dibeli: "))
        gudang["Paramex"]["stok"] -= qty
        tambah = [value for key, value in namaObat.items() if key == "Paramex"]
        tambah[0][0] += qty
        tambah[0][1] += int(int(gudang["Paramex"]["harga"]) * tambah[0][0])

    elif choice == "beli-panadol":
        print("Pembelian Obat Panadol")
        qty = int(input("Jumlah obat yang ingin dibeli: "))
        gudang["Panadol"]["stok"] -= qty
        tambah = [value for key, value in namaObat.items() if key == "Panadol"]
        tambah[0][0] += qty
        tambah[0][1] += int(int(gudang["Panadol"]["harga"]) * tambah[0][0])

    elif choice == "beli-bodrexin":
        print("Pembelian Obat Bodrexin")
        qty = int(input("Jumlah obat yang ingin dibeli: "))
        gudang["Bodrexin"]["stok"] -= qty
        tambah = [value for key, value in namaObat.items() if key == "Bodrexin"]
        tambah[0][0] += qty
        tambah[0][1] += int(int(gudang["Bodrexin"]["harga"]) * tambah[0][0])

    elif choice == "beli-procold":
        print("Pembelian Obat Procold")
        qty = int(input("Jumlah obat yang ingin dibeli: "))
        gudang["Procold"]["stok"] -= qty
        tambah = [value for key, value in namaObat.items() if key == "Procold"]
        tambah[0][0] += qty
        tambah[0][1] += int(int(gudang["Procold"]["harga"]) * tambah[0][0])

    elif choice == "hapus-paramex":
        qty = int(input("Jumlah obat yang ingin dihapus: "))
        gudang["Paramex"]["stok"] += qty
        hapus = [value for key, value in namaObat.items() if key == "Paramex"]
        hapus[0][0] -= qty
        hapus[0][1] -= int(int(gudang["Paramex"]["harga"]) * hapus[0][0])

    elif choice == "hapus-panadol":
        qty = int(input("Jumlah obat yang ingin dihapus: "))
        gudang["Panadol"]["stok"] += qty
        hapus = [value for key, value in namaObat.items() if key == "Panadol"]
        hapus[0][0] -= qty
        hapus[0][1] -= int(int(gudang["Panadol"]["harga"]) * hapus[0][0])

    elif choice == "hapus-bodrexin":
        qty = int(input("Jumlah obat yang ingin dihapus: "))
        gudang["Bodrexin"]["stok"] += qty
        hapus = [value for key, value in namaObat.items() if key == "Bodrexin"]
        hapus[0][0] -= qty
        hapus[0][1] -= int(int(gudang["Bodrexin"]["harga"]) * hapus[0][0])

    elif choice == "hapus-procold":
        qty = int(input("Jumlah obat yang ingin dihapus: "))
        gudang["Procold"]["stok"] += qty
        hapus = [value for key, value in namaObat.items() if key == "Procold"]
        hapus[0][0] -= qty
        hapus[0][1] -= int(int(gudang["Procold"]["harga"]) * hapus[0][0])

    elif choice == "keranjang":
        print(" " + "\nBarang yang dibeli: ")
        struk = {key: value for key, value in namaObat.items() if value[0] != 0}
        for key, value in struk.items():
            print(value[0], key + ", Total Harga Rp", value[1], "|", "Sisa stok barang:", gudang[key]["stok"])
            tagihan += value[1]

    elif choice == "checkout":
        struk = {key: value for key, value in namaObat.items() if value[0] != 0}
        for key, value in struk.items():
            tagihan += value[1]
        print("Total Tagihan: Rp", tagihan)
        bayar = int(input("Nominal uang pembayaran: Rp "))
        if bayar > tagihan:
            print("Uang kembaliannya sebesar: Rp", bayar - tagihan)
        elif bayar == tagihan:
            print("Uang pembayarannya pas")
        else:
            print("Uang pembayaran kurang")

    elif choice == "exit":
        sys.exit()

    else:
        print("Pilihan tidak ada di menu silahkan masukan ulang")
