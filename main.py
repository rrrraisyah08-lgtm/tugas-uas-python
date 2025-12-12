from database import init_db
from controllers.obat_controller import ObatController
from controllers.penjualan_controller import PenjualanController
from controllers.resep_controller import ResepController
from utils.ui import header

init_db()

obat = ObatController()
penjualan = PenjualanController()
resep = ResepController()

while True:
    header("SISTEM MANAJEMEN APOTEK")
    print("1. Kelola Obat")
    print("2. Kelola Penjualan")
    print("3. Kelola Resep")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        header("MENU OBAT")
        print("1. Tambah Obat")
        print("2. Lihat Obat")
        print("3. Hapus Obat")
        sub = input("Pilih: ")
        if sub == "1": obat.tambah()
        elif sub == "2": obat.tampil()
        elif sub == "3": obat.hapus()

    elif pilih == "2":
        header("MENU PENJUALAN")
        print("1. Tambah Penjualan")
        print("2. Lihat Penjualan")
        sub = input("Pilih: ")
        if sub == "1": penjualan.tambah()
        elif sub == "2": penjualan.tampil()

    elif pilih == "3":
        header("MENU RESEP")
        print("1. Input Resep")
        print("2. Lihat Resep")
        sub = input("Pilih: ")
        if sub == "1": resep.tambah()
        elif sub == "2": resep.tampil()

    elif pilih == "0":
        break
