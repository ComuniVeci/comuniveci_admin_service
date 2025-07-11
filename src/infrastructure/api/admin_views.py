from fastapi import APIRouter, HTTPException
from src.usecases.get_post_statistics import get_post_statistics

admin_router = APIRouter(prefix="/api/admin", tags=["Admin"])

@admin_router.get("/posts/statistics", summary="Estadísticas de publicaciones")
def posts_statistics():
    try:
        return get_post_statistics()
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
