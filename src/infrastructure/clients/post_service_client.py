import httpx
from src.config import POST_SERVICE_URL

def get_post_summary():
    try:
        response = httpx.get(f"{POST_SERVICE_URL}/api/posts/summary", timeout=5.0)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as e:
        raise RuntimeError(f"Error de conexión con post-service: {e}")
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"Error en post-service: {e.response.text}")
