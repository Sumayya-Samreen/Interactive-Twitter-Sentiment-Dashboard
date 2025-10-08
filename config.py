from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env file

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
TRACK_KEYWORDS = os.getenv("TRACK_KEYWORDS").split(",")
MAX_TWEETS = int(os.getenv("MAX_TWEETS", 50))
USE_MOCK_DATA = os.getenv("USE_MOCK_DATA", "False").lower() == "true"
