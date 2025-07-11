import os
from dotenv import load_dotenv

load_dotenv()

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL")
POST_SERVICE_URL = os.getenv("POST_SERVICE_URL")
