from fastapi import APIRouter
from app.api.v1.endpoints import widgets

api_router = APIRouter()
api_router.include_router(widgets.router, prefix="/widgets", tags=["widgets"])