from fastapi import FastAPI, Response
from src.app.api.api import api_router
from src.app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/healthz", status_code=200)
def healthz() -> Response:
    return Response(status_code=200)

@app.get("/readyz", status_code=200)
def readyz() -> Response:
    # TODO: Add logic to check DB connection, etc.
    return Response(status_code=200)

app.include_router(api_router, prefix=settings.API_V1_STR)
