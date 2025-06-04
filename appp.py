import streamlit as st
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Mongo client here
try:
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
    client.admin.command('ping')
    st.success("MongoDB connected successfully!")
except Exception as e:
    st.error(f"MongoDB connection error: {e}")

