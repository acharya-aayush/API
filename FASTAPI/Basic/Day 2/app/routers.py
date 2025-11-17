from fastapi import APIRouter, HTTPException
from .schemas import Book, BookCreate
from .services import add_book, get_all_books, get_book

router = APIRouter()

@router.get("/", response_model=list[Book])
def list_books():
    return get_all_books()

@router.get("/{book_id}", response_model=Book)
def read_book(book_id: int):
    book = get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=Book, status_code=201)
def create_book(payload: BookCreate):
    return add_book(payload)
