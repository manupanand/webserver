
from mongoengine import connect
#,Document,StringField
#

#load_dotenv(find_dotenv())

#mongo_url=os.getenv("MONGO_URL")

# connect(host=os.getenv("MONGO_URL"))#,db='restaurants',alias='db1')#alias is given fro name of connection
# #we can provide more number of connect
# #connect(host=mongo_url,db='users',alias='db2')# havr to give seperate name alias
# #disconnect(alias="db2")
# class User(Document):
#     name= StringField()
#     meta={'db_alias':'db1'}#about the connection to db1

connect('project_1')