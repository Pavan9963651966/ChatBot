import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

def ingest_data():
    documents = ["Acies Global deals with business services and Data analytics"]
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.create_documents(documents)

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"),model ="text-embedding-3-large")
    db = Chroma(persist_directory=os.getenv("VECTORDB_PATH"), embedding_function=embeddings)
    
    db.add_documents(chunks)
    print("Data ingested successfully!")

if __name__ == "__main__":
    ingest_data()
