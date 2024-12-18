from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import tasks
from database import init_db

app = FastAPI()

# Добавляем CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)

# Подключение маршрутов
app.include_router(tasks.router)

# Инициализация базы данных при старте
@app.on_event("startup")
async def startup():
    await init_db()

# Корневой эндпоинт для проверки статуса сервера
@app.get("/")
async def read_root():
    return {"message": "Server is running"}
