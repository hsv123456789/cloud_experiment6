from pymongo import MongoClient
import os

# Get the MongoDB URI from the environment variable
MONGODB_URI = os.environ.get('MONGODB_URI')

# Connect to the MongoDB database
client = MongoClient(MONGODB_URI)

# Access the database named 'mydatabase'
db = client.mydatabase

# Create a new collection named 'mycollection'
collection = db.mycollection

# Insert a new document into the collection
document = {"name": "Test Document", "value": 1}
collection.insert_one(document)

print(f"Document inserted into the collection: {document}")