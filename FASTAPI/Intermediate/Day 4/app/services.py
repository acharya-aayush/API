from datetime import date
from typing import Optional
from .schemas import Event, EventCreate, EventUpdate

events: list[Event] = [
    Event(id=1, title="Product review meeting", date=date(2026, 2, 15), location="Main office", notes="Prepare customer feedback")
]

_next_id = 2


def get_all_events() -> list[Event]:
    return events


def get_event(event_id: int) -> Optional[Event]:
    return next((item for item in events if item.id == event_id), None)


def create_event(payload: EventCreate) -> Event:
    global _next_id
    event = Event(id=_next_id, status="scheduled", **payload.model_dump())
    events.append(event)
    _next_id += 1
    return event


def update_event(event_id: int, payload: EventUpdate) -> Optional[Event]:
    event = get_event(event_id)
    if event is None:
        return None
    if payload.title is not None:
        event.title = payload.title
    if payload.date is not None:
        event.date = payload.date
    if payload.location is not None:
        event.location = payload.location
    if payload.notes is not None:
        event.notes = payload.notes
    return event
