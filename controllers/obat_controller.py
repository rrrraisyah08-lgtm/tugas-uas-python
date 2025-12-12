from database import get_connection
from utils.validator import input_int
from utils.ui import header

class ObatController:

    def tambah(self):
        header("Tambah Obat")
        nama = input("Nama Obat: ")
        stok = input_int("Stok: ")
        harga = input_int("Harga: ")

        con = get_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO obat (nama, stok, harga) VALUES (%s, %s, %s)",
                    (nama, stok, harga))
        con.commit()
        con.close()
        print("Obat berhasil ditambahkan!")

    def tampil(self):
        header("Daftar Obat")
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM obat")
        data = cur.fetchall()
        con.close()
        for d in data:
            print(f"{d['id']}. {d['nama']} - stok: {d['stok']} - harga: {d['harga']}")

    def hapus(self):
        header("Hapus Obat")
        id_ = input_int("ID obat: ")

        con = get_connection()
        cur = con.cursor()
        cur.execute("DELETE FROM obat WHERE id=%s", (id_,))
        con.commit()
        con.close()
        print("Obat berhasil dihapus!")
