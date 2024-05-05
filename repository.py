# Паттерн репозитория позволяет работать с базой данных как с как с коллекцией обьектов
# удалять / добавлять

from sqlalchemy import select


from schemas import STaskAdd, STask
from database import new_session, TaskOrm


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task) for task in task_models]
            return task_schemas
