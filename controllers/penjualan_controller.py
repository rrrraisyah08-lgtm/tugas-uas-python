from database import get_connection
from utils.validator import input_int
from utils.ui import header
from datetime import datetime

class PenjualanController:

    def tambah(self):
        header("Tambah Penjualan")
        obat_id = input_int("ID Obat: ")
        jumlah = input_int("Jumlah: ")

        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM obat WHERE id=%s", (obat_id,))
        obat = cur.fetchone()

        if not obat:
            print("Obat tidak ditemukan!")
            return

        total = jumlah * obat["harga"]

        cur.execute("""INSERT INTO penjualan (obat_id, jumlah, total, tanggal)
            VALUES (%s,%s,%s,%s)""", (obat_id, jumlah, total, datetime.now()))
        con.commit()
        con.close()
        print("Penjualan berhasil disimpan!")

    def tampil(self):
        header("Data Penjualan")
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM penjualan")
        data = cur.fetchall()
        con.close()

        for d in data:
            print(f"{d['id']} | Obat: {d['obat_id']} | Jml: {d['jumlah']} | Total: {d['total']}")
