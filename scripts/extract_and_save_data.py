# Importing libs
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests

# Function to connect to mongoDb
def connect_mongo(uri):
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("✅ Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(f"❌ Error!\n {e}")

# Function to create and/or connect to a database
def create_connect_db(client, db_name):
    try:
        if db_name not in client.list_database_names():
            db = client[db_name]
            print("🔨 Database not found, creating it...")
            print("✅ Database successfuly created")
            return db
        else:
            print("🤔 A database with this name already exists...")
    except Exception as e:
        print(f"❌ Error!\n {e}")


# Function to create and/or connect to a collection
def create_connect_collection(db, cl_name):
    try:
        if cl_name not in db.list_collection_names():
            collection = db[cl_name]
            print("🔨 Collection not found, creating it...")
            print("✅ Collection successfuly created")
            return collection
        else:
            print("🤔 A collection with this name already exists...")
    except Exception as e:
        print(f"❌ Error!\n {e}")


# Function to extract data from API
def extract_api_data(url):
    try:
        r = requests.get(url=url)
        print("✅ Request made successfuly!")
        return r.json()
    except Exception as e:
        print(f"❌ Error!\n {e}")

# Function to insert data in the collection
def insert_data(cl, data):
    result = cl.insert_many(data)
    n_docs_inseridos = len(result.inserted_ids)
    print(f"🚀 {n_docs_inseridos} documents were added!")
    return n_docs_inseridos 

