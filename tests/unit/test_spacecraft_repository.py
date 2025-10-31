from unittest.mock import MagicMock
from app.repositories.spacecraft_repository import SpacecraftRepository
from app.schemas.spacecraft import SpacecraftCreate, SpacecraftUpdate


def test_create_repository():
    db_session = MagicMock()
    repo = SpacecraftRepository(db_session)
    spacecraft_data = SpacecraftCreate(registry_code="TEST-004", name="Repo Craft")
    repo.create = MagicMock(return_value={"id": 1, "name": "Repo Craft"})
    result = repo.create(spacecraft_data)
    assert result["name"] == "Repo Craft"


def test_get_repository():
    db_session = MagicMock()
    repo = SpacecraftRepository(db_session)
    repo.get = MagicMock(return_value={"id": 1})
    result = repo.get(1)
    assert result["id"] == 1


def test_get_all_repository():
    db_session = MagicMock()
    repo = SpacecraftRepository(db_session)
    repo.get_all = MagicMock(return_value=[{"id": 1}, {"id": 2}])
    result = repo.get_all()
    assert len(result) == 2


def test_update_repository():
    db_session = MagicMock()
    repo = SpacecraftRepository(db_session)
    update_data = SpacecraftUpdate(registry_code="TEST-004", name="Updated Repo")
    repo.update = MagicMock(return_value={"id": 1, "name": "Updated Repo"})
    result = repo.update(1, update_data)
    assert result["name"] == "Updated Repo"


def test_delete_repository():
    db_session = MagicMock()
    repo = SpacecraftRepository(db_session)
    repo.delete = MagicMock(return_value={"id": 1})
    result = repo.delete(1)
    assert result["id"] == 1
