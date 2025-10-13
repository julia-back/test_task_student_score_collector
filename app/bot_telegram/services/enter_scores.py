from aiogram.fsm.context import FSMContext
from aiogram import types
from bot_telegram.fsm_states import EnterScoreState
from database import DatabaseManager
from scores.models import Score
from users.models import User
from sqlalchemy import select
from logging_config import app_logger


logger = app_logger.getChild(__name__)


async def ask_subject_for_enter_score(message: types.Message, state: FSMContext):
    await message.answer(text="Введите предмет, баллы которого хотите сохранить:")
    await state.set_state(EnterScoreState.wait_subject)


async def save_subject(message: types.Message, state: FSMContext):
    subject = message.text.strip().title()
    await state.update_data(subject=subject)
    return True


async def ask_point(message: types.Message, state: FSMContext):
    await message.answer(text="Введите баллы ЕГЭ:")
    await state.set_state(EnterScoreState.wait_score)


async def save_point(message: types.Message, state: FSMContext):
    str_point = message.text.strip()

    try:
        point = int(str_point)
    except ValueError:
        await message.answer(text="Некорректный ввод. Введите целое число баллов без лишних символов:")
        return

    if 0 <= point <= 100:
        await state.update_data(point=point)
    else:
        await message.answer(text="Некорректный ввод. Введите целое число от 0 до 100.")

    return True


async def save_score_in_db(message: types.Message, state: FSMContext):
    try:
        user = None
        async for session in DatabaseManager.get_session():
            result = await session.execute(select(User).where(User.telegram_id == message.chat.id))
            user = result.scalar_one_or_none()

        if user:
            user_id = user.id
        else:
            await state.clear()
            await message.answer(text="Пользоатель не зарегистрирован, пожалуйста, "
                                      "пройдите регистрацию.")
            return

        data = await state.get_data()
        subject = data.get("subject")
        point = data.get("point")

        score_for_save = Score(subject=subject, point=point, user_id=user_id)
        async for session in DatabaseManager.get_session():
            session.add(score_for_save)
            await session.commit()
            await session.refresh(score_for_save)

        await state.clear()
        await message.answer(text="Баллы успешно сохранены!\n"
                                  f"Предмет - {score_for_save.subject}\n"
                                  f"Балл ЕГЭ - {score_for_save.point}")
    except Exception:
        logger.critical("Error saving score in database.")
