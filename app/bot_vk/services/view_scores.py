from bot_vk.states import ViewScoresState, state_dispenser
from database import DatabaseManager
from logging_config import app_logger
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from users.models import User
from vkbottle.bot import Message

logger = app_logger.getChild(__name__)


async def ask_subject_for_view_scores(message: Message):
    await state_dispenser.set(message.from_id, ViewScoresState.wait_subject)
    await message.answer(
        "Введите предмет, по которому необходимо посмотреть баллы:" "(или введите 'все' для просмотра всех баллов)"
    )


async def view_user_scores(message: Message):
    subject = message.text.strip()

    user_scores = None
    try:
        async for session in DatabaseManager.get_session():
            result = await session.execute(
                select(User).options(selectinload(User.scores)).where(User.vk_id == message.from_id)
            )
            user = result.scalar_one_or_none()

            if user:
                if subject.lower() == "все":
                    user_scores = user.scores
                else:
                    user_scores = [score for score in user.scores if score.subject.lower() == subject.lower()]
            else:
                await state_dispenser.delete(message.from_id)
                await message.answer("Пользователь не зарегистрирован.")
                return

            if (not user_scores) and subject.lower() != "все":
                await message.answer("Предмет не найден, попробуйте еще раз:")
                return
    except Exception:
        logger.critical("Error during get user scores.")

    text = "Ваши баллы:"
    for score in user_scores:
        text += f"\n{str(score.subject).title()} - {score.point}"

    await state_dispenser.delete(message.from_id)
    await message.answer(text)
