from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.contact import ContactCreate, ContactRead
from app.services.contact_service import ContactService
from app.database import get_db

router = APIRouter(prefix="/contacts", tags=["Contacts"])
service = ContactService()

@router.post("/", response_model=ContactRead)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return service.create_contact(db, contact)

@router.get("/", response_model=list[ContactRead])
def list_contacts(db: Session = Depends(get_db)):
    return service.get_all_contacts(db)

@router.get("/{contact_id}", response_model=ContactRead)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    return service.get_contact_by_id(db, contact_id)

@router.put("/{contact_id}", response_model=ContactRead)
def update_contact(contact_id: int, contact: ContactCreate, db: Session = Depends(get_db)):
    return service.update_contact(db, contact_id, contact)

@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    service.delete_contact(db, contact_id)
    return {"detail": "Contact deleted"}
