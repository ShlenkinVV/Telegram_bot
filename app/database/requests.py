from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select, update, delete, desc

async def add_user(tg_id, tg_username, username, relation):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id)) # ищем пользователя

        if not user:
            session.add(User(tg_id=tg_id, tg_username=tg_username, name=username, relation=relation))
            await session.commit()


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