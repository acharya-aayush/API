from fastapi import FastAPI
from .routers import articles

app = FastAPI(title="Knowledge Base API")

app.include_router(articles.router, prefix="/articles", tags=["articles"])

@app.get("/")
def root():
    return {"service": "Knowledge base", "status": "ready"}
