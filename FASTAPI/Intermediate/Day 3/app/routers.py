from fastapi import APIRouter, HTTPException
from .schemas import Item, ItemCreate, ItemStatus
from .services import get_all_items, get_item, add_item

router = APIRouter()

@router.get("/", response_model=list[Item])
def list_items(status: ItemStatus | None = None):
    return get_all_items(status)

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=Item, status_code=201)
def create_item_endpoint(payload: ItemCreate):
    return add_item(payload)
