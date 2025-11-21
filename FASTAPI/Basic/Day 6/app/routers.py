from fastapi import APIRouter, HTTPException
from .schemas import Product, ProductCreate
from .services import add_product, get_all_products, get_product

router = APIRouter()

@router.get("/", response_model=list[Product])
def list_products(category: str | None = None):
    return get_all_products(category)

@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int):
    product = get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=Product, status_code=201)
def create_product(payload: ProductCreate):
    return add_product(payload)
