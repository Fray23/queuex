from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from app.models.enums import TaskStatus


class TaskCreate(BaseModel):
    type: str
    payload: dict


class TaskRead(BaseModel):
    id: UUID
    type: str
    status: TaskStatus
    created_at: datetime
    completed_at: Optional[datetime] = None
