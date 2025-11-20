from fastapi import APIRouter, HTTPException
from .schemas import Note, NoteCreate
from .services import add_note, get_all_notes, get_note

router = APIRouter()

@router.get("/", response_model=list[Note])
def list_notes(tag: str | None = None):
    return get_all_notes(tag)

@router.get("/{note_id}", response_model=Note)
def read_note(note_id: int):
    note = get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post("/", response_model=Note, status_code=201)
def create_note(payload: NoteCreate):
    return add_note(payload)
