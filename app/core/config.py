import os

from dotenv import load_dotenv

load_dotenv()

if os.getenv("TESTING") == "true":
    DATABASE_URL = "sqlite+aiosqlite:///:memory:"
else:
    DATABASE_URL = os.getenv("DATABASE_URL")
