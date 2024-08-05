#zidan amikul afham
#5230411330

from prettytable import PrettyTable

class Node:
    def __init__(self, no_sku, nama_barang, harga_satuan, jumlah_stok):
        self.no_sku = no_sku
        self.nama_barang = nama_barang
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, no_sku, nama_barang, harga_satuan, jumlah_stok):
        new_node = Node(no_sku, nama_barang, harga_satuan, jumlah_stok)
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while(True):
            if new_node.no_sku == temp.no_sku:
                return False
            if new_node.no_sku < temp.no_sku:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def search(self, no_sku):
        return self._search(self.root, no_sku)

    def _search(self, current, no_sku):
        if current is None:
            return None
        if no_sku == current.no_sku:
            return current
        elif no_sku < current.no_sku:
            return self._search(current.left, no_sku)
        else:
            return self._search(current.right, no_sku)

    def update_stok(self, no_sku, jumlah_stok):
        node = self.search(no_sku)
        if node:
            node.jumlah_stok += jumlah_stok
            print("\n>>> Stok berhasil ditambahkan <<<")
        else:
            print("\n>>> No. SKU tidak ditemukan. <<<")

    def reduce_stok(self, no_sku, jumlah_stok):
        node = self.search(no_sku)
        if node:
            node.jumlah_stok -= jumlah_stok
        else:
            print("\n>>> No. SKU tidak ditemukan. <<<")

    def tampilkan_stok(self):
        table = PrettyTable(["No. SKU", "Nama Barang", "Harga Satuan", "Jumlah Stok"])
        self._tampilkan_stok(self.root, table)
        print(table)

    def _tampilkan_stok(self, current, table):
        if current:
            self._tampilkan_stok(current.left, table)
            table.add_row([current.no_sku, current.nama_barang, current.harga_satuan, current.jumlah_stok])
            self._tampilkan_stok(current.right, table)

class Transaksi:
    def __init__(self, nama_konsumen, no_sku, jumlah_beli, subtotal):
        self.nama_konsumen = nama_konsumen
        self.no_sku = no_sku
        self.jumlah_beli = jumlah_beli
        self.subtotal = subtotal

def main_menu():
    print("\n|| Sistem Informasi Stok dan Transaksi (SITORSI)")
    print("\n+============================+")
    print("|         MAIN MENU          |")
    print("+============================+")
    print("|1. Kelola Stok Barang       |")
    print("|2. Kelola Transaksi Konsumen|")
    print("|0. Keluar                   |")
    print("+============================+")

def sub_menu1():
    print("\n+============================+")
    print("|     KELOLA STOK BARANG     |")
    print("+============================+")
    print("|1. Input Data Stok Barang   |")
    print("|2. Restok Barang            |")
    print("|3. Tampilkan Stok Barang    |")
    print("|0. Kembali                  |")
    print("+============================+")

def input_data_stok_barang(bst):
    no_sku = input("\nMasukkan No. SKU (4 digit angka) : ")
    if len(no_sku) != 4 or not no_sku.isdigit():
        print("\n>>> No. SKU harus berupa 4 digit angka. <<<")
        return
    if bst.search(no_sku):
        print("\n>>> No. SKU Sudah Tersimpan <<<")
        return
    nama_barang = input("Masukkan Nama Barang : ")
    harga_satuan = float(input("Masukkan Harga Satuan : "))
    jumlah_stok = int(input("Masukkan Jumlah Stok : "))
    bst.insert(no_sku, nama_barang, harga_satuan, jumlah_stok)
    print("\n>>> Data Stok Barang berhasil diinputkan. <<<")

def restok_barang(bst):
    no_sku = input("\nMasukkan No. SKU : ")
    if len(no_sku) != 4 or not no_sku.isdigit():
        print("\n>>> No. SKU harus berupa 4 digit angka. <<<")
        return
    node = bst.search(no_sku)
    if node:
        jumlah_stok = int(input("Masukkan stok yang ditambahkan : "))
        bst.update_stok(no_sku, jumlah_stok)
    else:
        print("\n>>> No. SKU tidak ditemukan. Silahkan input terlebih dahulu <<<")

def tampilkan_stok_barang(bst):
    print("\n|| Data Stok Barang")
    print("")
    bst.tampilkan_stok()

