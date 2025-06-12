"""Utility for loading an embedding model."""

from typing import Iterable, List

try:  # pragma: no cover - optional dependency during tests
    from fastembed import TextEmbedding
except ImportError:  # pragma: no cover
    TextEmbedding = None


class _DummyEmbedder:
    """Fallback embedder used when fastembed is unavailable."""

    def embed(self, texts: Iterable[str]) -> List[List[float]]:
        return [[float(len(t))] for t in texts]


def load_embedding_model(model_name: str = "BAAI/bge-base-en-v1.5"):
    """Load a fastembed TextEmbedding model or return a dummy embedder."""
    if TextEmbedding is None:
        return _DummyEmbedder()
    try:
        return TextEmbedding(model_name=model_name)
    except Exception:  # pragma: no cover - on failure use dummy model
        return _DummyEmbedder()
