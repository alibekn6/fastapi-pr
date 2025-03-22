from fastapi import APIRouter, Depends
from typing import Annotated, Optional
from schemas import TaskAdd, Task
from repository import TaskRepository

router = APIRouter(
    prefix='/tasks',
    tags=['Таски']
)

@router.post('')
async def addTask(task: Annotated[TaskAdd, Depends()]):
    task_id = await TaskRepository.add_one(task)

    return {"ok":True, "task_id": task_id}


@router.get('')
async def getTasks():
    tasks = await TaskRepository.find_all()
    return {"tasks": tasks}