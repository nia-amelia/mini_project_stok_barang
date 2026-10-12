# Mini Stock Management

## Deskripsi
Mini Stock Management adalah program sederhana berbasis Python untuk mengelola perhitungan stok barang.

## Fitur
1. Menambahkan stok barang.
2. Mengurangi stok barang dengan validasi persediaan.
3. Menghitung nilai persediaan berdasarkan jumlah dan harga satuan.

## Teknologi
- Python
- pytest

## Cara Menjalankan Pengujian

Instal dependensi:

```bash
python -m pip install -r requirements.txt
```

Jalankan unit test:

```bash
python -m pytest -v
```

## Cakupan Pengujian
Pengujian mencakup skenario input valid dan tidak valid untuk tiga fungsi utama, yaitu `tambah_stok`, `kurangi_stok`, dan `hitung_nilai_stok`.