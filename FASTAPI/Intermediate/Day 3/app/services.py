from typing import Optional
from .schemas import Item, ItemCreate, ItemStatus

items: list[Item] = [
    Item(id=1, name="Desk lamp", quantity=12, status=ItemStatus.in_stock, description="Warm LED desk lamp.")
]

_next_id = 2


def get_all_items(status: Optional[ItemStatus] = None) -> list[Item]:
    if status is None:
        return items
    return [item for item in items if item.status == status]


def get_item(item_id: int) -> Optional[Item]:
    return next((item for item in items if item.id == item_id), None)


def add_item(payload: ItemCreate) -> Item:
    global _next_id
    item = Item(id=_next_id, **payload.model_dump())
    items.append(item)
    _next_id += 1
    return item
