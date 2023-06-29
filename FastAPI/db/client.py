from pymongo import MongoClient

# db_client = MongoClient().local
# Local

# Base Remota
db_client = MongoClient(
    "mongodb+srv://Emmanuel:1001018117@cluster0.vszhwsc.mongodb.net/?retryWrites=true&w=majority"
).test
