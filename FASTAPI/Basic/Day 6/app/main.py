from fastapi import FastAPI
from .routers import products

app = FastAPI(title="Product Inventory API")

app.include_router(products.router, prefix="/products", tags=["products"])

@app.get("/")
def root():
    return {"service": "Product inventory", "status": "ready"}
