
# Sistem Pemesanan Makanan Kantin

REST API berbasis Python dan FastAPI untuk mengelola menu makanan dan pesanan kantin.

## Fitur

- Melihat seluruh menu.
- Melihat detail menu berdasarkan ID.
- Menambahkan menu.
- Memperbarui menu.
- Menghapus menu.
- Membuat pesanan makanan.
- Melihat seluruh pesanan.
- Melihat detail pesanan.
- Menghitung total harga pesanan.
- Validasi input menggunakan Pydantic.
- Penyimpanan data menggunakan SQLite.
- Pengujian API menggunakan pytest.

## Teknologi

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- pytest
- Git

## Struktur Proyek

```text
kantin_backend/
├── app/
│   ├── models/
│   ├── repositories/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── database.py
│   └── main.py
├── tests/
│   └── test_api.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Instalasi

Pastikan Python sudah terpasang.

Install dependensi dengan perintah:

```bash
pip install -r requirements.txt
```

## Menjalankan Server

Jalankan perintah:

```bash
python -m uvicorn app.main:app --reload
```

Buka dokumentasi API melalui:

http://127.0.0.1:8000/docs

## Menjalankan Unit Test

Jalankan:

```bash
python -m pytest -v
```

Pengujian mencakup endpoint API, validasi input, serta pembuatan menu dan pesanan.
