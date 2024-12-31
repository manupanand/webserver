import redis.asyncio as redis
from dotenv import load_dotenv,find_dotenv
import os
import asyncio
load_dotenv(find_dotenv())

async def list_operations():
    pool=redis.ConnectionPool.from_url(os.getenv("REDIS"))
    client=redis.Redis.from_pool(pool)

    #add elements to the list
    await client.lpush("taskkey","job1","job2")#LPUSH left push-> job2,job1
    await client.rpush("taskkey","job3")#RPOP right push

    #get list details
    length= await client.llen("taskkey")#LLEN list length
    task_at_index=await client.lindex("taskkey",0)#LINDEX
    print(f"list length :{length},task at index 0 :{task_at_index}")

    #remove elements from list
    left_item=await client.lpop("taskkey")#LPOP remove left item and return it
    right_item=await client.rpop("taskkey")#RPOP remove right item and return it
    print(f"left item is:{left_item}, right item is :{right_item}")

    await client.aclose()


asyncio.run(list_operations())