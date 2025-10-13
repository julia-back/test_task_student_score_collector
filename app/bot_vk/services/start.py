from bot_vk.keyboards import register_button, start_keyboard
from database import DatabaseManager
from logging_config import app_logger
from sqlalchemy import select
from users.models import User
from vkbottle.bot import Message

logger = app_logger.getChild(__name__)


async def say_hi_or_start_register(message: Message):
    user_vk_id = message.from_id
    user = None
    try:
        async for session in DatabaseManager.get_session():
            result = await session.execute(select(User).where(User.vk_id == user_vk_id))
            user = result.scalar_one_or_none()
    except Exception:
        logger.critical("Error during request from db.")

    if user:
        await message.answer("Привет, выбери действие в меню снизу:", keyboard=start_keyboard())

    else:
        await message.answer(
            "Добро пожаловать! Чтобы начать регистрацию, нажми кнопку:\n"
            "(чтобы отменить регистрацию введи команду /cansel)",
            keyboard=register_button(),
        )
