
from tortoise.models import Model
from tortoise import fields,run_async,Tortoise
from dotenv import load_dotenv
import os
import datetime
from fastapi import FastAPI
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.fastapi import register_tortoise


load_dotenv()

db_url=os.getenv("DB_URL")

app:FastAPI=FastAPI()

class User(Model):
    id=fields.IntField(primary_key=True)
    name=fields.CharField(max_length=50,null=True,unique=True)
    email=fields.CharField(max_length=50,null=True,unique=True)
    datetime=fields.DatetimeField(default=datetime.datetime.utcnow,null=True)

    class Meta:
        table="users"

    def __str__(self):
        return f"User(name={self.name},email={self.email})"
    
user_1=pydantic_model_creator(User,name="manu",email="manu@example.com")

register_tortoise(
    app,
    db_url=db_url,
    modules={'models':['main']},
    generate_schemas=True,
    add_exception_handler=True
)