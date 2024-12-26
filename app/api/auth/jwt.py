from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from api.dependencies.user_deps import get_current_user
from core.security import create_access_token, create_refresh_token
from models.user_model import User
from schemas.auth_schema import TokenSchema
from schemas.user_schema import UserDetail
from services.user_service import UserService

auth_router = APIRouter()


@auth_router.post(
    '/login',
    summary='Cria o Access Token e o Refresh Token',
    response_model=TokenSchema
)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email=data.username,
        password=data.password

    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail ou senha inválidos"
        )
    return {
        'access_token': create_access_token(usuario.user_id),
        'refresh_token': create_refresh_token(usuario.user_id)
    }


@auth_router.post(
    '/test-token',
    summary='Testa o Token',
    response_model=UserDetail
)
async def test_token(user: User = Depends(get_current_user)):
    return user
