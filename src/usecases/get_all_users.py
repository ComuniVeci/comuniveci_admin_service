import requests
from fastapi import HTTPException
from src.config import AUTH_SERVICE_URL

def get_all_users_from_auth():
    try:
        response = requests.get(f"{AUTH_SERVICE_URL}/api/auth/users", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Error al contactar auth-service: {e}")