from app.database.models import async_session
from app.database.models import User, Task
from sqlalchemy import select, update, delete, desc

async def add_user(tg_id, tg_username, username, relation):
    async with async_session() as session:
        user = await session.scalar(select(User).where(tg_id == User.tg_id)) # ищем пользователя

        if not user:
            session.add(User(tg_id=tg_id, tg_username=tg_username, name=username, relation=relation))
            await session.commit()
            return True
        else:
            return False


async def get_users():
    async with async_session() as session:
        return await session.scalars(select(User))


async def delete_user(user_id):
    async with async_session() as session:
        # Ищем пользователя по id
        user = await session.scalar(select(User).where(User.id == user_id))

        if user:
            await session.delete(user)  # Удаляем пользователя
            await session.commit()  # Сохраняем изменения

async def add_task(user_id: int, description: str):
    async with async_session() as session:
        new_task = Task(user_id=user_id, description=description)
        session.add(new_task)
        await session.commit()

async def get_tasks(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(Task).where(user_id == Task.user_id))
        return result.scalars().all()

async def remove_task(task_id: int):
    async with async_session() as session:
        task = await session.get(Task, task_id)
        if task:
            await session.delete(task)
            await session.commit()
            return True
        return False