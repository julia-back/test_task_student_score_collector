from vkbottle.bot import Message
from database import DatabaseManager
from users.models import User
from sqlalchemy import select
from bot_vk.keyboards import start_keyboard, register_button
from bot_vk.states import RegisterState, state_dispenser


async def say_hi_or_start_register(message: Message):
    user_vk_id = message.from_id
    user = None
    async for session in DatabaseManager.get_session():
        result = await session.execute(select(User).where(User.vk_id == user_vk_id))
        user = result.scalar_one_or_none()

    if user:
        await message.answer("Привет, выбери действие в меню снизу:",
                             keyboard=start_keyboard())

    else:
        await state_dispenser.set(user_vk_id, RegisterState.wait_username_state)
        await message.answer("Добро пожаловать! Чтобы начать регистрацию, нажми кнопку:\n"
                             "(чтобы отменить регистрацию введи команду /cansel)",
                             keyboard=register_button())
