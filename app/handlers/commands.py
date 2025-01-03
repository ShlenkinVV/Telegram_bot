from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message
import app.database.requests as rq
import os
import app.keyboards as kb
from app.database.requests import catch_user


router = Router()
from dotenv import load_dotenv

load_dotenv('.env')

ADMIN_ID = os.getenv('ADMIN_ID')

@router.message(Command('help'), StateFilter(None))
async def get_help(message: Message):
    await message.answer('Это команда /help', reply_markup=kb.dev_acc)


@router.message(CommandStart())
async def cmd_start(message: Message):
    if await catch_user(message.from_user.id, message.from_user.username):
        from run import bot
        await bot.send_message(ADMIN_ID, f'Пользователь {message.from_user.username} зашел в твой бот ')

    await message.answer(f"""
    Привет, {message.from_user.first_name}. Заходи - не бойся, выходи - не плачь\n
    """, reply_markup=kb.main)


@router.message(Command('delete_user'), StateFilter(None))
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


@router.message(Command('users'), StateFilter(None))
async def get_users_info(message: Message):
    if str(message.from_user.id) != ADMIN_ID:
        await message.answer(f'Смотреть данные пользователей может только админ')
    else:
        all_users = await rq.get_users()
        text = ''
        for user in all_users:
            text += f'{user.id}) {user.name} - {user.relation} ({user.tg_username})\n'

        await message.answer(text)


@router.message(Command('all_users'), StateFilter(None))
async def get_all_users(message: Message):
    if str(message.from_user.id) != ADMIN_ID:
        await message.answer(f'Смотреть данные пользователей может только админ')
    else:
        all_users = await rq.get_all_users()
        text = ''
        for user in all_users:
            text += f'{user.tg_username}, {user.tg_id}\n'

        await message.answer(text)

