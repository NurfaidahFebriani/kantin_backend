
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Menu(Base):
    __tablename__ = "menus"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    nama: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    harga: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    tersedia: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
