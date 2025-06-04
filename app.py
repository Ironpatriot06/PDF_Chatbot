import os
import streamlit as st
from pdf_utils import load_pdf
from embed_utils import embed_and_store
from chatbot import answer_question, find_similar_docs
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Streamlit page
st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title("📄 Chat with your PDF")

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

# Handle uploaded PDF
if uploaded_file:
    with st.spinner("Reading and processing the PDF..."):
        try:
            texts = load_pdf(uploaded_file)  # should return list of text chunks
            stored_ids = embed_and_store(texts, uploaded_file.name)  # pass pdf_name here
            if stored_ids:
                st.success(f"✅ PDF processed and stored! {len(stored_ids)} chunks saved.")
            else:
                st.error("❌ No chunks were stored.")
        except Exception as e:
            st.error(f"Error processing PDF: {str(e)}")

# Ask a question
user_question = st.text_input("Ask a question from the PDF:")

if user_question:
    with st.spinner("Searching for answers..."):
        try:
            # 1. Embed user question
            embedding_response = genai.embed_content(
                model="models/embedding-001",
                content=user_question,
                task_type="retrieval_query"
            )
            query_embedding = embedding_response["embedding"]

            # 2. Find relevant chunks using cosine similarity
            matched_docs = find_similar_docs(query_embedding)

            # 3. Use Gemini to answer the question based on chunks
            response = answer_question(matched_docs, user_question)

            # 4. Display the result
            st.markdown("### 📢 Answer")
            st.write(response)

            with st.expander("🔍 See relevant PDF sections"):
                for doc in matched_docs:
                    st.write(doc["text"])
                    st.divider()

        except Exception as e:
            st.error(f"❌ Error answering question: {str(e)}")

