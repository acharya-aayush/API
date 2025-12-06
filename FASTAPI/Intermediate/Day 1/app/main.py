from fastapi import FastAPI
from .routers import projects

app = FastAPI(title="Project Tracker API")

app.include_router(projects.router, prefix="/projects", tags=["projects"])

@app.get("/")
def root():
    return {"service": "Project tracker", "status": "ready"}
