from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class EventCreate(BaseModel):
    title: str
    date: date
    location: str
    notes: Optional[str] = None

class EventUpdate(BaseModel):
    title: Optional[str] = None
    date: Optional[date] = None
    location: Optional[str] = None
    notes: Optional[str] = None

class Event(EventCreate):
    id: int
    status: str = Field(default="scheduled")

    class Config:
        orm_mode = True
