from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.app.main import app
from src.app.schemas.spacecraft import SpacecraftCreate, SpacecraftUpdate
import pytest

client = TestClient(app)

@pytest.mark.usefixtures("db_session")
def test_read_spacecrafts():
    response = client.get("/api/v1/spacecraft/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.usefixtures("db_session")
def test_update_spacecraft():
    import uuid
    unique_code = f"TEST-{uuid.uuid4()}"
    spacecraft_data = SpacecraftCreate(registry_code=unique_code, name="Update Craft")
    create_resp = client.post("/api/v1/spacecraft/", json=spacecraft_data.model_dump())
    assert create_resp.status_code == 200
    spacecraft_id = create_resp.json()["id"]
    # Actualizar
    update_data = SpacecraftUpdate(registry_code=unique_code, name="Updated Name")
    update_resp = client.put(f"/api/v1/spacecraft/{spacecraft_id}", json=update_data.model_dump())
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "Updated Name"

@pytest.mark.usefixtures("db_session")
def test_delete_spacecraft():
    # Crear primero una nave
    spacecraft_data = SpacecraftCreate(registry_code="TEST-003", name="Delete Craft")
    create_resp = client.post("/api/v1/spacecraft/", json=spacecraft_data.model_dump())
    assert create_resp.status_code == 200
    spacecraft_id = create_resp.json()["id"]
    # Eliminar
    delete_resp = client.delete(f"/api/v1/spacecraft/{spacecraft_id}")
    assert delete_resp.status_code == 200
    # Comprobar que ya no existe
    get_resp = client.get(f"/api/v1/spacecraft/{spacecraft_id}")
    assert get_resp.status_code == 404
