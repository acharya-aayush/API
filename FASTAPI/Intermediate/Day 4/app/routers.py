from fastapi import APIRouter, HTTPException
from .schemas import Event, EventCreate, EventUpdate
from .services import get_all_events, get_event, update_event, create_event

router = APIRouter()

@router.get("/", response_model=list[Event])
def list_events():
    return get_all_events()

@router.get("/{event_id}", response_model=Event)
def read_event(event_id: int):
    event = get_event(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/", response_model=Event, status_code=201)
def create_event_endpoint(payload: EventCreate):
    return create_event(payload)

@router.put("/{event_id}", response_model=Event)
def edit_event(event_id: int, payload: EventUpdate):
    event = update_event(event_id, payload)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
