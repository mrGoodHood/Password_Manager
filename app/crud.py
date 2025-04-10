from sqlalchemy.orm import Session
from app import models


def create_or_update_password(db: Session, service_name: str, encrypted_password: str):
    existing = db.query(models.Password).filter(models.Password.service_name == service_name).first()
    if existing:
        existing.encrypted_password = encrypted_password
    else:
        existing = models.Password(service_name=service_name, encrypted_password=encrypted_password)
        db.add(existing)
    db.commit()
    db.refresh(existing)
    return existing


def get_password_by_service_name(db: Session, service_name: str):
    return db.query(models.Password).filter(models.Password.service_name == service_name).first()


def search_passwords(db: Session, part_name: str):
    return db.query(models.Password).filter(models.Password.service_name.ilike(f"%{part_name}%")).all()
