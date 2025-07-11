from fastapi import APIRouter, HTTPException
from src.usecases.get_post_statistics import get_post_statistics
from src.usecases.get_all_users import get_all_users_from_auth

admin_router = APIRouter(prefix="/api/admin", tags=["Admin"])

@admin_router.get("/posts/statistics", summary="Estadísticas de publicaciones")
def posts_statistics():
    try:
        return get_post_statistics()
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    
@admin_router.get("/users", summary="Lista de todos los usuarios registrados")
def list_users():
    return get_all_users_from_auth()
