from pydantic import BaseModel
from typing import Optional, List

class ProjectCreate(BaseModel):
    name: str
    owner: str
    description: Optional[str] = None
    tags: List[str] = []

class Project(ProjectCreate):
    id: int

    class Config:
        orm_mode = True
