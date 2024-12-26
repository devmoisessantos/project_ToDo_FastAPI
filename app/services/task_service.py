from uuid import UUID
from models.user_model import User
from models.task_model import Task
from typing import List
from schemas.task_schema import TaskCreate, TaskUpdate, TaskDetail


class TaskService:

    @staticmethod
    async def get_tasks_by_user(user: User) -> List[Task]:
        tasks = await Task.find(Task.owner.id == user.id).to_list()
        return tasks

    @staticmethod
    async def create_task(data: TaskCreate, user: User) -> Task:
        # Criando a tarefa com os campos corretos
        task = Task(
            title=data.title,
            description=data.description,
            status=data.status,
            owner=user
        )
        return await task.insert()

    @staticmethod
    async def details_task(user: User, task_id: UUID):
        task = await Task.find_one(Task.task_id == task_id, Task.owner.id == user.id)
        return task

    @staticmethod
    async def update_task_by_id(user: User, task_id: UUID, data: TaskUpdate):
        task = await TaskService.details_task(user, task_id)
        await task.update({
            '$set': data.dict(exclude_unset=True)
        })
        await task.save()
        return task

    @staticmethod
    async def delete_task_by_id(user: User, task_id: UUID):
        task = await TaskService.details_task(user, task_id)
        if task:
            await task.delete()
        return f'message : Tarefa excluida com sucesso'
