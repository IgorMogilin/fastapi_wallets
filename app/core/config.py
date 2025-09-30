import os

from dotenv import load_dotenv

load_dotenv()

# Для тестов используем SQLite, для продакшена PostgreSQL
if os.getenv("TESTING") == "true":
    DATABASE_URL = "sqlite+aiosqlite:///:memory:"
else:
    DATABASE_URL = os.getenv("DATABASE_URL")
