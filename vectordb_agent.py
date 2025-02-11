import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
load_dotenv()


class VectorDBAgent:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key=os.getenv("OPENAI_API_KEY"))
        self.db = Chroma(persist_directory=os.getenv("VECTORDB_PATH"), embedding_function=self.embeddings)

    def retrieve(self, query):
        docs = self.db.similarity_search(query, k=5)
        return [doc.page_content for doc in docs]

if __name__ == "__main__":
    agent = VectorDBAgent()
    print(agent.retrieve("What is Acies Global Deal with?"))
