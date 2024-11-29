# """
# author - Shlenkin Vladimir
# GitHub - ShlenkinVV
# """
#
# from aiogram import F, Router
# from aiogram.filters import CommandStart, Command
# from aiogram.types import Message, CallbackQuery
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.context import FSMContext
# from dotenv import load_dotenv
# import os
#
# import app.keyboards as kb
# from app.middleware import TestMiddleware
# import app.database.requests as rq
#
# router = Router()
#
# ADMIN_ID = os.getenv('ADMIN_ID')
#
# # router.message.middleware(TestMiddleware())         # подключаем middleware к роутеру, работает при каждом сообщении
# # router.message.outer_middleware(TestMiddleware()) # Срабатывает вне зависимости от того, нашелся ли обработчик или нет
#
# # Класс состояний
# class Reg(StatesGroup):
#     name = State()
#     relation = State()
#
# @router.message(Command('help'))
# async def get_help(message: Message):
#     await message.answer('Это команда /help', reply_markup=kb.dev_acc)
#
# @router.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer(f'Привет, {message.from_user.first_name}. Заходи - не бойся, выходи - не плачь', reply_markup=kb.main)
#
# @router.message(Command('delete_user'))
# async def delete_user(message: Message):
#     if message.from_user.id != ADMIN_ID:
#         await message.answer('Удалять пользователей может только админ')
#     else:
#         args = message.text.split()
#
#         if len(args) > 1:  # Проверяем, есть ли аргументы
#             user_id = args[1]
#
#             try:
#                 await rq.delete_user(int(user_id))
#                 await message.reply(f"Пользователь с id {user_id} был успешно удален.")
#             except Exception as e:
#                 await message.reply(f"Произошла ошибка при удалении пользователя: {str(e)}")
#         else:
#             await message.reply("Пожалуйста, укажите id пользователя для удаления.")
#
#
# # @router.message(F.photo)
# # async def get_photo(message: Message):
# #     await message.answer(f'ID photo: {message.photo[-1].file_id}')
#
# # @router.callback_query(F.data == 'catalog')
# # async def get_catalog(callback: CallbackQuery):
# #     await callback.answer('То что ты пидор, ёпта') # Либо текст, либо путсые скобки
# #     await callback.message.answer('Это каталог')
#
# @router.message(F.text == 'Все пользователи')
# async def get_users(message: Message):
#     all_users = await rq.get_users()
#     text = 'Список пользователей:\n'
#     for user in all_users:
#         text+=f'{user.id}) {user.name} - {user.relation}\n'
#     await message.answer(text)
#
# @router.message(F.text == 'Анекдот')
# async def get_anek(message: Message):
#     pass
#
# #Использование состояний
# @router.message(Command('reg'))
# async def reg_one(message: Message, state: FSMContext):
#     await state.set_state(Reg.name)     # Меняем состояние
#     await message.answer('Введите Ваше имя')
#
#
# @router.message(Reg.name)       # принмаем состояние
# async def reg_two(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(Reg.relation)  # Меняем состояние
#     await message.answer('Кем вы приходитесь разрабу?(другом, сестрой, котом и т.д.)')
#
# @router.message(Reg.relation)
# async def reg_three(message: Message, state: FSMContext):
#     await state.update_data(relation=message.text)
#     data = await state.get_data()
#     await rq.add_user(message.from_user.id, data['name'], data['relation'])
#     await message.answer(f'Спасибо за регистрацию {data['name']}')
#     await state.clear()