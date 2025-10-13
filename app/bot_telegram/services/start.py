from aiogram import types
from database import DatabaseManager
from users.models import User
from sqlalchemy import select
from bot_telegram.keyboards import get_start_keyboard, get_register_button
from logging_config import app_logger


logger = app_logger.getChild(__name__)


async def sey_hi_or_start_register(message: types.Message):
    user = None
    try:
        async for session in DatabaseManager.get_session():
            result = await session.execute(select(User).where(User.telegram_id == message.chat.id))
            user = result.scalar_one_or_none()
    except Exception:
        logger.critical("Error during request to database.")

    if user:
        await message.answer(f"Привет, {User.username}!\nВыберите действие в меню:",
                             reply_markup=get_start_keyboard())
    else:
        await message.answer(text="Добро пожаловать! Давай начем регистрацию\n"
                                  "Для старта нажми книпку внизу:\n"
                                  "(чтобы отменить регистрацию введите команду /cansel)",
                             reply_markup=get_register_button())
