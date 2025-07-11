from fastapi import APIRouter
from .admin_views import admin_router

router = APIRouter()
router.include_router(admin_router)
