from fastapi import APIRouter
from pydantic import UUID4
from app.services.task import TaskService
from app.core.db.connection import session
from app.schemas.task import TaskRead, TaskCreate

router = APIRouter(prefix='/tasks')

@router.post('/', response_model=TaskRead)
async def create_task(task: TaskCreate):

    async with session() as async_session:
        task = await TaskService(async_session).create_task(task)
    return task


@router.get('/{id}', response_model=TaskRead)
async def get_task(id: UUID4):
    async with session() as async_session:
        task = await TaskService(async_session).get_task(task_id=id)
    return task
