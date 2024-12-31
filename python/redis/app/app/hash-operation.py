from dotenv import load_dotenv,find_dotenv
import os
import asyncio
import redis.asyncio as redis

load_dotenv(find_dotenv())
async def hash_operation():
    pool= redis.ConnectionPool.from_url(os.getenv("REDIS"))
    client= redis.Redis.from_pool(pool)

    #hash fields
    await client.hset("user:1",mapping={"name":"manu","age":30})#HSET
    name= await client.hget("user:1","name")#HGET
    #retreive all fields
    user_details= await client.hgetall("user:1") #HGETALL

    print(f"Name:{name}")
    print(f"User Details:{user_details}")

    await client.aclose()





asyncio.run(hash_operation())