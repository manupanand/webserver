from dotenv import load_dotenv,find_dotenv
from pymongo import MongoClient,monitoring
from pymongo.collection import Collection
from logger import CommandLogger
from mongoengine import *
import os
import json
import pymongo

load_dotenv(find_dotenv())

mongo_url=os.getenv("MONGO_URL")

monitoring.register(CommandLogger())


def connect_database()->MongoClient:
    try:
        client =MongoClient(mongo_url,connectTimeoutMs=60000,compressors='zlib',zlibCompressionLevel=3)
        # databases=client.list_database_names()
        # print(databases)
        return client
    except Exception as error:
        print(f"Erro in connecting to database :{error}")
        return None
def create_db()->Collection:
    client=connect_database()
    user_management=client.user_management
    users=user_management.users
    db=client.list_database_names()
    print(db)
    user1={
        "name":"manu",
        "email":"anu@example.com"
    }
    id=users.insert_one(user1).inserted_id
    print(id)
    return users

def load_data():
    db=create_db()#call db user
    with open("./database/user.json","r") as file:
        data =json.load(file)

    db.insert_many(data)

# load_data()
# connect_database()
def bulk_operation():
    client=connect_database()
    restaurant_management=client.restaurant_managemnt
    restaurant=restaurant_management.restaurant

    operations=[
        pymongo.InsertOne(
        {
            "name": "Mongo's Deli",
            "cuisine": "Sandwiches",
            "borough": "Manhattan",
            "restaurant_id": "1234"
        }
    ),
    pymongo.InsertOne(
        {
            "name": "Mongo's Deli",
            "cuisine": "Sandwiches",
            "borough": "Brooklyn",
            "restaurant_id": "5678"
        }
    )
    ]#can do updateone, updatemany etc
    result=restaurant.bulk_write(operations)

bulk_operation()