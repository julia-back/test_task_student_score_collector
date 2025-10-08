from aiogram import types
from aiogram.fsm.context import FSMContext
from bot_telegram.fsm_states import RegistrationStates
from database import DatabaseManager
from sqlalchemy import select
from users.models import User
from bot_telegram.keyboards import get_start_keyboard


async def ask_username(message: types.Message, state: FSMContext):
    await message.answer(text="Введите имя пользователя, оно должно быть уникальным:")
    await state.set_state(RegistrationStates.wait_for_username)


async def check_unique_and_save_username(message: types.Message, state: FSMContext):
    username = message.text.strip()
    username_in_db = None
    async for session in DatabaseManager.get_session():
        result = await session.execute(select(User).where(User.username == username))
        username_in_db = result.scalar_one_or_none()

    if username_in_db:
        await message.answer(text="Имя пользователя уже существует. Попробуйте еще раз:")
    else:
        await state.update_data(username=username)


async def ask_first_name(message: types.Message, state: FSMContext):
    await message.answer(text="Введите ваше имя:")
    await state.set_state(RegistrationStates.wait_for_first_name)


async def save_first_name(message: types.Message, state: FSMContext):
    first_name = message.text.strip().title()
    await state.update_data(first_name=first_name)


async def ask_last_name(message: types.Message, state: FSMContext):
    await message.answer(text="Введите фамилию:")
    await state.set_state(RegistrationStates.wait_for_last_name)


async def save_last_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text.strip().title())


async def save_user_data_in_db(message: types.Message, state: FSMContext):
    user_data = state.get_data()
    username = user_data.get("username")
    first_name = user_data.get("first_name")
    last_name = user_data.get("last_name")

    user = User(username=username, first_name=first_name,
                last_name=last_name, telegram_id=message.chat.id)

    async for session in DatabaseManager.get_session():
        await session.add(user)
        await session.commit()

    await state.clear()
    await message.answer(text="Спасибо за Ваши ответы! Регистрация завершена.",
                         reply_markup=get_start_keyboard())


async def cansel_register(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Регистрация отменена.")
