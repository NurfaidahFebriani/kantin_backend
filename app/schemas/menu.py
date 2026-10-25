
from pydantic import BaseModel, ConfigDict, Field


class MenuCreate(BaseModel):
    nama: str = Field(min_length=2, max_length=100)
    harga: int = Field(gt=0)
    tersedia: bool = True


class MenuResponse(MenuCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