def sub_menu2():
    print("\n+============================================+")
    print("|          KELOLA TRANSAKSI KONSUMEN         |")
    print("+============================================+")
    print("|1. Input Data Transaksi Baru                |")
    print("|2. Lihat Data Seluruh Transaksi Konsumen    |")
    print("|3. Lihat Data Transaksi Berdasarkan Subtotal|")
    print("|0. Kembali                                  |")
    print("+============================================+")

def input_data_transaksi_baru(bst, transaksi):
    nama_konsumen = input("Masukkan nama konsumen: ")
    while True:
        no_sku = input("Masukkan No. SKU barang: ")
        if len(no_sku) != 4 or not no_sku.isdigit():
            print("\n>>> No. SKU harus berupa 4 digit angka. <<<")
            return
        node = bst.search(no_sku)
        if node:
            jumlah_beli = int(input("Masukkan jumlah beli: "))
            if node.jumlah_stok >= jumlah_beli:
                subtotal = node.harga_satuan * jumlah_beli
                transaksi.append(Transaksi(nama_konsumen, no_sku, jumlah_beli, subtotal))
                bst.reduce_stok(no_sku, jumlah_beli)
                print("\n>>> Data Transaksi Konsumen berhasil diinputkan. <<<")
                lanjutkan_transaksi = input("Tambah produk lagi untuk konsumen ini? (Y/N): ").upper()
                if lanjutkan_transaksi == 'N':
                    break
            else:
                print("\n>>> Jumlah Stok No. SKU yang anda beli tidak mencukupi. <<<")
                lanjutkan_transaksi = input("Apakah ingin melanjutkan transaksi? (Y/N): ").upper()
                if lanjutkan_transaksi == 'N':
                    break
                
        else:
            print("\n>>> No. SKU yang diinputkan belum terdaftar. <<<")
            lanjutkan_transaksi = input("Apakah Ingin melanjutkan transaksi? (Y/N): ").upper()
            if lanjutkan_transaksi == 'N':
                break

def lihat_data_seluruh_transaksi(transaksi):
    print("\n|| Data Seluruh Transaksi Konsumen")
    print("")
    table = PrettyTable(["Konsumen", "No. SKU", "Jumlah Beli", "Subtotal"])
    for tr in transaksi:
        table.add_row([tr.nama_konsumen, tr.no_sku, tr.jumlah_beli, tr.subtotal])
    print(table)

def lihat_data_transaksi_berdasarkan_subtotal(transaksi):
    transaksi_urut = sorted(transaksi, key=lambda x: x.subtotal, reverse=True)
    print("\n|| Data Transaksi Berdasarkan Subtotal")
    print("")
    table = PrettyTable(["Konsumen", "No. SKU", "Jumlah Beli", "Subtotal"])
    for tr in transaksi_urut:
        table.add_row([tr.nama_konsumen, tr.no_sku, tr.jumlah_beli, tr.subtotal])
    print(table)

def main():  
    bst = BinarySearchTree()
    transaksi = []
    while (True):
        main_menu()
        pilihMenu = input("\n>> Masukkan Pilihan Menu: ")
        if pilihMenu == "1":
            while (True):
                sub_menu1()
                pilihSubMenu1 = input("\n>> Masukkan Pilihan Menu: ")
                if pilihSubMenu1 == "1":
                    input_data_stok_barang(bst)
                elif pilihSubMenu1 == "2":
                    restok_barang(bst)
                elif pilihSubMenu1 == "3":
                    tampilkan_stok_barang(bst)
                elif pilihSubMenu1 == "0":
                    break
                else:
                    print("\n>>> Pilihan tidak valid, silakan coba lagi. <<<")
        elif pilihMenu == "2":
            while (True):
                sub_menu2()
                pilihSubMenu2 = input(">> Masukkan Pilihan Menu: ")
                if pilihSubMenu2 == "1":
                    input_data_transaksi_baru(bst, transaksi)
                elif pilihSubMenu2 == "2":
                    lihat_data_seluruh_transaksi(transaksi)
                elif pilihSubMenu2 == "3":
                    lihat_data_transaksi_berdasarkan_subtotal(transaksi)
                elif pilihSubMenu2 == "0":
                    break
                else:
                    print("\n>>> Pilihan tidak valid, silakan coba lagi. <<<")
        elif pilihMenu == "0":
            print("\n>>> Terimakasih, Program SITORSI telah keluar. <<<")
            break
        else:
            print("\n>>> Pilihan tidak valid, silakan coba lagi. <<<")

if __name__ == "__main__":
    main()
