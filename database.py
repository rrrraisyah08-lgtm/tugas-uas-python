import pymysql

def get_connection():
    return pymysql.connect(host="localhost", user="root", password="", database="apotek_db",
        cursorclass=pymysql.cursors.DictCursor)

def init_db():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS obat (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(100),
        stok INT,
        harga DOUBLE)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS penjualan (
        id INT AUTO_INCREMENT PRIMARY KEY,
        obat_id INT,
        jumlah INT,
        total DOUBLE,
        tanggal DATETIME,
        FOREIGN KEY (obat_id) REFERENCES obat(id))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS resep (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama_pasien VARCHAR(100),
        obat_id INT,
        jumlah INT,
        keterangan TEXT,
        tanggal DATETIME,
        FOREIGN KEY (obat_id) REFERENCES obat(id))""")
    con.commit()
    con.close()
