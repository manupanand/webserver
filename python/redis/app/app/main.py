import redis
from dotenv import load_dotenv,find_dotenv
import os
load_dotenv(find_dotenv())

#connetion
redis_client=redis.from_url(os.getenv("REDIS"))

# redis_client=redis.Redis( 
#     host=os.getenv("REDIS_HOST"),
#     port=os.getenv("REDIS_PORT"),
#     decode_responses=os.getenv("REDIS_DECODE_RESPONSE"),
#     username=os.getenv("REDIS_USER_NAME"),
#     password=os.getenv("REDIS_PASSWORD"),
# )

#test connection
'''Connection test
from redis,Redis class create instance
'''
conn=redis_client.ping()
print(conn)
succc=redis_client.set('foo',"test")

res=redis_client.get('foo')
print(res)
re=redis_client.delete('foo')
print(re)