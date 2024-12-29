'''
Inherit from Base class fro creating model provided by sqlalchemy

'''
from database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Text
from datetime import datetime

'''
class Note:
    id serial
    title str
    content str
    date creat dateti,e

    then define we cannot be able to retent,each time we use return the class
'''
class Note(Base):
    __tablename__="notes"
    #id:Mapped[str]=mapped_column(primary_key=True,)
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    title:Mapped[str]=mapped_column(nullable=False)
    content:Mapped[str]= mapped_column(Text,nullable=False)
    date_created:Mapped[datetime]=mapped_column(default=datetime.utcnow)

    def __repr__(self)->str:
        return f"<Note {self.title} at {self.date_created}>"