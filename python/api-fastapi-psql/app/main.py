from fastapi import FastAPI, Body,HTTPException,status,Response
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from random import randrange
import asyncpg
import asyncio

# from database.postgres import print_log
import os
# import asyncpg

# Load environment variables
load_dotenv()
app=FastAPI()
# Access environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

conn_pool:Optional[asyncpg.Pool] = None
#get database
async def postgres_init()-> None:
    ''' tesing database connection'''
    global conn_pool
    try:
        conn_pool= await asyncpg.connect(DATABASE_URL)
        if conn_pool:
            print("connection pool created")
        values =await conn_pool.fetch('SELECT * FROM products;')
    except Exception as error:
        print(f"error inn conneting to database:{error}")
        raise

asyncio.run(postgres_init())
@app.get('/')
async def ome():
    
    return {"messge":"get home route"}