
from pydantic import BaseModel, Field


class OrderItemCreate(BaseModel):
    menu_id: int = Field(gt=0)
    jumlah: int = Field(gt=0)


class OrderCreate(BaseModel):
    items: list[OrderItemCreate] = Field(min_length=1)


class OrderItemResponse(BaseModel):
    menu_id: int
    nama_menu: str
    harga: int
    jumlah: int
    subtotal: int


class OrderResponse(BaseModel):
    id: int
    items: list[OrderItemResponse]
    total_harga: int
    status: str
