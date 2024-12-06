from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
import app.database.requests as rq
import app.keyboards as kb
from aiogram.types import ReplyKeyboardRemove

router = Router()
# Класс состояний
class Reg(StatesGroup):
    name = State()
    relation = State()

#Использование состояний
@router.message(Command('reg'), StateFilter(None))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)     # Меняем состояние
    await message.answer('Введите Ваше имя', reply_markup=kb.cancel_registration)



@router.message(Reg.name)       # принмаем состояние
async def reg_two(message: Message, state: FSMContext):
    if message.content_type == 'text':
        await state.update_data(name=message.text)
        await state.set_state(Reg.relation)  # Меняем состояние
        await message.answer('Кем вы приходитесь разрабу?(другом, сестрой, котом и т.д.)', reply_markup=kb.cancel_registration)
    else:
        await message.answer('Пожалуйста, введите текстовое сообщение.', reply_markup=kb.cancel_registration)

@router.message(Reg.relation)
async def reg_three(message: Message, state: FSMContext):
    if message.content_type == 'text':
        await state.update_data(relation=message.text)
        data = await state.get_data()
        user_added = await rq.add_user(message.from_user.id, message.from_user.username, data['name'], data['relation'])
        if user_added:
            await message.answer(f'Спасибо за регистрацию, {data['name']}', reply_markup=kb.main)
        else:
            await message.answer('Ваш аккаунт телеграм уже зарегистрирован', reply_markup=kb.main)
        await state.clear()
    else:
        await message.answer('Пожалуйста, введите текстовое сообщение.')

@router.callback_query(lambda c: c.data == "cancel_registration")
async def cancel_registration(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.answer("Регистрация отменена.")  # Отправляем ответ на нажатие кнопки
    await callback_query.message.answer("Вы отменили регистрацию.", reply_markup=kb.main)  # Возвращаемся к главному меню