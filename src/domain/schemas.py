from pydantic import BaseModel

class SummaryResponse(BaseModel):
    total_users: int
    total_posts: int
    approved_posts: int
    pending_posts: int
