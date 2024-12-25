import asyncpg
import asyncio
import os
from dotenv import load_dotenv
from typing  import Optional
import pandas.io.sql as psql
load_dotenv()
#db config
db_url=os.getenv("DB_URL")

conn_pool:Optional[asyncpg.Pool]=None

async def init_postgres()-> asyncpg.Pool:
    global conn_pool
    try:
        conn_pool= await asyncpg.create_pool(db_url)
        return conn_pool
        # async with conn_pool.acquire() as connection:

            # query="SELECT * FROM posts;"
            # result = await connection.fetchval(query)
            # table= psql.read_sql(query,connection)
            # print(table)
        
    except asyncpg.PostgresError as pg_error:
        print(f"Postgress error :{pg_error}")
    except Exception as error:
        print(f"Error while connecting to database:{error}")

# async def close_postgres()-> None:

# @asynccontextmanager
# async def lifespan(app:FastAPI):
#     await #init postgres
#     yield
#     await #close postgres
asyncio.run(init_postgres())