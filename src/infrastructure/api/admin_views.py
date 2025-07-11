from fastapi import APIRouter
from src.usecases.get_summary import get_summary

admin_router = APIRouter()

@admin_router.get("/summary")
def summary():
    return get_summary()
