from fastapi import APIRouter
from src.usecases.get_summary import get_admin_summary
from src.domain.schemas import SummaryResponse

admin_router = APIRouter(prefix="/api/admin", tags=["Admin"])

@admin_router.get("/summary", response_model=SummaryResponse)
def get_summary():
    return get_admin_summary()
