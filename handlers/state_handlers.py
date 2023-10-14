from aiogram import types
from loader import dp
import keyboards.kb as kb

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from api import *


class Group(StatesGroup):
    sample = State()


# --- обработчик ответа
@dp.message_handler(state=Group.sample)
async def answer_search_anime(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["sample"] = answer

    data = await state.get_data()
    result = data['sample']
    
    await message.answer(result)
    await state.finish()
                








