from fastapi import FastAPI
from src.infrastructure.api.routes import router as api_router

app = FastAPI(title="ComuniVeci Admin Service")

app.include_router(api_router)
