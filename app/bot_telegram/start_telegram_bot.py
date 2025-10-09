from aiogram import Bot, Dispatcher
from config import settings
import asyncio
import logging
from bot_telegram.routers.start import router as start_router
from bot_telegram.routers.register import router as register_router
from bot_telegram.routers.enter_scores import router as enter_scores_router
from bot_telegram.routers.view_scores import router as view_scores_router

logging.basicConfig(level=logging.INFO)


bot = Bot(token=str(settings.telegram_bot.api_key))
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(register_router)
dp.include_router(enter_scores_router)
dp.include_router(view_scores_router)


async def start_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
