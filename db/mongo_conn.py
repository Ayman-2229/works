
from pymongo import MongoClient, errors
import os
import sys

# Read Mongo URI from .env or default to local MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Create MongoDB client and select database with error handling
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Trigger a server selection to verify connection
    client.server_info()
except errors.ServerSelectionTimeoutError as err:
    print(f"Error: Could not connect to MongoDB server: {err}")
    sys.exit(1)

db = client["expense_explainer"]

# Collections
users_collection = db["users"]
expenses_collection = db["expenses"]
