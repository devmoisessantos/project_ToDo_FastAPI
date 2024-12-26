from fastapi import FastAPI
from core.config import settings
from models.task_model import Task
from models.user_model import User
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from api.api_v1.router import api_router
from fastapi.middleware.cors import CORSMiddleware


# Criação da instância FastAPI com o gerenciador
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def on_startup():
    await app_init()  # Inicializa a conexão com o banco e o Beanie
    print("Banco de dados inicializado!")


async def app_init():
    # Conectando ao MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    database = client["todoapp"]

    # Inserção inicial para forçar a criação do banco e da coleção
    await init_beanie(
        database=database,
        document_models=[
            User,
            Task
        ]
    )

    # # Fechando a conexão ao encerrar a aplicação
    # app.state.mongodb_client = client

# Inclua as rotas
app.include_router(api_router, prefix=settings.API_V1_STR)
