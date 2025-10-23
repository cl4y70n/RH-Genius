import chromadb
from chromadb.config import Settings

def create_vectorstore():
    client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./data/vectorstore"))
    collection = client.get_or_create_collection(name="faq_collection")
    return collection

def add_faqs(collection, faqs, embeddings):
    for faq, emb in zip(faqs, embeddings):
        collection.add(documents=[faq["resposta"]], embeddings=[emb])

def retrieve_answer(collection, query_embedding, top_k=1):
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results['documents'][0][0]