from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, Literal


class TaskCreate(BaseModel):
    type: str
    payload: dict


class TaskRead(BaseModel):
    id: UUID
    type: str
    status: Literal["pending", "processing", "done", "failed"]
    created_at: datetime
    completed_at: Optional[datetime] = None
