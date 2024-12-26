import asyncpg
import asyncio
import os
from dotenv import load_dotenv
from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import SessionLocal,get_connection_db
from models import User

load_dotenv()

db_url=os.getenv("DB_URL")

app:FastAPI= FastAPI()

@app.on_event("startup")
async def on_startup():
    await get_connection_db()
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get('/users/')
async def read_users(db:AsyncSession =Depends(get_db)):
    try:
        result=await db.execute(select(User))
        users= result.scalars().all()
        return users
    except Exception as error:
        print("Error while reading from database {error}")




# async def connect_db():
#     try:
#         connection =await asyncpg.connect(db_url)
#         if connection != None:
#             print("connected to database")
#         query=("""SELECT * FROM posts;""")
#         rows= await connection.fetch(query)
#         for row in rows:
#             print(dict(row))
#     except Exception as error:
#         print(f" Error while connecting to database {error}")
#     finally:
#         await connection.close()   

# # app: FastAPI= FastAPI()

# asyncio.run(connect_db()) 