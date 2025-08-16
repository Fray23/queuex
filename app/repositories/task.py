from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task import TaskModel


class TaskRepository:
    def __init__(self, session) -> None:
        self.session: AsyncSession = session

    async def create_task(self, type: str, payload: dict) -> TaskModel:
        task = TaskModel(
            type=type,
            payload=payload,
        )
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task

    async def get(self, id) -> TaskModel:
        q = select(TaskModel).where(TaskModel.id==id)
        task = await self.session.execute(q)
        return task.scalar()
