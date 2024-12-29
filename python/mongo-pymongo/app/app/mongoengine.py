from mongoengine import *
from mongoengine import connect,Document,StringField
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())

mongo_url=os.getenv("MONGO_URL")

connect(host=mongo_url,db='restaurants',alias='db1')#alias is given fro name of connection
#we can provide more number of connect
#connect(host=mongo_url,db='users',alias='db2')# havr to give seperate name alias
#disconnect(alias="db2")
class user(Document):
    name= StringField()
    meta={'db_alias':'db1'}#about the connection to db1