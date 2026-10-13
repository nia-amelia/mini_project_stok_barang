
import pytest

from inventory import (
    tambah_stok,
    kurangi_stok,
    hitung_nilai_stok,
)


# Pengujian fungsi tambah_stok
def test_tambah_stok_berhasil():
    assert tambah_stok(10, 5) == 15


def test_tambah_stok_nol_ditolak():
    with pytest.raises(ValueError):
        tambah_stok(10, 0)


# Pengujian fungsi kurangi_stok
def test_kurangi_stok_berhasil():
    assert kurangi_stok(10, 3) == 7


def test_kurangi_stok_melebihi_persediaan():
    with pytest.raises(ValueError):
        kurangi_stok(10, 15)


# Pengujian fungsi hitung_nilai_stok
def test_hitung_nilai_stok_berhasil():
    assert hitung_nilai_stok(10, 5000) == 50000


def test_hitung_nilai_stok_harga_negatif():
    with pytest.raises(ValueError):
        hitung_nilai_stok(10, -5000)


def test_tambah_stok_stok_awal_negatif():
    with pytest.raises(ValueError):
        tambah_stok(-1, 5)


def test_tambah_stok_jumlah_negatif():
    with pytest.raises(ValueError):
        tambah_stok(10, -2)


def test_kurangi_stok_stok_awal_negatif():
    with pytest.raises(ValueError):
        kurangi_stok(-1, 3)


def test_kurangi_stok_jumlah_nol():
    with pytest.raises(ValueError):
        kurangi_stok(10, 0)


def test_kurangi_stok_jumlah_negatif():
    with pytest.raises(ValueError):
        kurangi_stok(10, -2)


def test_kurangi_stok_jumlah_sama_dengan_persediaan():
    assert kurangi_stok(10, 10) == 0


def test_hitung_nilai_stok_stok_negatif():
    with pytest.raises(ValueError):
        hitung_nilai_stok(-1, 5000)


def test_hitung_nilai_stok_harga_nol():
    assert hitung_nilai_stok(10, 0) == 0

