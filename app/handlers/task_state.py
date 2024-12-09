from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.filters import Command, StateFilter
from sqlalchemy.testing.suite.test_reflection import users

import app.database.requests as rq
import app.keyboards as kb

router = Router()

class AddTaskState(StatesGroup):
    waiting_for_task = State()

class RmTaskState(StatesGroup):
    waiting_for_rm_task = State()

@router.callback_query(F.data == 'add_task', StateFilter(None))
async def add_task_command(callback: CallbackQuery, state: FSMContext):
    await state.set_state(AddTaskState.waiting_for_task)
    await callback.answer()
    await callback.message.answer("Введите задачу, которую хотите добавить:", reply_markup=kb.cancel_add_task)

@router.callback_query(F.data == "cancel_add_task")
async def cancel_registration(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer("Отмена")
    user_id = callback.from_user.id
    await list_tasks(callback.message, user_id)

@router.message(AddTaskState.waiting_for_task)
async def add_task(message: Message, state: FSMContext):
    if message.content_type == 'text':
        user_id = message.from_user.id
        task_description = message.text

        await rq.add_task(user_id, task_description)
        await message.answer(f"Задача '{task_description}' добавлена!")
        await list_tasks(message, user_id)
        await state.clear()
    else:
        await message.answer('Пожалуйста, введите текстовое сообщение.')

@router.message(F.text.in_(['Мои задачи📋','Мои задачи']), StateFilter(None))
async def list_tasks(message: Message,  user_id=None):
    if user_id is None:
        user_id = message.from_user.id
    tasks = await rq.get_tasks(user_id)

    if tasks:
        i = 1
        tasks_list = 'Ваши задачи:\n'
        for task in tasks:
            tasks_list += f'{i}) {task.description}\n'
            i+=1
        await message.answer(tasks_list, reply_markup=kb.tasks)
    else:
        await message.answer("У вас пока нет задач.", reply_markup=kb.tasks_empty)


@router.callback_query(F.data == 'remove_task', StateFilter(None))
async def remove_task_command(callback: CallbackQuery, state: FSMContext):
    await state.set_state(RmTaskState.waiting_for_rm_task)
    await callback.answer()
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer("Введите номер задачи, которую хотите удалить:", reply_markup=kb.cancel_add_task)

@router.message(RmTaskState.waiting_for_rm_task)
async def remove_task(message: Message, state: FSMContext):
    if message.content_type == 'text':
        user_id = message.from_user.id
        tasks = await rq.get_tasks(user_id)
        try:
            task_num = int(message.text)
            task_id = tasks[task_num-1].id
            await rq.remove_task(task_id)
            await message.answer(f"Задача '{tasks[task_num - 1].description}' удалена!")
            await list_tasks(message, user_id)

            await state.clear()
        except (IndexError, ValueError):
            await message.answer("Некорректный номер задачи. Введите ещё раз", reply_markup=kb.cancel_add_task)


    else:
        await message.answer('Пожалуйста, введите текстовое сообщение.')