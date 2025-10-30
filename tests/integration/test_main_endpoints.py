from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200

def test_readyz():
    response = client.get("/readyz")
    assert response.status_code == 200
