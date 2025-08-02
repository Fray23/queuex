from fastapi import APIRouter

router = APIRouter(prefix='/tasks')

@router.get('/')
async def hello_world():
    return {'hello': 'world'}
