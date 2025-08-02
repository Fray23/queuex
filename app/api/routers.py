from fastapi import APIRouter
from app.api.handlers.tasks import router

api_router = APIRouter()
api_router.include_router(router)
