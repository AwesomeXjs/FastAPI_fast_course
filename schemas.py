from typing import Optional
from pydantic import BaseModel


# чтобы обозначить данные которые можно ожидать от нашего апи (описание данных):


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None  # str | None  #


class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
