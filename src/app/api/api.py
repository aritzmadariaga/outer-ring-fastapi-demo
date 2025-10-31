from fastapi import APIRouter
from fastapi import APIRouter
from app.api.v1 import spacecraft

api_router = APIRouter()
api_router.include_router(spacecraft.router, prefix="/spacecraft")
