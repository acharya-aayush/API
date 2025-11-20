from typing import Optional
from .schemas import Note, NoteCreate

notes: list[Note] = [
    Note(id=1, title="Meeting notes", content="Review priorities for the launch.", tags=["work", "planning"])
]

_next_id = 2


def get_all_notes(tag: Optional[str] = None) -> list[Note]:
    if tag is None:
        return notes
    return [item for item in notes if tag.lower() in {t.lower() for t in item.tags}]


def get_note(note_id: int) -> Optional[Note]:
    return next((item for item in notes if item.id == note_id), None)


def add_note(payload: NoteCreate) -> Note:
    global _next_id
    note = Note(id=_next_id, **payload.model_dump())
    notes.append(note)
    _next_id += 1
    return note
