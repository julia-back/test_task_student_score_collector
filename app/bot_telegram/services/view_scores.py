from aiogram import types
from database import DatabaseManager
from sqlalchemy import select
from users.models import User
from aiogram.fsm.context import FSMContext
from bot_telegram.fsm_states import ViewScoresState
from sqlalchemy.orm import selectinload


async def ask_subject_for_view(message: types.Message, state: FSMContext):
    await message.answer(text="Введите название предмета или 'Все' для просмотра всех баллов.")
    await state.set_state(ViewScoresState.wait_subject)


async def view_user_scores(message: types.Message, state: FSMContext):
    user_scores = None
    async for session in DatabaseManager.get_session():
        result = await session.execute(
            select(User)
            .options(selectinload(User.scores))
            .where(User.telegram_id == message.chat.id)
        )
        user = result.scalar_one_or_none()

        if user:
            if message.text.lower() == "все":
                user_scores = user.scores
            else:
                user_scores = [score for score in user.scores
                               if score.subject.lower() == message.text.lower()]
        else:
            await message.answer(text="Пользователь не зарегистрирован.")
            await state.clear()
            return

    if not user_scores:
        await message.answer(text="Предмет не найден. Попробуйте еще раз.")
        return

    text = "Ваши баллы:"
    for score in user_scores:
        text += f"\n{str(score.subject).title()} - {score.point}"

    await message.answer(text=text)
    await state.clear()
