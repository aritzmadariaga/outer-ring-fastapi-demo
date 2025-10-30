from unittest.mock import MagicMock
import pytest
from app.services.spacecraft_service import SpacecraftService
from app.schemas.spacecraft import SpacecraftCreate, SpacecraftUpdate

@pytest.mark.usefixtures("db_session")
def test_get_spacecraft_service():
    db_session = MagicMock()
    service = SpacecraftService(db_session)
    # Simular que el repo devuelve un objeto
    service.repository.get = MagicMock(return_value={"id": 1, "name": "Test"})
    result = service.get_spacecraft(1)
    assert result["id"] == 1

@pytest.mark.usefixtures("db_session")
def test_get_all_spacecrafts_service():
    db_session = MagicMock()
    service = SpacecraftService(db_session)
    service.repository.get_all = MagicMock(return_value=[{"id": 1}, {"id": 2}])
    result = service.get_all_spacecrafts()
    assert len(result) == 2

@pytest.mark.usefixtures("db_session")
def test_update_spacecraft_service():
    db_session = MagicMock()
    service = SpacecraftService(db_session)
    service.repository.update = MagicMock(return_value={"id": 1, "name": "Updated"})
    update_data = SpacecraftUpdate(registry_code="TEST-001", name="Updated")
    result = service.update_spacecraft(1, update_data)
    assert result["name"] == "Updated"

@pytest.mark.usefixtures("db_session")
def test_delete_spacecraft_service():
    db_session = MagicMock()
    service = SpacecraftService(db_session)
    service.repository.delete = MagicMock(return_value={"id": 1})
    result = service.delete_spacecraft(1)
    assert result["id"] == 1
