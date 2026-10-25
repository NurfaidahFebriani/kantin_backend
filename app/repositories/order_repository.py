
from sqlalchemy.orm import Session

from app.models.order import Order, OrderItem


class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        orders = self.db.query(Order).all()

        return [
            self._order_to_dict(order)
            for order in orders
        ]

    def get_by_id(self, order_id: int):
        order = (
            self.db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )

        if order is None:
            return None

        return self._order_to_dict(order)

    def create(self, order_data: dict):
        order = Order(
            total_harga=order_data["total_harga"],
            status=order_data.get("status", "menunggu"),
        )

        self.db.add(order)
        self.db.flush()

        for item in order_data["items"]:
            order_item = OrderItem(
                order_id=order.id,
                menu_id=item["menu_id"],
                nama_menu=item["nama_menu"],
                harga=item["harga"],
                jumlah=item["jumlah"],
                subtotal=item["subtotal"],
            )

            self.db.add(order_item)

        self.db.commit()
        self.db.refresh(order)

        return self._order_to_dict(order)

    def _order_to_dict(self, order: Order):
        items = (
            self.db.query(OrderItem)
            .filter(OrderItem.order_id == order.id)
            .all()
        )

        return {
            "id": order.id,
            "items": [
                {
                    "menu_id": item.menu_id,
                    "nama_menu": item.nama_menu,
                    "harga": item.harga,
                    "jumlah": item.jumlah,
                    "subtotal": item.subtotal,
                }
                for item in items
            ],
            "total_harga": order.total_harga,
            "status": order.status,
        }
