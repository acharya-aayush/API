from fastapi import APIRouter, Depends, Header, HTTPException
from .schemas import Note, NoteCreate, User
from .services import get_notes_for_user, create_note_for_user

router = APIRouter()

def get_current_user(x_user: str | None = Header(None)) -> User:
    if x_user is None or x_user.strip() == "":
        raise HTTPException(status_code=400, detail="X-User header is required")
    return User(username=x_user)

@router.get("/", response_model=list[Note])
def list_notes(current_user: User = Depends(get_current_user)):
    return get_notes_for_user(current_user.username)

@router.post("/", response_model=Note, status_code=201)
def create_note_endpoint(payload: NoteCreate, current_user: User = Depends(get_current_user)):
    return create_note_for_user(current_user.username, payload)
