from typing import Optional
from .schemas import Book, BookCreate

books: list[Book] = [
    Book(id=1, title="The FastAPI Handbook", author="A. Dev", published_year=2025, summary="Practical examples for API builders.")
]

_next_id = 2


def get_all_books() -> list[Book]:
    return books


def get_book(book_id: int) -> Optional[Book]:
    return next((item for item in books if item.id == book_id), None)


def add_book(payload: BookCreate) -> Book:
    global _next_id
    book = Book(id=_next_id, **payload.model_dump())
    books.append(book)
    _next_id += 1
    return book
