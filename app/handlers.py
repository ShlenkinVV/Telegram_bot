"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}. Заходи - не бойся, выходи - не плачь')

@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('Пока не родила')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID photo: {message.photo[-1].file_id}')