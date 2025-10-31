from unittest.mock import MagicMock
from app.services.spacecraft_service import SpacecraftService
from app.schemas.spacecraft import SpacecraftCreate


def test_create_spacecraft_service():
    db_session = MagicMock()
    service = SpacecraftService(db_session)
    spacecraft_data = SpacecraftCreate(registry_code="TEST-001", name="Test Craft")
    service.create_spacecraft(spacecraft_data)
    assert db_session.add.called
    assert db_session.commit.called
    assert db_session.refresh.called
