from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_chat():
    payload = {"message": "hello"}
    response = client.post("/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert "results" in data
    assert isinstance(data["results"], list)
    if data["results"]:
        assert "text" in data["results"][0]
        assert "score" in data["results"][0]
