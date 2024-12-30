import redis.asyncio as redis
from dotenv import load_dotenv,find_dotenv
import os
import asyncio
load_dotenv(find_dotenv())

async def list_operations():
    pool=redis.ConnectionPool.from_url(os.getenv("REDIS"))