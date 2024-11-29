from aiogram import F, Router
from aiogram.types import Message
import app.database.requests as rq

router = Router()

@router.message(F.text == 'Все пользователи')
async def get_users(message: Message):
    all_users = await rq.get_users()
    text = 'Список пользователей:\n'
    for user in all_users:
        text+=f'{user.id}) {user.name} - {user.relation}\n'
    await message.answer(text)

@router.message(F.text == 'Анекдот')
async def get_anek(message: Message):
    pass