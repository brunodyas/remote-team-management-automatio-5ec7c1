from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/task_002', tags=['feature'])

@router.get('/status')
def feature_task_002_status():
    return {'ok': True, 'feature': 'API e lógica em server/ — feature core', 'task': 'task-002'}
