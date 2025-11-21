from typing import Optional
from .schemas import Product, ProductCreate

products: list[Product] = [
    Product(id=1, name="Wireless keyboard", category="office", quantity=12, description="Compact layout for desk use.")
]

_next_id = 2


def get_all_products(category: Optional[str] = None) -> list[Product]:
    if category is None:
        return products
    return [item for item in products if item.category.lower() == category.lower()]


def get_product(product_id: int) -> Optional[Product]:
    return next((item for item in products if item.id == product_id), None)


def add_product(payload: ProductCreate) -> Product:
    global _next_id
    product = Product(id=_next_id, **payload.model_dump())
    products.append(product)
    _next_id += 1
    return product
