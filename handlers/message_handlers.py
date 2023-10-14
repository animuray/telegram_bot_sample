from aiogram import types
from loader import dp
from database import DataBase
from api import *
import keyboards.kb as kb

db = DataBase('db.db')


@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    if message.text == 'Пример текста':
        await message.answer('Это пример твоего текста!')

