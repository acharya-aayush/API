from fastapi import APIRouter, HTTPException
from .schemas import Contact, ContactCreate
from .services import search_contacts, get_contact, create_contact

router = APIRouter()

@router.get("/", response_model=list[Contact])
def list_contacts(company: str | None = None, query: str | None = None):
    return search_contacts(company, query)

@router.get("/{contact_id}", response_model=Contact)
def read_contact(contact_id: int):
    contact = get_contact(contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.post("/", response_model=Contact, status_code=201)
def create_contact_endpoint(payload: ContactCreate):
    return create_contact(payload)
