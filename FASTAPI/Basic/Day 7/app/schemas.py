from pydantic import BaseModel
from typing import List

class CommentCreate(BaseModel):
    author: str
    content: str

class Comment(CommentCreate):
    id: int

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    title: str
    body: str

class Post(PostCreate):
    id: int
    comments: List[Comment] = []

    class Config:
        orm_mode = True
