import redis.asyncio as redis
from dotenv import load_dotenv,find_dotenv
import os
import asyncio

load_dotenv(find_dotenv())

async def pub_sub():
    pool= redis.ConnectionPool.from_url(os.getenv("REDIS"))
    client=redis.Redis.from_pool(pool)

    #subscribe
    pubsub=client.pubsub()
    await pubsub.subscribe("notifications")

    #simlating a subscriber
    async for message in pubsub.listen():
        print(f"Recieved :{message}")

    #publisher
    await client.publish("notifications","hello subscrober")


    await client.aclose()

asyncio.run(pub_sub())