from typing import Optional

from sqlmodel import Field,SQLModel,Session,create_engine,select
from dotenv import load_dotenv
import os
load_dotenv()
db_url=os.getenv("DB_URL")

class User(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name: str
    secret_name: str
    age:Optional[int]=None
# create rows of model as instance of model
user_1=User(name="manu p",secret_name="mpa",age=26)
user_2=User(name="neeraj",secret_name="pappan",age=26)


#create engine
engine=create_engine(db_url)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(user_1)
    session.add(user_2)
    session.commit()