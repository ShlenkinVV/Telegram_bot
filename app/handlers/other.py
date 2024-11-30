from aiogram import F, Router
from aiogram.types import Message
import app.database.requests as rq
from app.anekdots import aneks
from random import randint

router = Router()

@router.message(F.text == 'Все пользователи')
async def get_users(message: Message):
    all_users = await rq.get_users()
    text = 'Список пользователей:\n'
    i=1
    for user in all_users:
        text+=f'{i}) {user.name} - {user.relation}\n'
        i+=1
    await message.answer(text)

@router.message(F.text == 'Анекдот')
async def get_anek(message: Message):
    anek = aneks[randint(0, len(aneks)-1)]
    await message.answer(anek)

@router.message(F.text == 'Не нажимать')
async def get_angry(message: Message):
    await message.answer('Написано же "Не нажиамть"!!!')