import httpx
from src.config import AUTH_SERVICE_URL, POST_SERVICE_URL

def get_summary():
    with httpx.Client() as client:
        users = client.get(f"{AUTH_SERVICE_URL}/api/admin/users").json()
        stats = client.get(f"{POST_SERVICE_URL}/api/posts/statistics").json()
    
    return {
        "total_users": len(users),
        "posts_statistics": stats
    }
