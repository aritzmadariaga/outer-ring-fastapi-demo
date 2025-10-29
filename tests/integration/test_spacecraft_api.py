from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.app.main import app
from src.app.schemas.spacecraft import SpacecraftCreate

client = TestClient(app)

def test_create_spacecraft(db_session: Session):
    spacecraft_data = SpacecraftCreate(registry_code="TEST-001", name="Test Craft")
    response = client.post("/api/v1/spacecraft/", json=spacecraft_data.model_dump())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == spacecraft_data.name
    assert "id" in data

def test_read_spacecraft(db_session: Session):
    response = client.get("/api/v1/spacecraft/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
