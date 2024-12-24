import asyncio
import asyncpg

async def connect_to_db():

    db_url=('dburl')
    try:
        #connection
        # connection= await asyncpg.connect(db_url)
        pool= await asyncpg.create_pool(db_url)
        async with pool.acquire()as connection:
            result=await connection.fetchval("SELECT version();")
        print("Connected to db successfull")

        # query="SELECT * FROM products WHERE id=4;"

        # result= await connection.fetchval(query)
        print(f" Database :{result}")

    except asyncpg.PostgresError as error:
        print(f" error from databse:{error}")   
    except Exception as error:
        print(f"unexpected error:{error}")
    finally:
        if 'conenction' in locals() and not connection.is_closed():
            await connection.close()
            print("connection closed")
#run async function
asyncio.run(connect_to_db())