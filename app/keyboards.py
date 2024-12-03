"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV
"""
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Анекдот')],
    [KeyboardButton(text='История пользователей', callback_data='get_users' ), KeyboardButton(text='Не нажимать')]
], resize_keyboard=True,
    input_field_placeholder='Смотри вниз')

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