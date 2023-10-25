import asyncio
import logging
import sys
import os
from aiogram import Dispatcher, Bot
from core.handlers.basic import router

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

admin_id = os.getenv('ADMIN_ID')
TOKEN = os.getenv('TOKEN')
YKASSA_TOKEN = os.getenv('YKASSA_TOKEN')

async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text='Бот запущен')


bot = Bot(TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    dp.startup.register(start_bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        pass