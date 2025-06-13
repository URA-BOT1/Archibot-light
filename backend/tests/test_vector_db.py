import json
import os
import sqlite3
import tempfile

from backend.services.vector_store import LightVectorDB


def _temp_db_path():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.close()
    return tmp.name


def test_add_documents_and_storage():
    path = _temp_db_path()
    try:
        db = LightVectorDB(path)
        texts = ["doc1", "doc2"]
        embeds = [[1.0, 0.0], [0.0, 1.0]]
        db.add_documents(texts, embeds)
        assert db.count_documents() == 2

        with sqlite3.connect(path) as conn:
            rows = conn.execute("SELECT text, embedding FROM documents ORDER BY id").fetchall()
        assert rows[0][0] == "doc1"
        assert json.loads(rows[0][1]) == [1.0, 0.0]
        assert rows[1][0] == "doc2"
        assert json.loads(rows[1][1]) == [0.0, 1.0]
    finally:
        os.remove(path)


def test_count_documents():
    path = _temp_db_path()
    try:
        db = LightVectorDB(path)
        assert db.count_documents() == 0
        db.add_documents(["a"], [[0.1, 0.2]])
        assert db.count_documents() == 1
    finally:
        os.remove(path)


def test_similarity_search_order():
    path = _temp_db_path()
    try:
        db = LightVectorDB(path)
        texts = ["a", "b", "c"]
        embeds = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
        db.add_documents(texts, embeds)
        results = db.similarity_search([1.0, 0.0], k=3)
        ordered = [text for text, _ in results]
        assert ordered == ["a", "c", "b"]
        scores = [score for _, score in results]
        assert scores == sorted(scores, reverse=True)
    finally:
        os.remove(path)
