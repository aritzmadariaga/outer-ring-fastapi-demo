
"""
Main FastAPI application entry point.

Initializes the FastAPI app, configures health and readiness endpoints, and includes the API router.
"""

from fastapi import FastAPI, Response, status
from sqlalchemy import text
from src.app.db.session import engine
from src.app.api.api import api_router
from src.app.core.config import settings

app = FastAPI(
    title="Outer Ring FastAPI Base",
    description="A robust, scalable FastAPI backend for spacecraft management.\n\n"
                "This API allows you to create, retrieve, update, and delete spacecraft records, "
                "with full OpenAPI/Swagger documentation, professional error handling, and best practices.",
    version="0.1.0",
    contact={
        "name": "Aritz Madariaga",
        "email": "aritzmadariaga@deusto.es"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/healthz", status_code=200)
def healthz() -> Response:
    """
    Health check endpoint.

    Returns:
        Response: HTTP 200 if the service is healthy.
    """
    return Response(status_code=200)


@app.get("/readyz", status_code=200)
def readyz() -> Response:
    """
    Readiness check endpoint.

    Checks database connectivity. Returns 200 if DB is reachable, 503 otherwise.

    Returns:
        Response: HTTP 200 if the service is ready, 503 if not ready.
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return Response(status_code=200)
    except Exception:
        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

app.include_router(api_router, prefix=settings.API_V1_STR)
