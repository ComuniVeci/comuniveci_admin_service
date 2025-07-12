from fastapi import FastAPI
from src.infrastructure.api.routes import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ComuniVeci Admin Service")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Puedes poner ["*"] para permitir todo temporalmente
    allow_credentials=True,
    allow_methods=["*"],  # Puedes restringir a ["GET", "POST"] si prefieres
    allow_headers=["*"],
)

app.include_router(api_router)
