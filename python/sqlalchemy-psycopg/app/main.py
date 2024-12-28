from dotenv import load_dotenv
from fastapi import FastAPI,HTTPException,status,Response,Depends
from pydantic import BaseModel
import psycopg
import os
from psycopg.rows import dict_row
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal,engine

load_dotenv()

db_url=os.getenv("DB_URL")

# create enf=gine to create all our models

models.Base.metadata.create_all(bind=engine)


app:FastAPI=FastAPI()

# create dependency
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    title:str
    content:str
    published:bool
@app.get('/get')
def test_post(db: Session=Depends(get_db)):
    return{"status":"success"}
