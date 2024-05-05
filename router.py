from typing import Annotated

# APIRouter позволяет переносить набор ручек в отдельный файл и потом удобно перемещать в main

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(prefix='/tasks', tags=["Таски"])


@router.post("")
# Конструкция annotated - depends меняет интерфейс в документации чтобы можно было удобно посылать запросы
async def add_tasks(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return {"data": tasks}
