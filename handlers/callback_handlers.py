from api import *
from loader import dp
from aiogram.types import CallbackQuery
import keyboards.kb as kb
from database import DataBase

db = DataBase('db.db')


@dp.callback_query_handler(text_contains="sample1")
async def callback_query_handler(call: CallbackQuery):
	# do something
	text = 'something'
	await call.message.answer(text)


