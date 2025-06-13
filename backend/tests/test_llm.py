import importlib

from backend.services import llm
from fastapi import HTTPException
import logging


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


def test_openai_error(monkeypatch, caplog):
    monkeypatch.setenv("OPENAI_API_KEY", "key")
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    monkeypatch.delenv("TOGETHER_API_KEY", raising=False)
    importlib.reload(llm)
    class FakeOpenAI:
        class ChatCompletion:
            @staticmethod
            def create(*args, **kwargs):
                raise RuntimeError("boom")
    monkeypatch.setattr(llm, "openai", FakeOpenAI)
    client = llm.RobustLLMClient()
    with caplog.at_level(logging.ERROR):
        resp = client.generate("hi")
    assert resp == "LLM request failed"
    assert "boom" in caplog.text


def test_raise_http_exception(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "key")
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    monkeypatch.delenv("TOGETHER_API_KEY", raising=False)
    importlib.reload(llm)
    class FakeOpenAI:
        class ChatCompletion:
            @staticmethod
            def create(*args, **kwargs):
                raise RuntimeError("boom")
    monkeypatch.setattr(llm, "openai", FakeOpenAI)
    client = llm.RobustLLMClient()
    try:
        client.generate("hi", raise_http=True)
    except HTTPException as exc:
        assert exc.status_code == 500
    else:  # pragma: no cover
        assert False, "HTTPException not raised"
