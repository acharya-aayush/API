from fastapi import FastAPI
from .routers import auth

app = FastAPI(title="Auth Simulation API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"service": "Auth simulation", "status": "ready"}
