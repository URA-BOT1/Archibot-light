from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.llm import RobustLLMClient
from backend.services.embedding import load_embedding_model
from backend.services.redis_client import get_redis_client

app = FastAPI()

llm_client = RobustLLMClient()
embedding_model = load_embedding_model()
redis_client = get_redis_client()


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(req: ChatRequest):
    response = llm_client.generate(req.message)
    return {"response": response}
