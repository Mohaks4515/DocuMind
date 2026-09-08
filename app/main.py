from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.models import Base
from app.db.database import engine
from app.api.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    yield

    await engine.dispose()


app = FastAPI(
    title="DocuMind",
    description="AI Document Intelligence Platform",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to DocuMind"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


app.include_router(users_router)