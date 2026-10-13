# Pengujian Unit — Manajemen Stok Barang

## Deskripsi Project

Project ini merupakan aplikasi sederhana menggunakan Python untuk mengelola stok barang. Project dibuat untuk memenuhi tugas mata kuliah Analisis dan Pengujian Sistem, dengan fokus pada penerapan Unit Testing menggunakan pytest.

## Fitur Utama

Program memiliki tiga fungsi utama:

1. **`tambah_stok(stok, jumlah)`** — menambahkan jumlah barang ke persediaan.
2. **`kurangi_stok(stok, jumlah)`** — mengurangi persediaan dengan validasi jumlah barang.
3. **`hitung_nilai_stok(stok, harga)`** — menghitung nilai total persediaan berdasarkan jumlah stok dan harga barang.

Program menerapkan validasi untuk menolak nilai stok negatif, jumlah penambahan atau pengurangan yang tidak valid, pengurangan melebihi persediaan, dan harga negatif.

## Teknologi

- Python 3.11
- pytest 9.1.1

## Struktur Project

```text
stok-barang/
├── inventory.py
├── tests/
│   └── test_inventory.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Cara Menjalankan Pengujian

Pastikan Python dan pytest sudah terpasang serta virtual environment sudah diaktifkan jika digunakan.

Instal pytest jika belum tersedia:

```powershell
python -m pip install pytest
```

Jalankan seluruh test dengan perintah:

```powershell
python -m pytest -v
```

Pytest akan menemukan dan menjalankan test yang sesuai dengan pola penamaan yang dikenali. Hasil `PASSED` menunjukkan bahwa test memenuhi hasil yang diharapkan, sedangkan `FAILED` menunjukkan bahwa test tidak memenuhi harapan.

## Rancangan Test Case

Pengujian mencakup tiga fungsi utama dengan skenario input valid dan tidak valid.

| ID | Skenario | Expected output |
|---|---|---|
| TC-01 | Penambahan stok valid | 15 |
| TC-02 | Penambahan dengan jumlah nol | ValueError |
| TC-03 | Pengurangan stok valid | 7 |
| TC-04 | Pengurangan melebihi persediaan | ValueError |
| TC-05 | Menghitung nilai stok | 50000 |
| TC-06 | Harga negatif | ValueError |
| TC-07 | Stok awal negatif saat menambah | ValueError |
| TC-08 | Jumlah penambahan negatif | ValueError |
| TC-09 | Stok awal negatif saat mengurangi | ValueError |
| TC-10 | Jumlah pengurangan nol | ValueError |
| TC-11 | Jumlah pengurangan negatif | ValueError |
| TC-12 | Pengurangan sama dengan stok tersedia | 0 |
| TC-13 | Stok negatif saat menghitung nilai | ValueError |
| TC-14 | Harga nol | 0 |

## Status Pengujian

Enam test awal telah dijalankan dan menghasilkan **6 passed, 0 failed**.

Delapan skenario tambahan telah dirancang untuk memperluas cakupan pengujian. Status akhirnya akan diperbarui setelah seluruh test tambahan dijalankan.

## Tujuan

Pengujian ini bertujuan memeriksa kebenaran hasil fungsi serta perilaku program ketika menerima input yang tidak valid.