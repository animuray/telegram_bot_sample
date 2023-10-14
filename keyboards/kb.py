from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# --- Main menu buttons---
button1 = KeyboardButton('Главное меню') 


# --- добавляем Main menu buttons
def main_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1)
    return markup




