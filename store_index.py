from src.helper import load_pdf, text_split, download_hugging_face_embedding
import langchain
from langchain.vectorstores import Pinecone as LangchainPinecone
import pinecone
from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
embedding_model1 = "sentence-transformers/all-MiniLM-L6-v2"

extracted_data = load_pdf("data")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embedding(embedding_model1)


pc = Pinecone(
    api_key=PINECONE_API_KEY
)

index_name = "medical-chatbot"

docsearch = LangchainPinecone.from_texts(
    texts=[t.page_content for t in text_chunks], 
    embedding=embeddings, 
    index_name=index_name
)