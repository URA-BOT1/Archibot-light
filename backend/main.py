from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import json
from pathlib import Path

from backend.services.llm import RobustLLMClient
from backend.services.embedding import load_embedding_model
from backend.services.vector_store import LightVectorDB

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    _load_initial_embeddings()
    yield


app = FastAPI(lifespan=lifespan)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir les fichiers statiques du frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

llm_client = RobustLLMClient()
embedding_model = load_embedding_model()
vector_db = LightVectorDB()


def _load_initial_embeddings() -> None:
    """Load sample documents and store embeddings if DB is empty."""
    if vector_db.count_documents() > 0:
        return
    data_path = Path(__file__).resolve().parent / "data" / "documents.json"
    with open(data_path, "r", encoding="utf-8") as f:
        docs = json.load(f)
    texts = [d.get("content", "") for d in docs]
    # FastEmbed can embed a batch of texts at once
    embeddings = [emb.tolist() if hasattr(emb, "tolist") else list(emb)
                  for emb in embedding_model.embed(texts)]
    vector_db.add_documents(texts, embeddings)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    """Serve the frontend"""
    from fastapi.responses import FileResponse
    return FileResponse('frontend/index.html')


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):
    query_embedding = list(embedding_model.embed([req.message]))[0]
    if hasattr(query_embedding, "tolist"):
        query_embedding = query_embedding.tolist()
    results = vector_db.similarity_search(query_embedding)
    response = llm_client.generate(req.message)
    return {
        "response": response,
        "results": [{"text": text, "score": score} for text, score in results],
    }
