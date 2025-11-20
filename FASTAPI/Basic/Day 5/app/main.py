from fastapi import FastAPI
from .routers import notes

app = FastAPI(title="Tagged Notes API")

app.include_router(notes.router, prefix="/notes", tags=["notes"])

@app.get("/")
def root():
    return {"service": "Tagged notes", "status": "ready"}
