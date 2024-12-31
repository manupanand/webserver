from dotenv import load_dotenv,find_dotenv
import redis.asyncio as redis
import asyncio
import os

load_dotenv(find_dotenv())
async def key_management():
    pool =redis.ConnectionPool.from_url(os.getenv("REDIS"))
    client=redis.Redis.from_pool(pool)

    #set keys with patterns

    await client.set("user:1:name","manu")
    await client.set("user:2:name","Bob")

    #retreive by  pattern
    keys = await client.keys("user:*")
    print(f"keys matching the patern:{keys}")
    await client.expire("user:1:name",10)


    await client.aclose()
asyncio.run(key_management())