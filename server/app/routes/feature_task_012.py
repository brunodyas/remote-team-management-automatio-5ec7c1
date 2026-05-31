from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/task_012', tags=['feature'])

@router.get('/status')
def feature_task_012_status():
    return {'ok': True, 'feature': 'Back-end programado: servicos, validacoes e casos de borda', 'task': 'task-012'}
