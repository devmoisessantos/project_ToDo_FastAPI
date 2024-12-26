from uuid import UUID
from fastapi import APIRouter, Depends
from schemas.task_schema import TaskDetail, TaskCreate, TaskUpdate
from models.task_model import Task
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from services.task_service import TaskService
from typing import List

task_router = APIRouter()


@task_router.get("/", summary="Lista as tarefas",
                 response_model=List[TaskDetail])
async def list_tasks(user: User = Depends(get_current_user)):
    return await TaskService.get_tasks_by_user(user)


@task_router.get('/find-task/{task_id}', summary='Busca uma tarefa pelo ID', response_model=TaskDetail)
async def get_task_by_id(task_id: UUID, user: User = Depends(get_current_user)):
    return await TaskService.details_task_by_id(task_id, user)


@task_router.post("/create-task", summary="Cria uma tarefa", response_model=Task)
async def task_create(data: TaskCreate, user: User = Depends(get_current_user)):
    task = await TaskService.create_task(data, user)
    return task
    # return TaskDetail(
    #     task_id=task.task_id,
    #     title=task.title,
    #     description=task.description,
    #     status=task.status,
    #     created_at=task.created_at,
    #     updated_at=task.updated_at
    # )


@task_router.put("/update-task/{task_id}", summary="Atualiza uma tarefa por ID", response_model=TaskDetail)
async def update_task_by_id(task_id: UUID, data: TaskUpdate, user: User = Depends(get_current_user)):
    return await TaskService.update_task_by_id(user, task_id, data)


@task_router.delete("/delete-task/{task_id}", summary="Deleta uma tarefa por ID")
async def delete_task_by_id(task_id: UUID, user: User = Depends(get_current_user)):
    await TaskService.delete_task_by_id(user, task_id)
    return {'message': 'Tarefa excluida com sucesso'}
