from fastapi import FastAPI
from fastapi.params import Body


app=FastAPI()

@app.get('/')#decorator
async def home_route():
    return {"message":"Hello world!!"}

@app.post('/posts')
def get_post(payLoad : dict =Body(...)):
    print(f"{payLoad}")
    #return {"message":" sucessfully send post"}
    return {"newpost":f"title {payLoad['title']} content: {payLoad['content']}"}

