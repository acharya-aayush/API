from enum import Enum
from pydantic import BaseModel
from typing import Optional

class ItemStatus(str, Enum):
    in_stock = "in_stock"
    low_stock = "low_stock"
    out_of_stock = "out_of_stock"

class ItemCreate(BaseModel):
    name: str
    quantity: int
    status: ItemStatus
    description: Optional[str] = None

class Item(ItemCreate):
    id: int

    class Config:
        orm_mode = True
