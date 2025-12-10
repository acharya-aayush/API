from pydantic import BaseModel
from typing import List, Optional

class ArticleCreate(BaseModel):
    title: str
    body: str
    category: str
    tags: List[str] = []

class Article(ArticleCreate):
    id: int

    class Config:
        orm_mode = True
