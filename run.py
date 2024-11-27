"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""
import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_TOKEN = os.getenv('TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}. Заходи - не бойся, выходи - не плачь')

@dp.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('Пока не родила')

@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID photo: {message.photo[-1].file_id}')



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")