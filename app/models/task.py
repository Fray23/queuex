import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import Optional
import uuid
from .base import Base
from .enums import TaskStatus


class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(pg.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type: Mapped[str] = mapped_column(sa.String, nullable=False)
    payload: Mapped[dict] = mapped_column(pg.JSONB, nullable=False)
    status: Mapped[str] = mapped_column(sa.String, nullable=False, default=TaskStatus.pending)
    created_at: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.utcnow)
    completed_at: Mapped[Optional[datetime]] = mapped_column(sa.DateTime, nullable=True)
