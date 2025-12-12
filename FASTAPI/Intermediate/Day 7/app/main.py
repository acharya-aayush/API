from fastapi import FastAPI
from .routers import requests

app = FastAPI(title="Service Request API")

app.include_router(requests.router, prefix="/requests", tags=["requests"])

@app.get("/")
def root():
    return {"service": "Service requests", "status": "ready"}
