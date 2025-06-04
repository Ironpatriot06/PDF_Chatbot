import os
import numpy as np
from pymongo import MongoClient
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client["pdf_chatbot"]
collection = db["embeddings"]

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

def get_latest_pdf_name():
    latest_chunk = collection.find_one(sort=[("_id", -1)])
    if latest_chunk and "source_pdf" in latest_chunk:
        return latest_chunk["source_pdf"]
    return None

def find_similar_docs(query_embedding, top_k=5):
    current_pdf = get_latest_pdf_name()
    if not current_pdf:
        return []

    docs = list(collection.find({"source_pdf": current_pdf}, {"text": 1, "embedding": 1}))
    for doc in docs:
        doc["similarity"] = cosine_similarity(query_embedding, doc["embedding"])

    sorted_docs = sorted(docs, key=lambda x: x["similarity"], reverse=True)
    return sorted_docs[:top_k]

def answer_question(matched_docs, query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        context = "\n".join([doc["text"] for doc in matched_docs])

        prompt = f"""You are a helpful assistant. Use the following context to answer the question.

Context:
{context}

Question:
{query}
"""

        chat = model.start_chat()
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        print(f"Error answering question: {e}")
        return "Sorry, I couldn't process your question."

