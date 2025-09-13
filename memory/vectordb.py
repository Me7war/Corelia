import os
from qdrant_client import QdrantClient

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION = os.getenv("QDRANT_COLLECTION", "corelia-memory")

client = QdrantClient(url=QDRANT_URL)

def upsert_vector(id: str, vector: list, payload: dict = None):
    client.upsert(collection_name=COLLECTION, points=[{"id": id, "vector": vector, "payload": payload or {}}])

def search_vector(vector: list, top_k: int = 5):
    return client.search(collection_name=COLLECTION, query_vector=vector, limit=top_k)
