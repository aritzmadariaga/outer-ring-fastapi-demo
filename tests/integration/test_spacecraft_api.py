from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.app.main import app
from src.app.schemas.spacecraft import SpacecraftCreate

client = TestClient(app)

def test_create_spacecraft(db_session: Session):
    import uuid
    unique_code = f"TEST-{uuid.uuid4()}"
    spacecraft_data = SpacecraftCreate(registry_code=unique_code, name="Test Craft")
    response = client.post("/api/v1/spacecraft/", json=spacecraft_data.model_dump())
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == spacecraft_data.name
    assert "id" in data
def test_update_spacecraft_not_found(db_session: Session):
    update_data = {"registry_code": "NOT-FOUND", "name": "No existe"}
    response = client.put("/api/v1/spacecraft/99999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Spacecraft not found"

def test_delete_spacecraft_not_found(db_session: Session):
    response = client.delete("/api/v1/spacecraft/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Spacecraft not found"

def test_read_spacecraft(db_session: Session):
    response = client.get("/api/v1/spacecraft/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
