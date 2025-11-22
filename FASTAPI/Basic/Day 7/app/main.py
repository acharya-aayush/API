from fastapi import FastAPI
from .routers import blog

app = FastAPI(title="Blog Comments API")

app.include_router(blog.router, prefix="/posts", tags=["posts"])

@app.get("/")
def root():
    return {"service": "Blog comments", "status": "ready"}
