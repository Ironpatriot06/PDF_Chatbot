# 📄 PDF Chatbot Assistant

An intelligent **PDF Question Answering Chatbot** built using **LangChain**, **Google Gemini**, and **Streamlit**. This chatbot allows users to upload a PDF file and interact with it conversationally — asking questions and getting accurate answers based on the document's contents.

---

## ✨ Features

- 📥 Upload any PDF document
- 💬 Ask context-aware questions
- 🧠 Intelligent responses powered by **Google Gemini 1.5 Pro**
- 🧾 PDF text chunking & semantic search using **Chroma vector store**
- 🚀 Fast and lightweight Streamlit interface

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pdf-chatbot.git
cd pdf-chatbot
```

Create a Virtual Environment:

For MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```
For Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies: 
```bash
pip install streamlit langchain google-generativeai langchain-google-genai chromadb PyPDF2 tiktoken
```

Put your API key: 
```bash
GOOGLE_API_KEY=your_gemini_api_key
```

To run Streamlit: 
```bash
streamlit run app.py
```

Project Structure is:
pdf_chatbot/
├── app.py              # Main Streamlit app file
├── utils.py            # Helper functions (e.g., for PDF processing)
├── vectorstore/        # Chroma vector database folder
├── requirements.txt    # Python dependencies
└── .env                # Environment variables (API key)


🧪 How It Works

Upload a PDF file via the UI
The text is split into chunks
Chunks are embedded and stored in Chroma
User queries are converted to embeddings
Relevant chunks are retrieved
Gemini generates a response based on the context
