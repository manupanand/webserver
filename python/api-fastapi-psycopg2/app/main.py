from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
from contextlib import asynccontextmanager
from typing  import Optional
from database import init_postgres
import os
#psycopg not working
import asyncpg



load_dotenv()
#db config
db_url=os.getenv("DB_URL")
print(os.getenv("DB_URL"),db_url)
conn_pool:Optional[asyncpg.Pool]=None



# test connection


# async def init_postgres()-> None:
#     global conn_pool
#     try:
#         conn_pool= await asyncpg.create_pool()

# async def close_postgres()-> None:

# @asynccontextmanager
# async def lifespan(app:FastAPI):
#     await #init postgres
#     yield
#     await #close postgres



# app:FastAPI= FastAPI(lifespan=lifespan)

# @app.get('/')
# def get_main():
#     return {"message":"got main route"}