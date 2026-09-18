from fastapi import FastAPI

from app.api.users import router as users_router


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