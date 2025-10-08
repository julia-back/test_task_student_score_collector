from aiogram import types
from database import DatabaseManager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from users.models import User
from scores.models import Score
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_user_scores_from_inactive_buttons(user_scores: list[Score]):
    builder = InlineKeyboardBuilder()
    for score in user_scores:
        builder.button(text=f"{str(score.subject).title()} - {score.point}")
    return builder.adjust(1).as_markup()


async def view_user_scores(message: types.Message):
    user = None
    async for session in DatabaseManager.get_session():
        result = await session.execute(select(User).where(User.telegram_id == message.chat.id))
        user = result.scalar_one_or_none()
    if user:
        user_scores = user.scores
        buttons = await get_user_scores_from_inactive_buttons(user_scores)
        await message.answer(text="Ваши баллы:", reply_markup=buttons)
    else:
        await message.answer(text="Пользователь не зарегистрирован.")
