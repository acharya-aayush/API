from fastapi import FastAPI
from .routers import contacts

app = FastAPI(title="Contact Directory API")

app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])

@app.get("/")
def root():
    return {"service": "Contact directory", "status": "ready"}
