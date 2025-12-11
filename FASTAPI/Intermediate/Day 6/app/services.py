from typing import Dict, List
from .schemas import Note, NoteCreate

notes_by_user: Dict[str, List[Note]] = {
    "alice": [Note(id=1, owner="alice", title="Sprint notes", content="Release checklist and blockers.", tags=["sprint", "planning"])],
}

_next_id = 2


def get_notes_for_user(username: str) -> List[Note]:
    return notes_by_user.get(username, [])


def create_note_for_user(username: str, payload: NoteCreate) -> Note:
    global _next_id
    note = Note(id=_next_id, owner=username, **payload.model_dump())
    notes_by_user.setdefault(username, []).append(note)
    _next_id += 1
    return note
