from fastapi import FastAPI
from .routers import workouts

app = FastAPI(title="Workout Tracker API")

app.include_router(workouts.router, prefix="/workouts", tags=["workouts"])

@app.get("/")
def root():
    return {"service": "Workout tracker", "status": "ready"}
