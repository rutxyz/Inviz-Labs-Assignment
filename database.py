from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.property_management

def get_database():
    return db
