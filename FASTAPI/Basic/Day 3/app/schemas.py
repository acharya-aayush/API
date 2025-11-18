from pydantic import BaseModel
from typing import List, Optional

class RecipeBase(BaseModel):
    title: str
    ingredients: List[str]
    cook_time_minutes: int

class Recipe(RecipeBase):
    id: int
    description: Optional[str] = None

    class Config:
        orm_mode = True

class RecipeSearch(BaseModel):
    ingredient: Optional[str] = None
    max_minutes: Optional[int] = None
