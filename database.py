from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from Base import Base  # Импортируем Base из base.py
from models import Task  # Импорт модели Task для регистрации
Task
# URL базы данных
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Создание асинхронного движка базы данных
engine = create_async_engine(DATABASE_URL, echo=True)

# Создание асинхронной фабрики сессий
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

# Функция для инициализации базы данных
async def init_db():
    print("Инициализация базы данных...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Таблицы созданы.")

# Зависимость для FastAPI
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
