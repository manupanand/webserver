from dotenv import load_dotenv,find_dotenv
import redis.asyncio as redis
import os
import asyncio
load_dotenv(find_dotenv())

async def transaction():

    pool =redis.ConnectionPool.from_url(os.getenv("REDIS"))
    client= redis.Redis.from_pool(pool)

    #transacition batch process
    async with client.pipeline(transaction=True) as pipe:
        pipe.set("key-new-1","value1")
        pipe.set("key-new-2","value2")
        result=await pipe.execute()

    print(f"Transacation result:{result}")

    key_value= await client.get("key-new-1")
    print(f"{key_value}")

    #watch banking operation transactions
    await client.watch("balance")

    try:
        #start a transaction
        async with client.pipeline(transaction=True) as pipe:
            balance=await client.get("balance")
           
            # balance =int(bal)
            if balance>=50:
                pipe.decr("balance",50)
                pipe.incr("savings",50)
            res_bal=await pipe.execute()



    except redis.WatchError as error:
        print(f"Transaction failed:{error}")

    # print(f"result balance {res_bal}")

    await client.aclose()

asyncio.run(transaction())