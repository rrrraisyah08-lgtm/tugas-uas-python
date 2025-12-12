# 📦 Sistem Manajemen Apotek 

Aplikasi Python berbasis **Console (CLI)** untuk mengelola data **Obat, Penjualan, dan Resep** dengan konsep **OOP, modularisasi, dan SQLite**.  
Project ini sangat cocok untuk **tugas UAS** atau latihan membuat aplikasi Python terstruktur.

---

# 🚀 Quick Highlights

### ✔ Modular & Mudah Dikembangkan
Struktur package jelas dan rapi:
- `controllers/` — logika fitur  
- `models/` — class OOP  
- `utils/` — UI & validator  
- `database.py` — koneksi SQLite  

### ✔ Console UI Interaktif
Menu dikontrol dari `main.py` dan `utils/ui.py`.

### ✔ SQLite Database
Seluruh data disimpan di file `apotek.db`.


### Menggunakan:
- OOP  
- Percabangan  
- Perulangan  
- Modularisasi  
- CLI User Interface  

---

# 🗂 Project Structure

apotek_app/
│ main.py
│ database.py
│
├── controllers/
│ obat_controller.py
│ penjualan_controller.py
│ resep_controller.py
│
├── models/
│ obat.py
│ penjualan.py
│ resep.py
│
├── utils/
│ ui.py
│ validator.py
│
├── docs/
│ MANUAL.md
│
└── screenshots/
lihat_resep.png
pesan.png
tambah_harga_obat.png

yaml
Copy code

---

# ✅ Quick Start

### **Requirements**
- Python **3.10+**
- SQLite (sudah otomatis tersedia dalam Python)

### **Cara Menjalankan Program**

Buka terminal di folder project:

python main.py

yaml
Copy code

Jika berhasil, muncul tampilan seperti:

==================================================
SISTEM MANAJEMEN APOTEK
Kelola Obat

Kelola Penjualan

Kelola Resep

Keluar
Pilih menu:

yaml
Copy code

---

# 📝 Manual (Panduan Lengkap)

Manual lengkap berada di:

👉 **docs/MANUAL.md**

Silakan isi dengan:
- Langkah menjalankan program  
- Contoh input & output  
- Penjelasan fitur  
- Screenshot  

---

# 📸 Screenshots

> **Letakkan semua screenshot kamu di folder `/screenshots`**  
> Nama file boleh pakai contoh di bawah.

### **1. Lihat Resep**
![Lihat Resep](https://github.com/user-attachments/assets/96051f48-f20b-45ad-83d2-57091d69b7a8)


### **2. Menu Pesan / Input Resep**
![Menu Pesan](https://github.com/user-attachments/assets/NEW-LINK-DARI-GITHUB)



### **3. Tambah Obat & Daftar Obat**
![Tambah Obat](https://github.com/user-attachments/assets/NEW-LINK-DARI-GITHUB)


---

# 🔖 Quick Manual Link
👉 **docs/MANUAL.md**

---

# 💡 Development Notes

Gunakan `.gitignore` untuk mengabaikan file tidak penting:

pycache/
*.db

yaml
Copy code

Jika menambah library, buat:

requirements.txt

yaml
Copy code

---

# 🤝 Contributing

Gunakan workflow pengembangan:

git checkout -b fitur-penjualan

sql
Copy code

Commit dengan pesan jelas:

git commit -m "add fitur penjualan + update stok obat"
