from fastapi import FastAPI

from app.api.users import router as users_router
from app.api.auth import router as auth_router
from app.api.documents import router as documents_router


app = FastAPI(
    title="DocuMind",
    description="AI Document Intelligence Platform",
    version="1.0.0",
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
app.include_router(auth_router)
app.include_router(documents_router)