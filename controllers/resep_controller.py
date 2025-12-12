from database import get_connection
from utils.validator import input_int
from utils.ui import header
from datetime import datetime

class ResepController:

    def tambah(self):
        header("Input Resep")
        nama_pasien = input("Nama Pasien: ")
        obat_id = input_int("ID Obat: ")
        jumlah = input_int("Jumlah: ")
        keterangan = input("Keterangan: ")

        con = get_connection()
        cur = con.cursor()

        cur.execute("""INSERT INTO resep (nama_pasien, obat_id, jumlah, keterangan, tanggal)
            VALUES (%s,%s,%s,%s,%s)""", (nama_pasien, obat_id, jumlah, keterangan, datetime.now()))
        con.commit()
        con.close()
        print("Resep berhasil disimpan!")

    def tampil(self):
        header("Data Resep")
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM resep")
        data = cur.fetchall()
        con.close()

        for d in data:
            print(f"{d['id']} | {d['nama_pasien']} | Obat: {d['obat_id']} | Jml: {d['jumlah']}")
