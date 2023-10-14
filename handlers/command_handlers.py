from aiogram import types
from loader import dp
import keyboards.kb as kb
from database import DataBase

db = DataBase('db.db')


# -- обработчик команды старт
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет.')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('Поддержка максимальная.')








