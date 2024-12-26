from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description='Email do usuário')
    username: str = Field(
        ...,
        min_length=5,
        max_length=50,
        description='Username do usuário'
    )
    password: str = Field(
        ...,
        min_length=6,
        max_length=20,
        description='Senha do usuário'
    )
    
class UserDetail(BaseModel):
    user_id: UUID
    username: str
    email: str