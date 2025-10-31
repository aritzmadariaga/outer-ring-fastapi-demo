from fastapi.testclient import TestClient
from types import SimpleNamespace
import pytest

import app.main as main_mod
from app.core.config import settings


client = TestClient(main_mod.app)


def test_readyz_returns_503_when_db_unreachable(monkeypatch):
    """Simulate DB connection error to exercise the except branch in `readyz`.

    This will cover lines that return HTTP 503 in `src/app/main.py`.
    """

    class BadConn:
        def __enter__(self):
            raise Exception("db down")

        def __exit__(self, exc_type, exc, tb):
            return False

    # Replace engine.connect to return a context manager that raises on enter
    monkeypatch.setattr(main_mod.engine, "connect", lambda *a, **k: BadConn())

    resp = client.get("/readyz")
    assert resp.status_code == 503
