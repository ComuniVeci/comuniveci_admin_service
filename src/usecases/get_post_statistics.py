import httpx
from src.config import POST_SERVICE_URL

def get_post_statistics() -> dict:
    try:
        response = httpx.get(POST_SERVICE_URL, timeout=5.0)
        response.raise_for_status()
        data = response.json()
        return {
            "approved_posts": data.get("approved", 0),
            "pending_posts": data.get("pending", 0),
            "total_posts": data.get("total", 0)
        }
    except httpx.HTTPError as e:
        raise RuntimeError(f"Error al contactar post-service: {e}")
