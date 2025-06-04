from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_db():
    MONGO_URI = os.getenv("MONGO_URI")  # Store in .env file
    client = MongoClient(MONGO_URI)
    db = client["pdf_chatbot_db"]  # Database name
    return db

# Example usage
db = get_db()
embeddings_collection = db["embeddings"]  # Collection for embeddings
