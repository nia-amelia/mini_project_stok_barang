
def tambah_stok(stok, jumlah):
    """Menambahkan barang ke stok."""
    if stok < 0:
        raise ValueError("Stok awal tidak boleh negatif")

    if jumlah <= 0:
        raise ValueError("Jumlah penambahan harus lebih dari nol")

    return stok + jumlah


def kurangi_stok(stok, jumlah):
    """Mengurangi stok barang."""
    if stok < 0:
        raise ValueError("Stok awal tidak boleh negatif")

    if jumlah <= 0:
        raise ValueError("Jumlah pengurangan harus lebih dari nol")

    if jumlah > stok:
        raise ValueError("Stok tidak mencukupi")

    return stok - jumlah


def hitung_nilai_stok(stok, harga):
    """Menghitung nilai seluruh persediaan."""
    if stok < 0:
        raise ValueError("Stok tidak boleh negatif")

    if harga < 0:
        raise ValueError("Harga tidak boleh negatif")

    return stok * harga
