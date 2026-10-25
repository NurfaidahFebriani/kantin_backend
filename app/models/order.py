
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    total_harga: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    status: Mapped[str] = mapped_column(
        String(30), default="menunggu", nullable=False
    )


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"), nullable=False
    )
    menu_id: Mapped[int] = mapped_column(
        ForeignKey("menus.id"), nullable=False
    )
    nama_menu: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    harga: Mapped[int] = mapped_column(Integer, nullable=False)
    jumlah: Mapped[int] = mapped_column(Integer, nullable=False)
    subtotal: Mapped[int] = mapped_column(Integer, nullable=False)
