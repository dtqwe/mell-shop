from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🛒Магазин', callback_data='shop')
    keyboard_builder.button(text='👤Профиль', callback_data='profile')
    keyboard_builder.button(text='🆗Гарант', callback_data='guarantee')
    keyboard_builder.button(text='📱Наши контакты', callback_data='contacts')

    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup()

def get_products_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Marci Brightfist', callback_data='product_1')
    keyboard_builder.button(text='Spectre Crescent Huntress', callback_data='product_2')
    keyboard_builder.button(text='Snapfire Snailfire', callback_data='product_3')
    keyboard_builder.button(text='Dazzle Dezun Viper', callback_data='product_4')
    keyboard_builder.button(text='Dawnbreaker Astral Herald', callback_data='product_5')    
    keyboard_builder.button(text='Назад', callback_data="shop_back_to_main")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def shop_marci():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Купить', callback_data='buy_marci')    
    keyboard_builder.button(text='Назад', callback_data="marci_back_to_shop")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def shop_scpectre():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Купить', callback_data='buy_scpectre')    
    keyboard_builder.button(text='Назад', callback_data="scpectre_back_to_shop")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def shop_snapfire():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Купить', callback_data='buy_snapfire')    
    keyboard_builder.button(text='Назад', callback_data="snapfire_back_to_shop")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def shop_dazzle():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Купить', callback_data='buy_dazzle')    
    keyboard_builder.button(text='Назад', callback_data="dazzle_back_to_shop")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def shop_dawnbreaker():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Купить', callback_data='buy_dawnbreaker')    
    keyboard_builder.button(text='Назад', callback_data="dawnbreaker_back_to_shop")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
#-------------------------------------------------------------------------- END SHOP

def get_profile():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Назад', callback_data="profile_back_to_main")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def get_guarantee():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Назад', callback_data="guarantee_back_to_main")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def get_contacts():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Назад', callback_data="contacts_back_to_main")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()