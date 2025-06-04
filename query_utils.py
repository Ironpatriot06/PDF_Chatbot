from embed_utils import genai, collection
from numpy import dot, linalg

def get_relevant_chunks(query, pdf_name=None, top_k=3):
    """Retrieve top-k most relevant chunks from MongoDB."""
    try:
        # Embed the query
        response = genai.embed_content(
            model="models/embedding-001",
            content=query,
            task_type="retrieval_query"  # Different from document!
        )
        query_embedding = response['embedding']
        
        # Query MongoDB (filter by PDF if specified)
        filter = {"pdf_name": pdf_name} if pdf_name else {}
        chunks = list(collection.find(filter))
        
        # Calculate cosine similarity
        for chunk in chunks:
            chunk["similarity"] = dot(query_embedding, chunk["embedding"]) / (
                linalg.norm(query_embedding) * linalg.norm(chunk["embedding"])
            )
        
        # Return top-k most similar chunks
        chunks.sort(key=lambda x: x["similarity"], reverse=True)
        return chunks[:top_k]
    
    except Exception as e:
        print(f"🔴 Error during retrieval: {e}")
        return []
