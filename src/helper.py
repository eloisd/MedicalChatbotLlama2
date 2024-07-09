from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


# Extract text from PDFs
def load_pdf (data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    return documents


def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


def download_hugging_face_model(embedding_model):
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
    return embeddings

