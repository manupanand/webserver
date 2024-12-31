from dotenv import load_dotenv,find_dotenv
import redis.asyncio as redis
import os
import asyncio

load_dotenv(find_dotenv())

async def set_operations():
    pool=redis.ConnectionPool.from_url(os.getenv("REDIS"))
    client=redis.Redis.from_pool(pool)
    # add and remove element 
    await client.sadd("frequent_user","user1","user2")#SADD
    await client.srem("frequent_user","user2")#SREM
    #membership  and set operations
    is_member = await client.sismember("frequent_user","user1")#SISMEMBER
    members=await client.smembers("frequent_user")#SMEMBERS
    intersection=await client.sinter("set1","set2")# SINTER intersection

    print(f" is user1 a member? {is_member}")
    print(f" All users:{members}")
    print(f"Intersection of sets:{intersection}")


    await client.aclose()

asyncio.run(set_operations())