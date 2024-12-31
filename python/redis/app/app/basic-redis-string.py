import redis.asyncio as redis
from dotenv import load_dotenv,find_dotenv
import os
import asyncio
load_dotenv(find_dotenv())
async def basic_string_operations():
   
    pool = redis.ConnectionPool.from_url(os.getenv("REDIS"))
    client=redis.Redis.from_pool(pool)

    #set a string value
    await client.set("username","manu")#SET
    print(f"Username:{await client.get('username')}")#GET-> return a byte object b->Username:b'manu'
    username= await client.get("username")
    if username:
        username=username.decode('utf-8')
    print(f"Username:{username}")

    #increment and decrement operation
    await client.set("age",35)
    await client.incr("age")#INCR
    await client.decr("age")#DECR
    print(f"Age after increment and decrement:{await client.get("age")}")

    #append to a string

    await client.append("username","_developer")#APPEND
    print(f" username updated:{await client.get("username")}")

    #get the length of a string
    length=await client.strlen("username")#STRLEN
    print(f"Length:{length}")


    await client.aclose()

asyncio.run(basic_string_operations())