from typing import List
from decouple import config
from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"  # Anotação com ClassVar para variáveis que não são campos

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # BACKEND_CORS_ORIGINS é uma lista de origens permitidas para o front-end
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        # http://localhost:3000
    ]
    PROJECT_NAME: str = "TODOFast"

    # Banco de dados
    MONGO_CONNECTION_STRING: str = config('MONGO_CONNECTION_STRING', cast=str)
    DATABASE_NAME: str = 'todoapp'

    class Config:
        case_sensitive = True


settings = Settings()
