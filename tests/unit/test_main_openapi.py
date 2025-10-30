from fastapi.testclient import TestClient
from src.app.main import app
from src.app.core.config import settings

client = TestClient(app)


def test_openapi_license_and_routes():
    """Request generated OpenAPI JSON and assert license info and presence of API routes.

    This exercises FastAPI's openapi generation (covers the lines that set license_info and
    the router inclusion in `src/app/main.py`).
    """
    resp = client.get(f"{settings.API_V1_STR}/openapi.json")
    assert resp.status_code == 200
    data = resp.json()

    # License metadata should be present and reference GPL
    assert "info" in data
    assert "license" in data["info"]
    assert "GNU" in data["info"]["license"]["name"]

    # Ensure there are paths under the API prefix (router was included)
    assert any(p.startswith(settings.API_V1_STR) for p in data.get("paths", {}).keys())
