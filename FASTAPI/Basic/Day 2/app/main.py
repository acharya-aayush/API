from fastapi import FastAPI
from .routers import books

app = FastAPI(title="Book Catalog API")

app.include_router(books.router, prefix="/books", tags=["books"])

@app.get("/")
def root():
    return {"service": "Book catalog", "status": "ready"}
