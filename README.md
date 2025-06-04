📄 PDF Chatbot

A Streamlit-based AI chatbot that allows you to upload PDFs and ask questions from them using Google's Gemini Pro and MongoDB for semantic search.

⚙️ Features

📤 PDF Upload: Upload your PDFs for processing.
🧠 Embedding with Gemini: Text chunks from PDFs are embedded using Gemini's embedding model.
💾 MongoDB Storage: Chunks and embeddings are stored in MongoDB for retrieval.
🔍 Semantic Search: Questions are matched to relevant chunks using cosine similarity.
🤖 Answer Generation: Gemini generates answers based on the matched chunks.
🖥️ Screens

1. Upload & Process PDF
Upload any PDF.
Chunks are generated and embedded.
Embeddings are saved in MongoDB.
2. Ask Questions
Enter any question related to the uploaded PDF.
Top-matching chunks are retrieved.
Gemini provides an answer.
🛠️ Installation

1. Clone the Repository
git clone https://github.com/Ironpatriot06/Chatbot.git
cd Chatbot
2. Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
# or

venv\Scripts\activate      # On Windows


3. Install Dependencies
   
pip install -r requirements.txt

5. Create a .env File
   
Add the following environment variables in a file named .env in the root directory:


GOOGLE_API_KEY=your_gemini_api_key

MONGO_URI=your_mongodb_connection_uri

🚀 Running the App

streamlit run app.py

This will launch the Streamlit app in your browser.

Upload a PDF and start chatting with it.

📦 Project Structure

pdf_chatbot/
├── app.py                # Main Streamlit app
├── pdf_utils.py          # PDF reading and chunking logic
├── embed_utils.py        # Embedding logic & MongoDB storage
├── chatbot.py            # Semantic search & answering logic
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables
🧹 Optional Behavior

Keeps only the latest 1–2 PDFs in MongoDB.
Deletes the oldest one's embeddings automatically.
📌 Notes

This app uses google.generativeai for both embeddings and answers.
It stores chunk embeddings in MongoDB for persistent and efficient search.
🙌 Contributions

Pull requests and suggestions are welcome!

Let me know if you want a markdown version to download or want to push this to your GitHub automatically.
