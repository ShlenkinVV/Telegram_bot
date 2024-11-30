from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
import app.database.requests as rq
import app.keyboards as kb
from aiogram.types import ReplyKeyboardRemove

router = Router()
# Класс состояний
class Reg(StatesGroup):
    name = State()
    relation = State()

#Использование состояний
@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)     # Меняем состояние
    await message.answer('Введите Ваше имя', reply_markup=ReplyKeyboardRemove())


@router.message(Reg.name)       # принмаем состояние
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.relation)  # Меняем состояние
    await message.answer('Кем вы приходитесь разрабу?(другом, сестрой, котом и т.д.)')

@router.message(Reg.relation)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(relation=message.text)
    data = await state.get_data()
    await rq.add_user(message.from_user.id, message.from_user.username, data['name'], data['relation'])
    await message.answer(f'Спасибо за регистрацию, {data['name']}', reply_markup=kb.main)
    await state.clear()