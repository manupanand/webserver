from dotenv import load_dotenv
from fastapi import FastAPI,HTTPException,status,Response
from pydantic import BaseModel
import psycopg
import os
from psycopg.rows import dict_row

load_dotenv()

db_url=os.getenv("DB_URL")

app:FastAPI=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool

def connect_db():
    try:
        #connect to database
        connection=psycopg.connect(db_url,row_factory=dict_row)
      
        # cursor to perform database operation
        cursor =connection.cursor()
        print("connected to db successfull")
        return connection,cursor
        # cur.execute("SELECT * FROM posts;")

        # rows=cur.fetchall()
        # for row in rows:
        #     print(row)

        # cur.close()
        # conn.close()
    except Exception as error:
        print(f" Error in connecting to database {error}")