from typing import Optional

# async_sessionmaker - фабрика создания сессий, открытие транзакций для работы с бд
# create_async_engine - асинхронный движок для работы с бд
# mapped - работает с типами в модели
# declarativebase - базовая модель которую расширяет наша Model
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    # могут быть конфигурации
    pass


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]] = None

# функция чтобы sqlalchemy создала все нужные таблицы


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


# То же самое но для удаления таблиц :
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
