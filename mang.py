from pymongo import MongoClient
import numpy as np

# Setup MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["docdb"]
collection = db["documents"]

# Store documents
def store_embeddings(texts, embeddings):
    for text, embedding in zip(texts, embeddings):
        doc = {"text": text, "embedding": embedding}
        collection.insert_one(doc)

# Simple cosine similarity search
def find_similar_docs(query_embedding, top_k=5):
    all_docs = list(collection.find({}))
    for doc in all_docs:
        doc['similarity'] = cosine_similarity(query_embedding, doc['embedding'])
    sorted_docs = sorted(all_docs, key=lambda x: x['similarity'], reverse=True)
    return sorted_docs[:top_k]

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

