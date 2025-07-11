from src.infrastructure.clients.post_service_client import get_post_summary

def get_admin_summary():
    post_data = get_post_summary()
    # Aquí podrías agregar también datos de auth_service si decides integrarlo

    return {
        "total_posts": post_data.get("total", 0),
        "approved_posts": post_data.get("approved", 0),
        "pending_posts": post_data.get("pending", 0),
        "total_users": 0  # Cambiar si decides agregar integración con auth_service
    }

