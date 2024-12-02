from sqlalchemy import BigInteger, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
import os
from dotenv import load_dotenv

load_dotenv('.env')

DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_NAME=os.getenv('DB_NAME')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')

#engine = create_async_engine(url=os.getenv('BD_URL3')) # создание БД
engine = create_async_engine(url=f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}') # создание БД


async_session = async_sessionmaker(engine) # Подкючение к БД

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(25))
    relation: Mapped[str] = mapped_column(String(25))
    tg_username: Mapped[str] = mapped_column(String(25))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # Создаются классы
