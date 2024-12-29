
from tortoise.models import Model
from tortoise import fields,run_async,Tortoise
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

db_url=os.getenv("DB_URL")


class User(Model):
    id=fields.IntField(primary_key=True)
    name=fields.CharField(max_length=50,null=True,unique=True)
    email=fields.CharField(max_length=50,null=True,unique=True)
    datetime=fields.DatetimeField(default=datetime.datetime.utcnow,null=True)

    class Meta:
        table="users"

    def __str__(self):
        return f"User(name={self.name},email={self.email})"
    
async def init_db()->None:
    try:
        #initialise conenction
        await Tortoise.init(db_url=db_url,modules={"models":["database"]})
        #generate schema
        await Tortoise.generate_schemas()

        #create user
        user_1=await User.create(name="manu",email="manu@example.com")
        await user_1.save()
        user_2=await User.create(name="neeraj",email="neeraj@example.com")
        await user_2.save()
    except Exception as error:
        print(f"Error while creating table :{error}")
    # finally:
    #     #close connection
    #     await Tortoise.close_connections()

# will be executed when run directly not executed when imported as module
if __name__=="__main__":
    run_async(init_db())