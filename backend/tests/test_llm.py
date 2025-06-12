import importlib

from backend.services import llm


def _fake_post(url, json, headers, timeout=10):
    _fake_post.called = {"url": url, "json": json, "headers": headers}
    class Resp:
        def raise_for_status(self):
            pass
        def json(self):
            return {"choices": [{"message": {"content": "ok"}}]}
    return Resp()


def test_groq_fallback(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "key")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("TOGETHER_API_KEY", raising=False)
    importlib.reload(llm)
    monkeypatch.setattr(llm, "openai", None)
    monkeypatch.setattr(llm.httpx, "post", _fake_post)
    client = llm.RobustLLMClient()
    resp = client.generate("hi")
    assert resp == "ok"
    assert _fake_post.called["url"] == llm.RobustLLMClient.groq_url


def test_together_fallback(monkeypatch):
    monkeypatch.setenv("TOGETHER_API_KEY", "key")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    importlib.reload(llm)
    monkeypatch.setattr(llm, "openai", None)
    monkeypatch.setattr(llm.httpx, "post", _fake_post)
    client = llm.RobustLLMClient()
    resp = client.generate("hi")
    assert resp == "ok"
    assert _fake_post.called["url"] == llm.RobustLLMClient.together_url


def test_no_keys(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    monkeypatch.delenv("TOGETHER_API_KEY", raising=False)
    importlib.reload(llm)
    monkeypatch.setattr(llm, "openai", None)
    client = llm.RobustLLMClient()
    assert client.generate("hi") == "No LLM API key configured."
