from langflow import CustomComponent
from pymongo import MongoClient
import numpy as np
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

class MongoRetriever(CustomComponent):
    display_name = "MongoRetriever"

    def build_config(self):
        return {
            "query": {"display_name": "Query"},
            "top_k": {"display_name": "Top K", "default": 3}
        }

    def build(self, query: str, top_k: int = 3):
        # Embed the user query
        embedding_response = genai.embed_content(
            model="models/embedding-001",
            content=query,
            task_type="retrieval_query"
        )
        query_embedding = embedding_response["embedding"]

        # Connect to MongoDB
        client = MongoClient(os.getenv("MONGO_URI"))  # example: mongodb://localhost:27017
        db = client["docdb"]
        collection = db["documents"]

        # Retrieve and rank chunks
        docs = list(collection.find({}, {"text": 1, "embedding": 1}))
        for doc in docs:
            doc['similarity'] = cosine_similarity(query_embedding, doc['embedding'])

        top_docs = sorted(docs, key=lambda x: x['similarity'], reverse=True)[:top_k]

        # Combine matched texts
        context = "\n".join([doc['text'] for doc in top_docs])
        return context

