'''
engine:engine object use this we connect to database, we can use asyncio engine, but since we use sqlalchemy use orm engine

'''
from databases import Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()
db_url=os.getenv("DB_URL")

database =Database(db_url)

engine=create_engine(db_url,echo=True,future=True)
Base=declarative_base()
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

