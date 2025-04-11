from rag.create_index import create_chunk_based_faiss_index
from rag.search_index import search_index, retrieve_document
from dotenv import load_dotenv
import os

current_dir = os.path.dirname(__file__)
env_path = os.path.join(current_dir, "..", ".env")

load_dotenv(dotenv_path=env_path)

# Constants
FILE_PATH = os.path.join(current_dir,os.getenv("FILE_PATH2"))

queries2 = [
"Tell me about Davis-Lambert?",
"Which organizations show signs of potential money laundering through complex structures?",
"What irregular transaction patterns are identified for Aurora Financial Services, and why do these raise concerns about potential money laundering?",
]


# Create FAISS index and load chunks
index, chunks = create_chunk_based_faiss_index(file_path=FILE_PATH,force_recreate=False)
print(f"Indexing complete. Number of indexed chunks: {len(chunks)}")


sample_query = queries2[0]
indices, dim = search_index(sample_query, index)

print(indices, dim)

for idx in indices[0]:
    print(f"Index: {idx}, {type(idx)} {type(int(idx))}")
    doc = retrieve_document(int(idx))
    print(f"Docs: {doc}")