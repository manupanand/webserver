from pymongo import MongoClient
from dotenv import load_dotenv,find_dotenv
import os
import pprint



load_dotenv(find_dotenv())# will find env
mongo_url=os.getenv("MONGO_URL")


#connect to database
client=MongoClient(mongo_url)

#view
databases=client.list_database_names()
# print(databases)
#accessng the dtabase client["databasename"] like list/dictionary
test_database=client.test
#list collection
collections=test_database.list_collection_names()
# print(collections)

def insert_test_doc():
    #accesing a collection-test
    collection=test_database.test
    #insert document -python dictionary-bson -it will converted to type
    test_document={
        "name":"Manu",
        "type":"Test"
    }
    #collection.insert_one(test_document) returns _id to get it.insterted_id
    inserted_id=collection.insert_one(test_document).inserted_id
    print(inserted_id)

#create a database that doesnt exists -monogo will create it -name:production
production=client.production
person_collection=production.person_collection

#insert_test_doc()

def create_document():
    #craete a document from group
    first_names=["Manu","Neeraj","Sruthi","niko"]
    last_names=["anand","pappan","renjan","aro"]
    ages=[25,26,25,25]
    docs=[]
    #zip gives a corresponding tuple in same indices
    for first_name,last_name,age in zip(first_names,last_names,ages):
        doc={
            "first_name":first_name,
            "last_name":last_name,
            "age":age
        }
        #person_collection.insert_one(doc)
        docs.append(doc)
    person_collection.insert_many(docs)

#create_document()
#read from database person collection
#find() - allow to pass {} to find usinf id/parmater -if () empty it returns all
printer = pprint.PrettyPrinter()
def find_all_person():
    people =person_collection.find()# return cursor able to iterate over - convert to list or loop 

    for person in people:
        printer.pprint(person)


#find_all_person()

#find one person -pass key and value
def find_one_person():
    man=person_collection.find_one({"first_name":"Manu"})
    printer.pprint(man)

#find_one_person()

def count_all_people():
    # anotehr method person_collection.find().count()
    count =person_collection.count_documents(filter={})#filter empty returns all
    print(" number of people",count)

#count_all_people()

#find by id
def get_person_by_id(person_id):# we need to convet string person_id to bson using ObjectId()
    from bson.objectid import ObjectId

    _id= ObjectId(person_id)#convert to bson
    person=person_collection.find_one({"_id":_id})
    printer.pprint(person)
# get_person_by_id("6770389ce18e6ea8a1bff480")

#search for specific age range query operator $and $gte greater than

def get_age_range(min_age,max_age):
    query={"$and":[
            {"age":{"$gte":min_age}},
            {"age":{"$lte":max_age}}
        ]}
    
    people=person_collection.find(query).sort("age")
    for person in people:
        printer.pprint(person)

#get_age_range(22,25)

#get specified columns only

def project_column():
    column={"_id":0,"age":1,"last_name":1}
    people=person_collection.find({},column)
    for person in people:
        printer.pprint(person)

# project_column()

#update by id
def update_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id =ObjectId(person_id)

    all_updates={
        "$set":{"new_field":True},#set new parameter
        "$inc":{"age":1},#increment
        "$rename":{"first_name":"first","last_name":"last"}
    }
    person_collection.update_one({"_id":_id},all_updates)

    # to unset or delet a field
    #person_collection.update_one({"_id":_id},{"$unset":{"new_field":""}})


#update_person_by_id("6770389ce18e6ea8a1bff480")

#update allcontact and keep old id
#replace will work
def replace_one(person_id):
    from bson.objectid import ObjectId
    _id =ObjectId(person_id)

    new_doc={
        "first_name":"new name",
        "last_name":"last name",
        "age":100
    }
    person_collection.replace_one({"_id":_id},new_doc)

#replace_one("6770389ce18e6ea8a1bff480")


def delete_doc_by_id(person_id):
    from bson.objectid import ObjectId

    _id=ObjectId(person_id)

    person_collection.delete_one({"_id":_id})
    #delete many
    #person_collection.delete_many({})

#delete_doc_by_id("6770389ce18e6ea8a1bff483")

#relationship - foreign key join
address={
    "_id":"6770389ce18e6ea8a1bff480",
    "street":"Bay street",
    "number":2566,
    "country":"India"
}
def add_address(person_id,address):
    from bson.objectid import ObjectId
    _id=ObjectId(person_id)

    person_collection.update_one({"_id":_id},{"$addToSet":{"address":address}})

#add_address("6770389ce18e6ea8a1bff480",address)

def add_address_relationship(person_id,address):
    from bson.objectid import ObjectId
    _id=ObjectId(person_id)

    address=address.copy()
    address["owner_id"]=person_id
    address_collection=production.address
    address_collection.insert_one(address)


    