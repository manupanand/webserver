from fastapi import FastAPI
from dotenv import load_dotenv
from pymongo import MongoClient

import os


load_dotenv()

db_url=os.getenv("MONGO_URL")
database_name=os.getenv("DB_NAME")

app:FastAPI= FastAPI()

@app.on_event("startup")
def init_db_client():
    try:
        app.mongodb_client=MongoClient(db_url)
        app.database=app.mongodb_client(database_name)
        print("Database connected succes fully")
    except Exception as error:
        print(f"Error in connecting :{error}")

    
@app.on_event("shutdown")
def shutdown_db():
    app.mongodb_client.close()