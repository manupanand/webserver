import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

db_url = os.getenv("DB_URL")

engine= create_engine(db_url,echo=True)# responsible to connect to database
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)#we have to make a session to talk to database
Base=declarative_base() #all models we make extend this base class