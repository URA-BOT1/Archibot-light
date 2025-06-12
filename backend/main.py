from fastapi import FastAPI
from pydantic import BaseModel

import json
from pathlib import Path

from backend.services.llm import RobustLLMClient
from backend.services.embedding import load_embedding_model
from backend.services.redis_client import get_redis_client
from backend.services.vector_store import LightVectorDB

app = FastAPI()

llm_client = RobustLLMClient()
embedding_model = load_embedding_model()
redis_client = get_redis_client()
vector_db = LightVectorDB()


def _load_initial_embeddings() -> None:
    """Load sample documents and store embeddings if DB is empty."""
    if vector_db.count_documents() > 0:
        return
    data_path = Path(__file__).resolve().parent / "data" / "documents.json"
    with open(data_path, "r", encoding="utf-8") as f:
        docs = json.load(f)
    texts = [d.get("content", "") for d in docs]
    embeddings = [embedding_model(text) for text in texts]
    vector_db.add_documents(texts, embeddings)


@app.on_event("startup")
def startup_event():
    _load_initial_embeddings()


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):
    query_embedding = embedding_model(req.message)
    results = vector_db.similarity_search(query_embedding)
    response = llm_client.generate(req.message)
    return {
        "response": response,
        "results": [{"text": text, "score": score} for text, score in results],
    }
