from fastapi import FastAPI, HTTPException, Depends, Query
from app import models, shemas, crud, database, encryption
from sqlalchemy.orm import Session
from app.dependencies import get_db

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.post("/password/{service_name}", response_model=shemas.PasswordResponse)
def create_or_update_password(service_name: str, password_data: shemas.PasswordCreate, db: Session = Depends(get_db)):
    encrypted_pw = encryption.encrypt_password(password_data.password)
    return crud.create_or_update_password(db, service_name, encrypted_pw)


@app.get("/password/{service_name}", response_model=shemas.PasswordResponse)
def get_password(service_name: str, db: Session = Depends(get_db)):
    password_obj = crud.get_password_by_service_name(db, service_name)
    if password_obj is None:
        raise HTTPException(status_code=404, detail="Password not found")
    decrypted_pw = encryption.decrypt_password(password_obj.encrypted_password)
    return {"service_name": password_obj.service_name, "password": decrypted_pw}


@app.get("/password/", response_model=list[shemas.PasswordResponse])
def search_passwords(service_name: str = Query(...), db: Session = Depends(get_db)):
    results = crud.search_passwords(db, service_name)
    return [{"service_name": p.service_name, "password": encryption.decrypt_password(p.encrypted_password)} for p in results]
