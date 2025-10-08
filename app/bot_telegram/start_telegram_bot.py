from aiogram import Bot, Dispatcher
from config import settings
import asyncio
import logging
from bot_telegram.routers import router as bot_routers

logging.basicConfig(level=logging.INFO)


bot = Bot(token=str(settings.telegram_bot.api_key))
dp = Dispatcher()
dp.include_router(bot_routers)


async def start_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
