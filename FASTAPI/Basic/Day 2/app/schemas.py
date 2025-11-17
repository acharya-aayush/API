from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int
    summary: Optional[str] = None

class Book(BookCreate):
    id: int

    class Config:
        orm_mode = True
