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

def test_chat(monkeypatch):
    """Test /chat endpoint returns a valid response and uses docs in the prompt."""
    captured = {}

    def fake_generate(prompt: str):
        captured["prompt"] = prompt
        return "ok"

    import backend.main as main
    monkeypatch.setattr(main.llm_client, "generate", fake_generate)

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

    assert "Context:" in captured["prompt"]
    assert "Question: hello" in captured["prompt"]
    if data["results"]:
        assert data["results"][0]["text"] in captured["prompt"]


def test_no_redis_client_variable():
    """Ensure redis_client variable has been removed from backend.main."""
    import importlib
    main = importlib.import_module("backend.main")
    assert not hasattr(main, "redis_client")

