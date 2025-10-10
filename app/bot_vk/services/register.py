from vkbottle.bot import Message
from bot_vk.states import RegisterState, state_dispenser
from database import DatabaseManager
from users.models import User


async def start_register_ask_username(message: Message):
    user_vk_id = message.from_id
    await state_dispenser.set(user_vk_id, RegisterState.wait_username_state)
    await message.answer("Введите имя пользователя, оно должно быть уникальным:")


async def cansel_register(message: Message):
    await state_dispenser.delete(message.from_id)
    await message.answer("Регистрация отменена.")


async def save_username_ask_first_name(message: Message):
    username = message.text.strip()
    await state_dispenser.set(message.from_id, RegisterState.wait_first_name_state,
                              username=username)
    await message.answer("Введите Ваше имя:")


async def save_first_name_ask_last_name(message: Message):
    first_name = message.text.strip().title()
    state = await state_dispenser.get(message.from_id)
    username = state.payload.get("username")
    await state_dispenser.set(message.from_id, RegisterState.wait_last_name_state,
                              username=username, first_name=first_name)
    await message.answer("Введите фамилию:")


async def save_user_data_in_db(message: Message):
    try:
        last_name = message.text.strip().title()
        state = await state_dispenser.get(message.from_id)
        username = state.payload.get("username")
        first_name = state.payload.get("first_name")

        user = User(username=username, first_name=first_name,
                    last_name=last_name, vk_id=message.from_id)
        async for session in DatabaseManager.get_session():
            session.add(User)
            await session.commit()
            await session.refresh(user)

        await message.answer("Поздравляем, регистрация завершена!\n"
                             f"Имя пользователя: {user.username}\n"
                             f"Имя: {user.first_name}\n"
                             f"Фамилия: {user.last_name}\n")
    finally:
        await state_dispenser.delete(message.from_id)
