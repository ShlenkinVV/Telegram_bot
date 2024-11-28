"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers import router

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_TOKEN = os.getenv('TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()






async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")