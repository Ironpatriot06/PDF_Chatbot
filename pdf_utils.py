from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def load_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    raw_text = ""
    for page in reader.pages:
        raw_text += page.extract_text() or ""
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(raw_text)
    return texts

