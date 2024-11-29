"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import main_router
from app.database.models import async_main

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_TOKEN = os.getenv('TOKEN')


async def main():
    await async_main()
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # подключение логов
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")