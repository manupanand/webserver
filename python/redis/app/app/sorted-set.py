from dotenv import load_dotenv,find_dotenv
import redis.asyncio as redis
import os 
import asyncio
load_dotenv(find_dotenv())
async def sorted_set_operations():
    pool= redis.ConnectionPool.from_url(os.getenv("REDIS"))
    client=redis.Redis.from_pool(pool)

    #sort based on score
    # add element with score
    await client.zadd("leaderboard",{"manu":300,"papap":200})#ZADD

    #get range
    top_player=await client.zrange("leaderboard",0,-1,withscores=True)
    rank= await client.zrank("leaderboard","manu")
    print(f"Top players:{top_player}")
    print(f"manu rank:{rank}")

    await client.aclose()







asyncio.run(sorted_set_operations())