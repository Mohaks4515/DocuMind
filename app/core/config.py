import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "DocuMind")

    POSTGRES_USER = os.getenv("POSTGRES_USER", "documind")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "documind")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "documind")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

    DATABASE_URL = (
        f"postgresql+asyncpg://"
        f"{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}"
        f"/{POSTGRES_DB}"
    )


settings = Settings()