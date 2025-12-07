from typing import Optional
from .schemas import Contact, ContactCreate

contacts: list[Contact] = [
    Contact(id=1, name="Jade Patel", email="jade@studio.com", company="Studio Co", phone="+12125551234")
]

_next_id = 2


def get_contact(contact_id: int) -> Optional[Contact]:
    return next((item for item in contacts if item.id == contact_id), None)


def search_contacts(company: Optional[str], query: Optional[str]) -> list[Contact]:
    results = contacts
    if company:
        results = [item for item in results if item.company and item.company.lower() == company.lower()]
    if query:
        term = query.lower()
        results = [item for item in results if term in item.name.lower() or term in item.email.lower() or (item.company and term in item.company.lower())]
    return results


def create_contact(payload: ContactCreate) -> Contact:
    global _next_id
    contact = Contact(id=_next_id, **payload.model_dump())
    contacts.append(contact)
    _next_id += 1
    return contact
