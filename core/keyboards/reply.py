from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Магазин'),
    KeyboardButton(text='Профиль')],
    [KeyboardButton(text='Гарант'),
    KeyboardButton(text='Наши контакты')]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите категорию ниже:')
