from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from random import randrange
import os
# import asyncpg

# Load environment variables
load_dotenv()
app=FastAPI()
# Access environment variable
DATABASE_URL = os.getenv("DATABASE_URL")
#get database


#in memory data
my_posts = [{"title":"title 1 ",
             "content":"some content 1",
             "published":True,
             "rating":3,"id":2},
             {"title":"title 2 ",
             "content":"some content 2",
             "published":False,
             "rating":3,"id":5},
             {"title":"title 3 ",
             "content":"some content 3",
             "published":True,
             "rating":3,"id":4}]


# Schema for input-validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = False  # Default value
    rating: Optional[int] = None
    id:int



@app.get("/")  # Home route
async def home_route():
    return {"message": "Hello, world!"}

@app.get('/getposts')
def get_all_post():
    return {"data":my_posts}

@app.post("/posts")
async def get_post(payLoad: dict = Body(...)):
    print(f"{payLoad}")
    return {"newpost": f"title: {payLoad['title']}, content: {payLoad['content']}"}

@app.post("/createposts")
async def create_posts(newPosts: Post):
    print(f"{newPosts}")
    print(newPosts.dict())  # Convert to dict
    return {"data": newPosts}

@app.post('/newdata')
def create_new_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000)
    my_posts.append(post_dict)
    return {"data":post_dict}
#retrieve one data
@app.get('/posts/{id}')
def get_post(id:int): #it automaticaly convert to integer if set type to int
    data={}
    for post in my_posts:
        if post["id"]==id:
        # if post["id"]==int(id):
            data=post     
    return{ "data":data}




