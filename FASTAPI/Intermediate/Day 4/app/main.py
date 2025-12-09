from fastapi import FastAPI
from .routers import events

app = FastAPI(title="Event Scheduling API")

app.include_router(events.router, prefix="/events", tags=["events"])

@app.get("/")
def root():
    return {"service": "Event scheduling", "status": "ready"}
