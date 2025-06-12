import sqlite3
import json
import math
from typing import List, Tuple


class LightVectorDB:
    """A lightweight vector store using SQLite to persist embeddings."""

    def __init__(self, db_path: str = "vector_store.db") -> None:
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS documents (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, embedding TEXT)"
            )
            conn.commit()
        finally:
            conn.close()

    def add_documents(self, texts: List[str], embeddings: List[List[float]]) -> None:
        """Store documents and their embeddings in the database."""
        if len(texts) != len(embeddings):
            raise ValueError("texts and embeddings must have the same length")
        conn = sqlite3.connect(self.db_path)
        try:
            conn.executemany(
                "INSERT INTO documents (text, embedding) VALUES (?, ?)",
                [(text, json.dumps(emb)) for text, emb in zip(texts, embeddings)],
            )
            conn.commit()
        finally:
            conn.close()

    def count_documents(self) -> int:
        """Return the number of stored documents."""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute("SELECT COUNT(*) FROM documents")
            return cursor.fetchone()[0]
        finally:
            conn.close()

    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)

    def similarity_search(
        self, query_embedding: List[float], k: int = 4
    ) -> List[Tuple[str, float]]:
        """Return top k documents most similar to the query embedding."""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.execute("SELECT text, embedding FROM documents")
            scores = []
            for text, emb_str in cursor:
                emb = json.loads(emb_str)
                score = self._cosine_similarity(query_embedding, emb)
                scores.append((text, score))
            scores.sort(key=lambda x: x[1], reverse=True)
            return scores[:k]
        finally:
            conn.close()

