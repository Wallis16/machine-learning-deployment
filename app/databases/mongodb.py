# from dotenv import load_dotenv, find_dotenv
from fastapi import Depends, HTTPException
from pymongo.errors import ServerSelectionTimeoutError
from pymongo import MongoClient

import os
#from dotenv import load_dotenv, find_dotenv
#load_dotenv(find_dotenv())

user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')

# Dependency to get the MongoDB client
async def get_mongo_client():
    try:
        mongo_uri = f'mongodb+srv://{user}:{password}@{database}.hi7evkw.mongodb.net/'
        client = MongoClient(mongo_uri)
        yield client
    finally:
        client.close()

# Dependency to get the MongoDB database
async def get_database(client = Depends(get_mongo_client)):
    try:
        yield client[database]
    except ServerSelectionTimeoutError:
        raise HTTPException(status_code=500, detail='Could not connect to database')
