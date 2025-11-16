from pydantic import BaseModel
from typing import Optional

class WorkoutCreate(BaseModel):
    title: str
    duration_minutes: int
    notes: Optional[str] = None

class Workout(WorkoutCreate):
    id: int

    class Config:
        orm_mode = True
