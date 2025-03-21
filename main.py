import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from config import TOKEN, DEFAULT_MODEL
from handlers import register_all_handlers
from state import set_current_model

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    set_current_model(DEFAULT_MODEL)
    register_all_handlers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())