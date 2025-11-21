# RAG_QUERY.PY

import os
import faiss
import numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import DB_FOLDER, EMBEDDING_MODEL

# Load embedding model
emb = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def store_documents(text):
    """Split text → embed → store in FAISS."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)
    vectors = emb.embed_documents(chunks)

    # Convert vectors to numpy
    vectors_np = np.array(vectors).astype("float32")

    # Create FAISS index
    index = faiss.IndexFlatL2(vectors_np.shape[1])
    index.add(vectors_np)

    # Save FAISS index
    faiss.write_index(index, f"{DB_FOLDER}/index.faiss")

    # Save chunks
    with open(f"{DB_FOLDER}/chunks.txt", "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n---CHUNK---\n")

def query_rag(question):
    """Query vector DB and return top chunk."""
    # Load FAISS index
    index = faiss.read_index(f"{DB_FOLDER}/index.faiss")

    # Load chunks
    with open(f"{DB_FOLDER}/chunks.txt", "r", encoding="utf-8") as f:
        chunks = f.read().split("---CHUNK---\n")

    # Embed question
    q_vec = emb.embed_query(question)
    q_vec_np = np.array([q_vec]).astype("float32")

    # Search
    D, I = index.search(q_vec_np, 1)
    best_chunk = chunks[I[0][0]]

    return best_chunk
