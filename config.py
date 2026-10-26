import os
from dotenv import load_dotenv

load_dotenv()
API_KEY: str | None  = os.getenv("GEMINAI_API_KEY")
MODELS: str = os.getenv("MODELS")
BASE_URL: str = os.getenv("BASE_URL", "https://openrouter.ai/api/v1")

if not API_KEY:
    raise SystemExit("Error: OPENROUTER_API_KEY is missing. Add it to your .env file.")