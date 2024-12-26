from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth, UserDetail
from services.user_service import UserService
import pymongo

router = APIRouter()

@router.post("/adiciona", summary="Adiciona um usuário", tags=["users"], response_model=UserDetail)
async def add_users(data: UserAuth):
    try:
        return await UserService.create_user(data)
    
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail= 'Usuário ou e-mail já existe'
        )
