from dotenv import load_dotenv
from fastapi import FastAPI,HTTPException,status,Response
from pydantic import BaseModel
import psycopg
import os
from psycopg.rows import dict_row

load_dotenv()

db_url=os.getenv("DB_URL")

app:FastAPI=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool

def connect_db():
    try:
        #connect to database
        connection=psycopg.connect(db_url,row_factory=dict_row)
      
        # cursor to perform database operation
        cursor =connection.cursor()
        print("connected to db successfull")
        return connection,cursor
        # cur.execute("SELECT * FROM posts;")

        # rows=cur.fetchall()
        # for row in rows:
        #     print(row)

        # cur.close()
        # conn.close()
    except Exception as error:
        print(f" Error in connecting to database {error}")
@app.get("/")
def get_all_posts():
    try:

        connection,cursor=connect_db()
        query=("""SELECT * FROM posts;""")
        cursor.execute(query)
        posts=cursor.fetchall()
        return {"message":posts}
    
    except Exception as error:
        print("error in {error}")
    finally:
        cursor.close()
        connection.close()

#post request -create new data
@app.post('/create',status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    try:
        connection,cursor=connect_db()
        query=("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *;""")
        cursor.execute(query,(post.title,post.content,post.published))
        new_post=cursor.fetchone()
        if new_post is None:
            raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        connection.commit()#commit the staged change
        return {"data":new_post}
    except Exception as error:
        print(f"error in creating :{error}")
    finally:
        connection.close()
        cursor.close()