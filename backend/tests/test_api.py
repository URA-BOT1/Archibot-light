from fastapi.testclient import TestClient
from backend.main import app, vector_db


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
    """Test /chat endpoint returns a valid response and search results."""
    with create_client() as client:
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


def test_no_redis_client_variable():
    """Ensure redis_client variable has been removed from backend.main."""
    import importlib
    main = importlib.import_module("backend.main")
    assert not hasattr(main, "redis_client")

