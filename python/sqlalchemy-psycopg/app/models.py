from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,func,TIMESTAMP
from sqlalchemy.sql.expression import null


class Post(Base):
    __tablename__="posts"

    id= Column(Integer, primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,default=True)
    created_at=Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())