from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str

class NoteCreate(BaseModel):
    title: str
    content: str
    tags: List[str] = []

class Note(NoteCreate):
    id: int
    owner: str

    class Config:
        orm_mode = True
