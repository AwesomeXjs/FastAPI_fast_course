from fastapi import FastAPI
from contextlib import asynccontextmanager

from router import router as tasks_router
from database import create_tables, delete_tables

# создание базы данных на основе моделей (функция lifespan из документации)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

# чтобы запустить приложение на вебсервере uvicorn:
# uvicorn main:app --reload
