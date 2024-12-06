"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Анекдот')],
    [KeyboardButton(text='История пользователей', callback_data='get_users' ), KeyboardButton(text='Мои задачи')]
], resize_keyboard=True)

# main = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
#     [InlineKeyboardButton(text='Корзина', callback_data='cart'), InlineKeyboardButton(text='Контакты', callback_data='contacts')]
# ])


dev_acc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Связь с админом', url='https://t.me/uzi_smuzi')]
])

cancel_registration = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена', callback_data='cancel_registration')]
])

tasks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить задачу', callback_data='add_task')],
    [InlineKeyboardButton(text='Удалить задачу', callback_data='remove_task')]
])


tasks_empty = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить задачу', callback_data='add_task')]
])

cancel_add_task = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отмена', callback_data='cancel_add_task')]
])