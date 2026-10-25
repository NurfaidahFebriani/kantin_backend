
from app.repositories.menu_repository import MenuRepository
from app.repositories.order_repository import OrderRepository


class OrderService:
    def __init__(
        self,
        menu_repository: MenuRepository,
        order_repository: OrderRepository,
    ):
        self.menu_repository = menu_repository
        self.order_repository = order_repository

    def get_all_orders(self):
        return self.order_repository.get_all()

    def get_order_by_id(self, order_id: int):
        return self.order_repository.get_by_id(order_id)

    def create_order(self, order_data: dict):
        order_items = []
        total_harga = 0

        for item in order_data["items"]:
            menu = self.menu_repository.get_by_id(item["menu_id"])

            if menu is None:
                raise ValueError(
                    f"Menu dengan ID {item['menu_id']} tidak ditemukan"
                )

            if not menu.tersedia:
                raise ValueError(
                    f"Menu {menu.nama} sedang tidak tersedia"
                )

            jumlah = item["jumlah"]
            subtotal = menu.harga * jumlah

            order_items.append({
                "menu_id": menu.id,
                "nama_menu": menu.nama,
                "harga": menu.harga,
                "jumlah": jumlah,
                "subtotal": subtotal,
            })

            total_harga += subtotal

        order = {
            "items": order_items,
            "total_harga": total_harga,
            "status": "menunggu",
        }

        return self.order_repository.create(order)
