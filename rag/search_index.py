import os
from typing import List, Tuple, Dict, Any
import sqlite3
import numpy as np
import faiss
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv(dotenv_path="../../.env")

# Constants
FILE_PATH = os.getenv("FILE_PATH2")
MODEL_NAME = "BAAI/bge-small-en-v1.5"
INDEX_PATH = "faiss_chunk_index.bin"
DB_PATH= "chunks.db"

def search_index(query: str, index: faiss.Index, top_k: int = 5) -> List[str]:
    """
    Search the FAISS index to retrieve the most relevant text chunks for a query.

    Args:
        query (str): Query string.
        index (faiss.Index): FAISS index to search.
        chunks (List[str]): Original list of text chunks.
        top_k (int): Number of top results to retrieve.

    Returns:
        List[str]: Most relevant text chunks.
    """
    model = SentenceTransformer(MODEL_NAME)
    query_embedding = model.encode([query], normalize_embeddings=True).astype(np.float32)
    distances, indices = index.search(query_embedding, top_k)

    # return [chunks[idx] for idx in indices[0]]
    return indices, distances



def retrieve_document(doc_idx: int) -> Dict[str, Any]:
    """Retrieve document details from the database by index."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT text FROM documents WHERE id=?", (doc_idx + 1,))
        result = cursor.fetchone()
        return {"text": result[0]} if result else {}