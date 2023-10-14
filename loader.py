import asyncio
import config
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

loop = asyncio.get_event_loop()
bot = Bot(config.TOKEN, parse_mode='HTML')
storage = MemoryStorage()

dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())
