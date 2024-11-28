"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.middleware import TestMiddleware

router = Router()

router.message.middleware(TestMiddleware()) # подключаем middleware к роутеру, работает при каждом сообщении
router.message.outer_middleware(TestMiddleware()) # Срабатывает вне зависимости от того, нашелся ли обработчик или нет

# Класс состояний
class Reg(StatesGroup):
    name = State()
    relation = State()

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help', reply_markup=kb.dev_acc)

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}. Заходи - не бойся, выходи - не плачь', reply_markup=kb.main)

@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('Пока не родила')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID photo: {message.photo[-1].file_id}')

@router.callback_query(F.data == 'catalog')
async def get_catalog(callback: CallbackQuery):
    await callback.answer('То что ты пидор, ёпта') # Либо текст, либо путсые скобки
    await callback.message.answer('Это каталог')



#Использование состояний
@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)     # Меняем состояние
    await message.answer('Введите Ваше имя')


@router.message(Reg.name)       # принмаем состояние
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.relation)  # Меняем состояние
    await message.answer('Кем вы приходитесь разрабу?(другом, сестрой, котом и т.д.)')

@router.message(Reg.relation)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(relation=message.text)
    data = await state.get_data()
    await message.answer('Спасибо за регистрацию')
    await state.clear()