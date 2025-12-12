from pydantic import BaseModel
from enum import Enum
from typing import Optional

class RequestStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"

class RequestCreate(BaseModel):
    title: str
    description: str

class RequestPatch(BaseModel):
    status: Optional[RequestStatus] = None
    note: Optional[str] = None

class ServiceRequest(RequestCreate):
    id: int
    status: RequestStatus
    note: Optional[str] = None

    class Config:
        orm_mode = True
