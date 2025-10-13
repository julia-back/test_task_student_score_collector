from aiogram import Bot, Dispatcher
from config import settings
import asyncio
from bot_telegram.routers.start import router as start_router
from bot_telegram.routers.register import router as register_router
from bot_telegram.routers.enter_scores import router as enter_scores_router
from bot_telegram.routers.view_scores import router as view_scores_router
from logging_config import app_logger, logging_queue_listener


logger = app_logger.getChild(__name__)


bot = Bot(token=str(settings.telegram_bot.api_key))
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(register_router)
dp.include_router(enter_scores_router)
dp.include_router(view_scores_router)


async def start_bot():
    logging_queue_listener.start()
    logger.critical("Start telegram bot.")
    await dp.start_polling(bot)
    logger.info("Stop telegram bot.")
    logging_queue_listener.stop()

if __name__ == "__main__":
    asyncio.run(start_bot())
