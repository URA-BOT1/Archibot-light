from typing import Callable

try:
    from sentence_transformers import SentenceTransformer
except ImportError:  # pragma: no cover
    SentenceTransformer = None


def load_embedding_model(model_name: str = "all-MiniLM-L6-v2") -> Callable[[str], list]:
    """Load a sentence transformer model or return a fallback embedder."""
    if SentenceTransformer is None:
        def dummy_embed(text: str):
            return [len(text)]
        return dummy_embed
    try:
        model = SentenceTransformer(model_name)
        return lambda text: model.encode(text).tolist()  # ensure JSON serializable
    except Exception:
        def dummy_embed(text: str):
            return [len(text)]
        return dummy_embed
