
from typing import List, Tuple


import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter



# Constants
MODEL_NAME = "BAAI/bge-small-en-v1.5"


def load_and_split_documents(file_path: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    """
    Load text file and split it into smaller chunks for indexing.

    Args:
        file_path (str): Path to the raw text file.
        chunk_size (int): Size of each chunk in characters.
        chunk_overlap (int): Overlap between chunks in characters.

    Returns:
        List[str]: List of text chunks.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        raw_text = file.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(raw_text)

    return chunks


def embed_text_chunks(chunks: List[str], model_name: str = MODEL_NAME) -> np.ndarray:
    """
    Embed text chunks using SentenceTransformer.

    Args:
        chunks (List[str]): List of text chunks.
        model_name (str): SentenceTransformer model name.

    Returns:
        np.ndarray: Array of embeddings.
    """
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, batch_size=64, show_progress_bar=True)
    return np.array(embeddings, dtype=np.float32)