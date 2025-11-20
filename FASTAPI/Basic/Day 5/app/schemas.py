from pydantic import BaseModel
from typing import List

class NoteCreate(BaseModel):
    title: str
    content: str
    tags: List[str] = []

class Note(NoteCreate):
    id: int

    class Config:
        orm_mode = True
