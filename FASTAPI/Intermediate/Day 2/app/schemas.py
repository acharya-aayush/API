from pydantic import BaseModel
from typing import Optional

class ContactCreate(BaseModel):
    name: str
    email: str
    company: Optional[str] = None
    phone: Optional[str] = None

class Contact(ContactCreate):
    id: int

    class Config:
        orm_mode = True
