import os
import uuid
from pymongo import MongoClient
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client["pdf_chatbot"]
collection = db["embeddings"]

def embed_and_store(text_chunks, pdf_name="default"):
    stored_ids = []

    # Optional: delete old PDFs if needed, as you had before

    for chunk in text_chunks:
        try:
            embedding_response = genai.embed_content(
                model="models/embedding-001",
                content=chunk,
                task_type="retrieval_document"
            )
            embedding = embedding_response["embedding"]

            doc_id = str(uuid.uuid4())
            doc = {
                "_id": doc_id,
                "text": chunk,
                "embedding": embedding,
                "source_pdf": pdf_name
            }

            collection.insert_one(doc)
            stored_ids.append(doc_id)

        except Exception as e:
            print(f"Error storing chunk: {e}")

    return stored_ids








