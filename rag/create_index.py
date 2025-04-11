import os
from typing import List, Tuple
import sqlite3
import numpy as np
import faiss
from dotenv import load_dotenv
from load_preprocess_data import load_and_split_documents, embed_text_chunks

current_dir = os.path.dirname(__file__)
env_path = os.path.join(current_dir, "..", ".env")

load_dotenv(dotenv_path=env_path)
# Constants
MODEL_NAME = "BAAI/bge-small-en-v1.5"
INDEX_PATH = "faiss_chunk_index.bin"
DB_PATH= "chunks.db"


def store_metadata(documents: List[str ]) -> None:
    """Store document metadata in SQLite."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS documents")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT
            )
        """)
        # Prepare the data to be inserted (just the text)
        document_data = [(doc,) for doc in documents]
        
        # Insert multiple records at once
        cursor.executemany("""
            INSERT INTO documents (text)
            VALUES (?)
        """, document_data)

        conn.commit()
    

def create_chunk_based_faiss_index(
    file_path: str,
    force_recreate: bool = False,  # Flag to force index recreation
    chunk_size: int = 500, chunk_overlap: int = 50
) -> Tuple[faiss.Index, List[str]]:
    """
    Create a FAISS index from embedded text chunks.

    Args:
        file_path (str): Path to text file to index.
        chunk_size (int): Size of text chunks.
        chunk_overlap (int): Overlap between chunks.

    Returns:
        Tuple[faiss.Index, List[str]]: FAISS index and corresponding text chunks.
    """
    chunks = load_and_split_documents(file_path, chunk_size, chunk_overlap)
    # print(chunks) # chunks 
    
    embeddings = embed_text_chunks(chunks)
    dimension = embeddings.shape[1]

    if force_recreate or not os.path.exists(INDEX_PATH):
        index = faiss.IndexHNSWFlat(dimension, 32)
        index.hnsw.efConstruction = 40
        index.add(embeddings)
        faiss.write_index(index, INDEX_PATH)
        print(f"FAISS index created with {len(chunks)} documents and saved to {INDEX_PATH}.")

        store_metadata(chunks)
        print("Metadata stored in SQLite database.")
    else:
        index = faiss.read_index(INDEX_PATH)
        print(f"FAISS index loaded from {INDEX_PATH}.")


    print(f"FAISS chunk-based index created with {index.ntotal} chunks.")
    return index, chunks