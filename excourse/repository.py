from sqlalchemy import select
from database import TaskOrm, new_session
from schemas import Task, TaskAdd

class TaskRepository:
    @classmethod
    async def add_one(self, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.dict()
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
            return task_models
        
    @classmethod


