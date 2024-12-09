"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Анекдот🙃'), KeyboardButton(text='Мои задачи📋')],
    [KeyboardButton(text='История пользователей👨‍💻'), KeyboardButton(text='Aboutℹ️')]
], resize_keyboard=True)


dev_acc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Связь с админом', url='https://t.me/uzi_smuzi')]
])

cancel_registration = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена❌', callback_data='cancel_registration')]
])

tasks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить задачу➕', callback_data='add_task')],
    [InlineKeyboardButton(text='Удалить задачу🗑️', callback_data='remove_task')]
])


tasks_empty = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить задачу➕', callback_data='add_task')]
])

cancel_add_task = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена❌', callback_data='cancel_add_task')]
])

registration = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Зарегистрироваться', callback_data='reg')]
])

anek = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ввести номер анекдота', callback_data='num_anek')]
])

cancel_chose_anek = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена❌', callback_data='cancel_chose_anek')]
])