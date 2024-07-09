from dotenv import load_dotenv
import os
from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embedding
from src.prompts import *
import langchain
from langchain.vectorstores import Pinecone as LangchainPinecone
import pinecone
from pinecone import Pinecone
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers 

app = Flask(__name__)

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

embedding_model1 = "sentence-transformers/all-MiniLM-L6-v2"

embeddings = download_hugging_face_embedding(embedding_model1)

pc = Pinecone(
    api_key=PINECONE_API_KEY
)

index_name = "medical-chatbot"

docsearch = LangchainPinecone.from_existing_index(index_name=index_name, embedding=embeddings)


PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q8_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.4})

qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)


@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])

if __name__ == '__main__':
    app.run(debug=True)
