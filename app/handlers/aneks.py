"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""
from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
import app.database.requests as rq
import app.keyboards as kb
from app.anekdots import aneks
from random import randint

router = Router()

class Anek(StatesGroup):
    num_of_anek = State()


@router.message(F.text.in_(['Анекдот🙃','Анекдот']), StateFilter(None))
async def get_anek(message: Message):
    index = randint(0, len(aneks)-1)
    anek = aneks[index]
    await message.answer(f'{index+1}/{len(aneks)}\n'+anek, reply_markup=kb.anek)

@router.callback_query(F.data == "num_anek", StateFilter(None))
async def get_anek_by_num(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Anek.num_of_anek)
    await callback.answer()
    await callback.message.answer(f'Введите номер анекдота\n(от 1 до {len(aneks)})', reply_markup=kb.cancel_chose_anek)

@router.callback_query(F.data == "cancel_chose_anek", StateFilter(Anek.num_of_anek))
async def cancel_registration(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer("Отмена")
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer('Вы отменили выбор анекдота')

@router.message(StateFilter(Anek.num_of_anek))
async def cancel_registration(message: Message, state: FSMContext):
    if message.content_type == 'text':
        try:
            index = int(message.text)
            anek = aneks[index-1]
            await message.answer(f'{index}/{len(aneks)}\n' + anek, reply_markup=kb.anek)
            await state.clear()
        except (IndexError, ValueError):
            await message.answer("Некорректный номер анекдота. Введите ещё раз", reply_markup=kb.cancel_chose_anek)

    else:
        await message.answer('Пожалуйста, введите текстовое сообщение.')