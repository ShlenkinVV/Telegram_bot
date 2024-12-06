from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
import app.database.requests as rq
from app.anekdots import aneks
from random import randint
import app.keyboards as kb

router = Router()

class MainState(StatesGroup):
    main = State()


@router.message(F.text == 'История пользователей', StateFilter(None))
async def get_users(message: Message):
    all_users = await rq.get_users()
    text = 'Список пользователей, которые пользовались этим ботом:\n'
    i=1
    for user in all_users:
        text+=f'{i}) {user.name} - {user.relation}\n'
        i+=1
    text+='\nХочешь попасть в историю? Жми на кнопку ниже'
    await message.answer(text, reply_markup=kb.registration)

@router.message(F.text == 'Анекдот', StateFilter(None))
async def get_anek(message: Message):
    anek = aneks[randint(0, len(aneks)-1)]
    await message.answer(anek)

@router.message(F.text == 'About', StateFilter(None))
async def get_info(message: Message):
    await message.answer(f"""
    Телеграмм бот для портфолио. Не для комерческих целей.
С течением времени бот будет дорабатываться, количество анекдотов увеличиваться.\n
Если Вы заметили какой-то баг или столкнулись с тем, что бот не работает, то буду рад если Вы сообщите об этом(@uzi_smuzi).

Озанкомиться со структурой, реализацией и полным функционалом бота Вы можете на GitHub:
https://github.com/ShlenkinVV/Telegram_bot\n

<b>Благодарности</b>:
Разработичк никого не благодарит. Напртив, ждет пока его самого отблагодарят. Можно сюда:

BTC - bc1qmlpamfrsm99h5pd6erk5gs27x72dvqp23nzf4j

TON - UQC15221lnBJ2P1T7mVv4VWFdn7zsyOUNFABtUetqeA7yFGL


    """, reply_markup=kb.main, parse_mode='html')