from fastapi import APIRouter
from .handlers import user, task
from api.auth.jwt import auth_router

api_router = APIRouter()

api_router.include_router(
    user.router,
    prefix="/users",
    tags=["users"]
)

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"]
)

api_router.include_router(
    task.task_router,
    prefix="/task",
    tags=["task"]
)
