import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

def build_vector_db():
    if not os.path.exists("data/"):
        os.makedirs("data/")
        print("Created 'data/' directory. Please drop sample PDF files there.")
        return

    loader = DirectoryLoader("data/", glob="./*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()
    
    if not docs:
        print("No PDF documents found in 'data/' folder. Please add at least one PDF.")
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = Chroma.from_documents(
        documents=splits, 
        embedding=embeddings, 
        persist_directory="./chroma_db"
    )
    print(f"Successfully embedded {len(splits)} chunks into ChromaDB.")

if __name__ == "__main__":
    build_vector_db()