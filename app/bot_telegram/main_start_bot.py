from aiogram import Bot, Dispatcher
from config import settings
import asyncio
import logging
from routers.start import router as start_router

logging.basicConfig(level=logging.INFO)


bot = Bot(token=str(settings.telegram_bot.api_key))
dp = Dispatcher()
dp.include_router(start_router)


async def start_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
