from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    category: str
    quantity: int
    description: Optional[str] = None

class Product(ProductCreate):
    id: int

    class Config:
        orm_mode = True
