
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# 1. Menguji halaman utama
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "success"


# 2. Menguji status kesehatan API
def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


# 3. Menguji pengambilan semua menu
def test_get_menus():
    response = client.get("/api/v1/menus/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# 4. Menguji pengambilan semua pesanan
def test_get_orders():
    response = client.get("/api/v1/orders/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# 5. Menguji pembuatan menu
def test_create_menu():
    response = client.post(
        "/api/v1/menus/",
        json={
            "nama": "Es Teh Unit Test",
            "harga": 5000,
            "tersedia": True,
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["nama"] == "Es Teh Unit Test"
    assert data["harga"] == 5000
    assert data["tersedia"] is True
    assert "id" in data


# 6. Menguji validasi harga menu
def test_create_menu_invalid_price():
    response = client.post(
        "/api/v1/menus/",
        json={
            "nama": "Es Teh Tidak Valid",
            "harga": 0,
            "tersedia": True,
        },
    )

    assert response.status_code == 422


# 7. Menguji menu yang tidak ditemukan
def test_get_menu_not_found():
    response = client.get("/api/v1/menus/999999")

    assert response.status_code == 404


# 8. Menguji pembuatan pesanan
def test_create_order():
    menu_response = client.post(
        "/api/v1/menus/",
        json={
            "nama": "Menu Tes Pesanan",
            "harga": 10000,
            "tersedia": True,
        },
    )

    assert menu_response.status_code == 201

    menu_id = menu_response.json()["id"]

    response = client.post(
        "/api/v1/orders/",
        json={
            "items": [
                {
                    "menu_id": menu_id,
                    "jumlah": 2,
                }
            ]
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["total_harga"] == 20000
    assert data["status"] == "menunggu"
    assert len(data["items"]) == 1
    assert data["items"][0]["jumlah"] == 2


# 9. Menguji pesanan dengan menu yang tidak ditemukan
def test_create_order_with_missing_menu():
    response = client.post(
        "/api/v1/orders/",
        json={
            "items": [
                {
                    "menu_id": 999999,
                    "jumlah": 1,
                }
            ]
        },
    )

    assert response.status_code == 400


# 10. Menguji pesanan dengan daftar item kosong
def test_create_order_with_empty_items():
    response = client.post(
        "/api/v1/orders/",
        json={
            "items": [],
        },
    )

    assert response.status_code == 422


# 11. Menguji nama menu terlalu pendek
def test_create_menu_name_too_short():
    response = client.post(
        "/api/v1/menus/",
        json={
            "nama": "A",
            "harga": 5000,
            "tersedia": True,
        },
    )

    assert response.status_code == 422


# 12. Menguji harga menu negatif
def test_create_menu_negative_price():
    response = client.post(
        "/api/v1/menus/",
        json={
            "nama": "Es Teh Negatif",
            "harga": -5000,
            "tersedia": True,
        },
    )

    assert response.status_code == 422


# 13. Menguji jumlah pesanan nol
def test_create_order_zero_quantity():
    response = client.post(
        "/api/v1/orders/",
        json={
            "items": [
                {
                    "menu_id": 1,
                    "jumlah": 0,
                }
            ]
        },
    )

    assert response.status_code == 422


# 14. Menguji pesanan yang tidak ditemukan
def test_get_order_not_found():
    response = client.get("/api/v1/orders/999999")

    assert response.status_code == 404


# 15. Menguji pesanan dengan menu tidak tersedia
def test_create_order_unavailable_menu():
    menu_response = client.post(
        "/api/v1/menus/",
        json={
            "nama": "Menu Tidak Tersedia",
            "harga": 12000,
            "tersedia": False,
        },
    )

    assert menu_response.status_code == 201

    menu_id = menu_response.json()["id"]

    response = client.post(
        "/api/v1/orders/",
        json={
            "items": [
                {
                    "menu_id": menu_id,
                    "jumlah": 1,
                }
            ]
        },
    )

    assert response.status_code == 400
    assert "tidak tersedia" in response.json()["detail"]
