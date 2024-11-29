from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
import app.database.requests as rq
import os
import app.keyboards as kb
router = Router()
from dotenv import load_dotenv

load_dotenv('.env')

ADMIN_ID = os.getenv('ADMIN_ID')

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help', reply_markup=kb.dev_acc)

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}. Заходи - не бойся, выходи - не плачь', reply_markup=kb.main)

@router.message(Command('delete_user'))
async def delete_user(message: Message):
    if str(message.from_user.id) != ADMIN_ID:
        await message.answer(f'Удалять пользователей может только админ')
    else:
        args = message.text.split()

        if len(args) > 1:  # Проверяем, есть ли аргументы
            user_id = args[1]

            try:
                await rq.delete_user(int(user_id))
                await message.reply(f"Пользователь с id {user_id} был успешно удален.")
            except Exception as e:
                await message.reply(f"Произошла ошибка при удалении пользователя: {str(e)}")
        else:
            await message.reply("Пожалуйста, укажите id пользователя для удаления.")