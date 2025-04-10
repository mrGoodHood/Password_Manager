from fastapi import FastAPI, HTTPException, Depends, Query
from app import models, shemas, database
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI


@app.post("/password/{service_name}", response_model=shemas.PasswordResponse)
def create_or_update_password():
    pass


@app.get("/password/{service_name}", response_model=shemas.PasswordResponse)
def get_password():
    pass


@app.get("/password/", response_model=list[shemas.PasswordResponse])
def search_passwords():
    pass

