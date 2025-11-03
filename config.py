import os
from dotenv import load_dotenv

load_dotenv()  # Automatically load environment variables from .env

DOG_API_URL = os.getenv("DOG_API_URL", "https://dog.ceo/api")
TWITCH_URL = os.getenv("TWITCH_URL", "https://www.twitch.tv")