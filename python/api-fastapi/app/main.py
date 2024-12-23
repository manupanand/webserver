from fastapi import FastAPI, Body,HTTPException,status,Response
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
             "rating":3,"id":4},
             {"title":"title 3 ",
             "content":"some content 3",
             "published":True,
             "rating":3,"id":7}]
def find_index_posts(id):
    for index,post in enumerate(my_posts):
        if post["id"]==id:
            return index
        
# def find_post(id):
#     for post in my_posts:
#         if post["id"]==id:
#             return post



# Schema for input-validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = False  # Default value
    rating: Optional[int] = None
    # id:int



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

@app.post('/newdata',status_code=status.HTTP_201_CREATED)
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
        elif post["id"]!=id:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"request with id:{id} not found")
        #   response.status_code=status.HTTP_404_NOT_FOUND
        #   return{"message": f"request with id:{id} not found"}

# delete post
 
@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)#delete 204
def delete_post(id :int):
    #find index 
    #my_post.pop(index)
    index = find_index_posts(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"given id {id} not found") 
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#update
@app.put('/posts/{id}')
def update_post(id:int, post:Post):
    index_post=find_index_posts(id)
    print(index_post)
    if  index_post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} doesnot exists")
    else:
        post_dict=post.dict()
        post_dict['id']=id
        my_posts[index_post]=post_dict
    return {f"message":"post updated succesfuly ","data":my_posts[index_post]}
