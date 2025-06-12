from fastapi.testclient import TestClient
from backend.app.main import app, vector_db


def create_client():
    """Create a TestClient ensuring startup events run."""
    return TestClient(app)

def test_health():
    """Health endpoint should load documents on startup."""
    with create_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
        assert vector_db.count_documents() > 0

def test_chat():
    """/chat should return a response string and search results."""
    with create_client() as client:
        payload = {"message": "hello"}
        response = client.post("/chat", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert isinstance(data.get("results"), list)
