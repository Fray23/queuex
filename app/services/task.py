from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db.connection import session
from app.repositories.task import TaskRepository
from app.models.task import TaskModel
from app.schemas.task import TaskCreate
from app.core.amqp.producer import TaskQueueProducer


class TaskService:
    def __init__(self, session: AsyncSession):
        self.repository = TaskRepository(session)
        self.producer = TaskQueueProducer()

    async def create_task(self, task: TaskCreate) -> TaskModel:
        new_task = await self.repository.create_task(
            type=task.type,
            payload=task.payload
        )
        await self.producer.publish_task(
            task_type=task.type,
            task_id=str(new_task.id)
        )
        return new_task

    async def get_task(self, task_id: UUID4) -> TaskModel:
        task = await self.repository.get(id=task_id)
        return task
