from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    title: str
    filename: str
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True