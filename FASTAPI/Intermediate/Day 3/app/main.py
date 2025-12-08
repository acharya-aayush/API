from fastapi import FastAPI
from .routers import inventory

app = FastAPI(title="Inventory Status API")

app.include_router(inventory.router, prefix="/inventory", tags=["inventory"])

@app.get("/")
def root():
    return {"service": "Inventory status", "status": "ready"}
