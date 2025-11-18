from fastapi import FastAPI
from .routers import recipes

app = FastAPI(title="Recipe Search API")

app.include_router(recipes.router, prefix="/recipes", tags=["recipes"])

@app.get("/")
def root():
    return {"service": "Recipe search", "status": "ready"}
