from aiogram import executor
from loader import dp, bot
import config
from database import DataBase

db = DataBase('db.db')


# -- при запуске, бот будет отправлять уведомление админу по chat_id=admin_id, о том что он запущен и работает
async def send_to_admin(dp):
    await bot.send_message(chat_id=config.admin_id, text='Бот запущен!')


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=send_to_admin, skip_updates=True)



