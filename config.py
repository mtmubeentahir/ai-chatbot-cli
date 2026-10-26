import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()
API_KEY: Optional[str]  = os.getenv("OPENROUTER_API_KEY")
MODEL: str = os.getenv("MODEL", "openrouter/free")
BASE_URL: str = os.getenv("BASE_URL", "https://openrouter.ai/api/v1")

if not API_KEY:
    raise SystemExit("Error: OPENROUTER_API_KEY is missing. Add it to your .env file.")